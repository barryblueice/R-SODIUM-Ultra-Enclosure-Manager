# usb_monitor.py
import usb.core
from PySide6.QtCore import QThread
from PySide6.QtCore import Signal as pyqtSignal
from loguru import logger
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

    def create_packet(target: int, nvs_status: int, cmd: int, exclosure_status = 0x00, ext_gpio_config = 0x00, applied = 0x00) -> bytes:
        last_padded = bytes([applied]).ljust(27, b"\x00")
        data = bytes([target, cmd, nvs_status, exclosure_status, ext_gpio_config]) + last_padded
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
            resp = device.read(REPORT_SIZE, timeout_ms=100)
        except Exception as e:
            logger.error(e)

        if not resp:
            return None
        
    @staticmethod
    def hid_comm(
            device, 
            cmd: int,
            target = 0x00,
            nvs_status = 0x00, 
            exclosure_status = 0x00,
            ext_gpio_config = 0x00,
            applied = 0x00
            ):
        """HID通信函数

        Arguments:
            device -- 目标HID设备
            target -- 通信命令（0xFE，握手命令）/目标GPIO（0x01-0x2C）
            nvs_status -- 是否存储设置到NVS（0x01启用存储）
            cmd -- GPIO操作命令。
                0x00低电平
                0x01高电平
                0x02查询nvs存储的GPIO状态
                0x03查询当前GPIO电平状态
                0x04查询硬盘盒状态
                0x05硬盘盒模式存储
                0x06存储高电平时的GPIO状态
                0x07重新应用GPIO状态
                0x08SATA硬盘延时上电
                0x09查询SATA硬盘延时上电时间
                0x0A是否随主机端休眠
                0x0B查询随主机端休眠状态
                0x0C是否控制器卸载后休眠
                0x0D查询控制器卸载后休眠状态
            exclosure_status -- 设备状态。（默认为0x00，即Combine Mode）
            ext_gpio_config -- 存储高电平时的GPIO状态
            applied -- 立刻执行
        """

        packet = USBCommunicatorThread.create_packet(target, nvs_status, cmd, exclosure_status, ext_gpio_config, applied)
        device.write(packet)

        try:

            resp = device.read(REPORT_SIZE, timeout_ms=1000)

        except:

            return target,False
        
        if not resp:
            return None

        if all(b == 0xFF for b in resp):
            pass
        else:
            resp = bytes(resp)
            if USBCommunicatorThread.verify_response(resp):
                resp_cmd = resp[1:32].rstrip(b"\x00")
                return target,resp_cmd
            else:
                logger.error("HMAC Mismatch")
                return None
        
    def verify_rsodium_hid_controller(
            device: hid.device
            ) -> bool:
        packet = USBCommunicatorThread.create_packet(
            target=0xFE, 
            nvs_status=0x00, 
            cmd=0x00,)
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

            self.msleep(100)

    def stop(self):
        self.running = False