# usb_monitor.py
import usb.core
from PyQt6.QtCore import QThread, pyqtSignal


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
                is_mass_storage = False
                if dev:
                    try:
                        for cfg in dev:
                            for intf in cfg:
                                if intf.bInterfaceClass == 0x08:
                                    is_mass_storage = True
                                    break
                            if is_mass_storage:
                                break
                    except usb.core.USBError:
                        pass

                if is_mass_storage and not self.device_present:
                    self.device_present = True
                    self.device_event.emit(True)

                elif not is_mass_storage and self.device_present:
                    self.device_present = False
                    self.device_event.emit(False)
            except:
                pass

            self.msleep(1000)
