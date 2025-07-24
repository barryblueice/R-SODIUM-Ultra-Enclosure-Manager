# usb_monitor.py
import usb.core
from PySide6.QtCore import QThread
from PySide6.QtCore import Signal as pyqtSignal


class DeviceMonitorThread(QThread):
    device_event = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.running = True
        self.device_present = False

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
                    self.device_present = True
                    self.device_event.emit(True)

                elif not is_hid_device and self.device_present:
                    self.device_present = False
                    self.device_event.emit(False)
            except:
                pass

            self.msleep(1000)
