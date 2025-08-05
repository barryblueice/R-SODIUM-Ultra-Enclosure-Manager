from progressbar import ProgressWindow
from main_windows import MainWindow
from usb_module import USBCommunicatorThread

device = USBCommunicatorThread.dev

def on_boxmode_execute_clicked(main_window: MainWindow):
    for i in [
        main_window.ui.combinemode,
        main_window.ui.nvmeonly,
        main_window.ui.sataonly,
        main_window.ui.hubonly
    ]:
        n = 0
        if i.isChecked():
            n = i.mode_id
            print (n)
            break

    USB_COMM = USBCommunicatorThread()

    match n:
        case 0: # COMBINE MODE
            # USB_COMM.hid_comm(device, target=0x21, nvs_status=0x01, cmd=0x01)
            # USB_COMM.hid_comm(device, target=0x23, nvs_status=0x01, cmd=0x01)
            pass
        case 1: # ASM2362 ONLY
            USB_COMM.hid_comm(device, target=0x21, nvs_status=0x01, cmd=0x00)
            USB_COMM.hid_comm(device, target=0x22, nvs_status=0x01, cmd=0x00)
            USB_COMM.hid_comm(device, target=0x23, nvs_status=0x01, cmd=0x01)
            USB_COMM.hid_comm(device, target=0x26, nvs_status=0x01, cmd=0x00)
        case 2: # ASM1352R ONLY
            USB_COMM.hid_comm(device, target=0x21, nvs_status=0x01, cmd=0x01)
            USB_COMM.hid_comm(device, target=0x22, nvs_status=0x01, cmd=0x01)
            USB_COMM.hid_comm(device, target=0x23, nvs_status=0x01, cmd=0x00)
            USB_COMM.hid_comm(device, target=0x26, nvs_status=0x01, cmd=0x01)
        case _: # HUB ONLY or other condition
            USB_COMM.hid_comm(device, target=0x21, nvs_status=0x01, cmd=0x00)
            USB_COMM.hid_comm(device, target=0x22, nvs_status=0x01, cmd=0x00)
            USB_COMM.hid_comm(device, target=0x23, nvs_status=0x01, cmd=0x00)
            USB_COMM.hid_comm(device, target=0x26, nvs_status=0x01, cmd=0x00)

    main_window.progress_window = ProgressWindow(main_window=main_window)
    main_window.progress_window.progressbar_start()