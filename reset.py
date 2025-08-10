from PySide6.QtCore import QObject, Signal, Slot, QThread

from progressbar import ProgressWindow
from main_windows import MainWindow
from usb_module import USBCommunicatorThread

USB_COMM = USBCommunicatorThread()
device = USBCommunicatorThread.dev

class RESETHandler(QObject):
    finished = Signal()

    def __init__(self, device):
        super().__init__()
        self.device = device

    @Slot()
    def run(self):
        USB_COMM.hid_comm(self.device, cmd=0xFC)
        self.finished.emit()

def on_reset_execute_clicked(main_window: MainWindow):

    main_window.progress_window = ProgressWindow(main_window=main_window)
    main_window.progress_window.progressbar_start()

    thread = QThread()
    worker = RESETHandler(device)
    worker.moveToThread(thread)

    main_window.reset_thread = thread
    main_window.reset_worker = worker

    thread.started.connect(worker.run)
    worker.finished.connect(thread.quit)
    worker.finished.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)

    def cleanup():
        main_window.reset_thread = None
        main_window.reset_worker = None

    thread.finished.connect(cleanup)

    thread.start()