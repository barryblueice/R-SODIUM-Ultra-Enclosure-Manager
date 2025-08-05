from progressbar import ProgressWindow
from main_windows import MainWindow

from usb_module import USBCommunicatorThread

USB_COMM = USBCommunicatorThread()
device = USBCommunicatorThread.dev

def on_sata_execute_clicked(main_window: MainWindow):
    sata_onpower = int(main_window.ui.powertime.text())
    USB_COMM.hid_comm(device, target=sata_onpower, cmd=0x08)
    main_window.progress_window = ProgressWindow(main_window=main_window)
    main_window.progress_window.progressbar_start()