from PySide6.QtCore import QObject, Signal, Slot, QThread
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from progressbar import ProgressWindow
from main_windows import MainWindow
from usb_module import USBCommunicatorThread

USB_COMM = USBCommunicatorThread()
device = USBCommunicatorThread.dev

_reset_status = 0

class RESETHandler(QObject):
    finished = Signal()

    def __init__(self, device):
        super().__init__()
        self.device = device

    @Slot()
    def run(self):
        if _reset_status == 0:
            USB_COMM.hid_comm(self.device, cmd=0xFC)
            self.finished.emit()
        elif _reset_status == 1:
            USB_COMM.hid_comm(self.device, cmd=0xFB)
            self.finished.emit()

def dfu_message_box(main_window):
    main_window.dfu_msg_box = QMessageBox()
    msg = main_window.dfu_msg_box
    msg.setWindowTitle("DFU Firmware Update")
    msg.setTextFormat(Qt.RichText)
    msg.setText(
        "The controller will automatically reboot and enter DFU mode, "
        "enabling firmware updates via the <a href='https://dfu.stetelthings.com/'>ESP32-S2 Web Flasher</a>.<br><br>"
        "<b>Important Notes:</b><br>"
        "1. Only firmware files named according to the pattern '*-dfu.bin' are supported for DFU updates.<br>"
        "2. After completing the DFU update, please re-unplug the enclosure to apply the updated firmware.<br><br>"
        "<span style='color:red; font-weight:bold;'>Warning: After completing the DFU update and unplugging the device, you must wait until the controller is FULLY EJECTED before reconnecting it to the host; otherwise, Controller recognition may fail."
    )
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setTextInteractionFlags(Qt.TextBrowserInteraction)
    msg.setWindowModality(Qt.ApplicationModal)
    msg.setWindowFlag(Qt.WindowStaysOnTopHint)
    msg.setWindowIcon(QIcon("icon.ico"))
    msg.show()

def on_reset_execute_clicked(main_window: MainWindow):

    global _reset_status

    _reset_status = 0

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

def on_dfu_reset_execute_clicked(main_window: MainWindow):

    global _reset_status

    dfu_message_box(main_window)

    _reset_status = 1
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