from PySide6.QtCore import QObject, Signal, Slot, QThread

from progressbar import ProgressWindow
from main_windows import MainWindow
from usb_module import USBCommunicatorThread

import time

USB_COMM = USBCommunicatorThread()
device = USBCommunicatorThread.dev

class SATAHandler(QObject):
    finished = Signal()

    def __init__(self, device, n, sata_onpower):
        super().__init__()
        self.device = device
        self.n = n
        self.sata_onpower = sata_onpower

    @Slot()
    def run(self):
        match self.n:
            case 30:
                USB_COMM.hid_comm(self.device,target=0x24,nvs_status=0x01,cmd=0x00)
                USB_COMM.hid_comm(self.device,target=0x25,nvs_status=0x01,cmd=0x01)
            case 31:
                USB_COMM.hid_comm(self.device,target=0x24,nvs_status=0x01,cmd=0x01)
                USB_COMM.hid_comm(self.device,target=0x25,nvs_status=0x01,cmd=0x00)
            case 32:
                USB_COMM.hid_comm(self.device,target=0x24,nvs_status=0x01,cmd=0x00)
                USB_COMM.hid_comm(self.device,target=0x25,nvs_status=0x01,cmd=0x00)
            case _:
                USB_COMM.hid_comm(self.device,target=0x24,nvs_status=0x01,cmd=0x01)
                USB_COMM.hid_comm(self.device,target=0x25,nvs_status=0x01,cmd=0x01)

        USB_COMM.hid_comm(self.device, target=0x15, cmd=0x00)
        time.sleep(6)
        USB_COMM.hid_comm(self.device, target=0x15, cmd=0x01)
        USB_COMM.hid_comm(self.device, target=self.sata_onpower, cmd=0x08)

        self.finished.emit()

def on_sata_execute_clicked(main_window: MainWindow):
    n = 0
    for i in [
        main_window.ui.R0,
        main_window.ui.R1,
        main_window.ui.PM,
        main_window.ui.JBOD
    ]:
        if i.isChecked():
            n = i.mode_id
            break

    sata_onpower = int(main_window.ui.powertime.text())

    main_window.progress_window = ProgressWindow(main_window=main_window)
    main_window.progress_window.progressbar_start()

    thread = QThread()
    worker = SATAHandler(device, n, sata_onpower)
    worker.moveToThread(thread)

    # 保持引用
    main_window.sata_thread = thread
    main_window.sata_worker = worker

    thread.started.connect(worker.run)
    worker.finished.connect(thread.quit)
    worker.finished.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)

    def cleanup():
        main_window.sata_thread = None
        main_window.sata_worker = None

    thread.finished.connect(cleanup)

    thread.start()