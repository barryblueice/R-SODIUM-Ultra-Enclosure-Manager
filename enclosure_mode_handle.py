from progressbar import ProgressWindow
from main_windows import MainWindow
from usb_module import USBCommunicatorThread

device = USBCommunicatorThread.dev

def on_boxmode_execute_clicked(main_window: MainWindow):
    for i in [
        main_window.ui.combinemode,
        main_window.ui.hubonly,
        main_window.ui.sataonly,
        main_window.ui.nvmeonly
    ]:
        if i.isChecked():
            print(i.text())
            break
    resp = USBCommunicatorThread.hid_comm(
        device, 
        target=0x01, 
        nvs_status=0x00, cmd=0x02)
    main_window.progress_window = ProgressWindow(main_window=main_window)
    main_window.progress_window.progressbar_start()