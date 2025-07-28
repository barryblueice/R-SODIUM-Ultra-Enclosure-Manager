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

class DeviceMonitorThread(QThread):
    device_event = pyqtSignal(bool)
    dev = hid.device()

    def __init__(self):
        super().__init__()
        self.running = True
        self.device_present = False

    def calc_hmac(data: bytes) -> bytes:
        return hmac.new(HMAC_KEY, data, hashlib.sha256).digest()

    def create_packet(cmd: int, payload) -> bytes:
        if isinstance(payload, int):
            payload = bytes([payload])
        elif isinstance(payload, str):
            payload = payload.encode()
        elif not isinstance(payload, bytes):
            raise TypeError

        payload_padded = payload.ljust(31, b"\x00")
        data = bytes([cmd]) + payload_padded
        mac = DeviceMonitorThread.calc_hmac(data)
        return bytes([REPORT_ID]) + data + mac


    def verify_response(resp: bytes) -> bool:
        if len(resp) < REPORT_SIZE:
            return False
        data = resp[:32]
        recv_mac = resp[32:64]
        calc_mac = DeviceMonitorThread.calc_hmac(data)
        return calc_mac == recv_mac

    def send_command_and_wait_response(device, cmd: int, payload: bytes = b''):
        if isinstance(payload, int):
            payload = bytes([payload])
        elif isinstance(payload, str):
            payload = payload.encode()
        elif not isinstance(payload, bytes):
            raise TypeError()

        packet = DeviceMonitorThread.create_packet(cmd, payload)
        # print (list(packet))
        device.write(packet)

        try:
            resp = device.read(REPORT_SIZE, timeout_ms=1000)
        except Exception as e:
            return None

        if not resp:
            return None
        
    def send_command_and_wait_response(device, cmd: int, payload: bytes = b''):
        if isinstance(payload, int):
            payload = bytes([payload])
        elif isinstance(payload, str):
            payload = payload.encode()
        elif not isinstance(payload, bytes):
            raise TypeError()

        packet = DeviceMonitorThread.create_packet(cmd, payload)
        device.write(packet)

        try:
            resp = device.read(REPORT_SIZE, timeout_ms=1000)
        except Exception as e:
            return None

        if not resp:
            return None
        
    def verify_rsodium_hid_controller(
            device: hid.device,
            cmd: int,
            payload: bytes = b'') -> tuple[int, bytes] | None:
        packet = DeviceMonitorThread.create_packet(cmd, payload)
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
                    DeviceMonitorThread.dev.open(VID, PID)
                    if DeviceMonitorThread.verify_rsodium_hid_controller(DeviceMonitorThread.dev, 0xFE, b'\x00'):
                        self.device_present = True
                        self.device_event.emit(True)
                    else:
                        dev.close()
                        self.device_present = False
                        self.device_event.emit(False)

                elif not is_hid_device and self.device_present:
                    self.device_present = False
                    self.device_event.emit(False)
            except:
                pass

            self.msleep(1000)
