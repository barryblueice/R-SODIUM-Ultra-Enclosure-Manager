from progressbar import ProgressWindow
from main_windows import MainWindow

from usb_module import USBCommunicatorThread

import time

USB_COMM = USBCommunicatorThread()
device = USBCommunicatorThread.dev

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

    match n:
        case 30:
            USB_COMM.hid_comm(device,target=0x24,nvs_status=0x01,cmd=0x00)
            USB_COMM.hid_comm(device,target=0x25,nvs_status=0x01,cmd=0x01)
        case 31:
            USB_COMM.hid_comm(device,target=0x24,nvs_status=0x01,cmd=0x01)
            USB_COMM.hid_comm(device,target=0x25,nvs_status=0x01,cmd=0x00)
        case 32:
            USB_COMM.hid_comm(device,target=0x24,nvs_status=0x01,cmd=0x00)
            USB_COMM.hid_comm(device,target=0x25,nvs_status=0x01,cmd=0x00)
        case _:
            USB_COMM.hid_comm(device,target=0x24,nvs_status=0x01,cmd=0x01)
            USB_COMM.hid_comm(device,target=0x25,nvs_status=0x01,cmd=0x01)

    sata_onpower = int(main_window.ui.powertime.text())
    USB_COMM.hid_comm(device, target=0x15, cmd=0x00)
    time.sleep(6)
    USB_COMM.hid_comm(device, target=0x15, cmd=0x01)
    USB_COMM.hid_comm(device, target=sata_onpower, cmd=0x08)
    main_window.progress_window = ProgressWindow(main_window=main_window)
    main_window.progress_window.progressbar_start()