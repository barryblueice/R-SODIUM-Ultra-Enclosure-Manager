# usb_monitor.py
import usb.core
from PySide6.QtCore import QThread
from PySide6.QtCore import Signal as pyqtSignal
import hid
import hmac
import hashlib

HMAC_KEY = b"a0HyIvVM6A6Z7dTPYrAk8s3Mpouh"

VID = 0x0D00
PID = 0x0721
REPORT_ID = 0x00
REPORT_SIZE = 64

class USBCommunicatorThread(QThread):
    device_event = pyqtSignal(bool)
    dev = hid.device()

    def __init__(self):
        super().__init__()
        self.running = True
        self.device_present = False

    def calc_hmac(data: bytes) -> bytes:
        return hmac.new(HMAC_KEY, data, hashlib.sha256).digest()

    def create_packet(target: int, nvs_status: int, cmd) -> bytes:
        if isinstance(cmd, int):
            cmd = bytes([cmd])
        elif isinstance(cmd, str):
            cmd = cmd.encode()
        elif not isinstance(cmd, bytes):
            raise TypeError

        cmd_padded = cmd.ljust(30, b"\x00")
        data = bytes([target]) + cmd_padded + bytes([nvs_status])
        mac = USBCommunicatorThread.calc_hmac(data)
        return bytes([REPORT_ID]) + data + mac


    def verify_response(resp: bytes) -> bool:
        if len(resp) < REPORT_SIZE:
            return False
        data = resp[:32]
        recv_mac = resp[32:64]
        calc_mac = USBCommunicatorThread.calc_hmac(data)
        return calc_mac == recv_mac

    def send_command_and_wait_response(device, cmd: int, payload: bytes = b''):
        if isinstance(payload, int):
            payload = bytes([payload])
        elif isinstance(payload, str):
            payload = payload.encode()
        elif not isinstance(payload, bytes):
            raise TypeError()

        packet = USBCommunicatorThread.create_packet(cmd, payload)
        # print (list(packet))
        device.write(packet)

        try:
            resp = device.read(REPORT_SIZE, timeout_ms=1000)
        except Exception as e:
            return None

        if not resp:
            return None
        
    @staticmethod
    def hid_comm(
            device, 
            target: int, 
            nvs_status: int, 
            cmd: bytes = b''
            ):
        """HID通信函数

        Arguments:
            device -- 目标HID设备
            target -- 通信命令（0xFE，握手命令）/目标GPIO（0x01-0x2C）
            nvs_status -- 是否存储设置到NVS（0x01启用存储）
            cmd -- GPIO操作命令（0x00低电平、0x01高电平、0x02查询nvs存储状态、0x03查询GPIO电平状态）
        """

        if isinstance(cmd, int):
            cmd = bytes([cmd])
        elif isinstance(cmd, str):
            cmd = cmd.encode()
        elif not isinstance(cmd, bytes):
            raise TypeError()

        packet = USBCommunicatorThread.create_packet(target, nvs_status, cmd)
        # print (list(packet))
        device.write(packet)

        try:
            resp = device.read(REPORT_SIZE, timeout_ms=1000)
        except Exception as e:
            return None

        if not resp:
            return None

        resp = bytes(resp)
        if USBCommunicatorThread.verify_response(resp):
            resp_target = resp[0]
            resp_cmd = resp[1:32].rstrip(b"\x00")
            # print(f"Received valid response. target: {resp_target:#02x}, cmd: {resp_cmd}")
            return resp_target, resp_cmd
        else:
            return None
        
    def verify_rsodium_hid_controller(
            device: hid.device
            ) -> bool:
        packet = USBCommunicatorThread.create_packet(
            target=0xFE, 
            nvs_status=0x00, 
            cmd=0x00)
        device.write(packet)
        try:
            resp = bytes(device.read(REPORT_SIZE, timeout_ms=1000))
            return b"PONG" == resp[1:32].rstrip(b"\x00")
        except:
            return False


    def run(self):
        while self.running:
            try:
                dev = usb.core.find(idVendor=0x0D00, idProduct=0x0721)
                is_hid_device = False
                if dev:
                    try:
                        for cfg in dev:
                            for intf in cfg:
                                if intf.bInterfaceClass == 0x03:
                                    is_hid_device = True
                                    break
                            if is_hid_device:
                                break
                    except usb.core.USBError:
                        pass

                if is_hid_device and not self.device_present:
                    USBCommunicatorThread.dev.open(VID, PID)
                    if USBCommunicatorThread.verify_rsodium_hid_controller(USBCommunicatorThread.dev):
                        self.device_present = True
                        self.device_event.emit(True)
                    else:
                        self.device_present = False
                        self.device_event.emit(False)
                        USBCommunicatorThread.dev.close()

                elif not is_hid_device and self.device_present:
                    self.device_present = False
                    self.device_event.emit(False)
                    USBCommunicatorThread.dev.close()
            except:
                pass

            self.msleep(1000)