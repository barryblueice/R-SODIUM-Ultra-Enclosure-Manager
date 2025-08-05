from progressbar import ProgressWindow
from main_windows import MainWindow
from usb_module import USBCommunicatorThread

device = USBCommunicatorThread.dev

gpio_mode_id_list = {
    "11": 0x23,
    "12": 0x26,
    "13": 0x22,
    "21": 0x23,
    "22": 0x26,
    "23": 0x22,
}

def on_boxmode_execute_clicked(main_window: MainWindow):
    m_checked = []
    m_not_checked = []
    for i in [
        main_window.ui.combinemode,
        main_window.ui.nvmeonly,
        main_window.ui.sataonly,
        main_window.ui.hubonly
    ]:
        n = 0
        if i.isChecked():
            n = i.mode_id
            # print (n)
            break

    USB_COMM = USBCommunicatorThread()

    USB_COMM.hid_comm(device, target=n, cmd=0x05)

    match n:
        case 0: # COMBINE MODE
            for i in [
                main_window.ui.nvme_self_power_checkbox,
                main_window.ui.sata1_self_power_checkbox,
                main_window.ui.sata2_self_power_checkbox,
                main_window.ui.nvme_ext_power_checkbox,
                main_window.ui.sata1_ext_power_checkbox,
                main_window.ui.sata2_ext_power_checkbox,
            ]:
                if i.isChecked():
                    m_checked.append(i.mode_id)
                else:
                    m_not_checked.append(i.mode_id)

            for i in m_checked:

                if i.startswith('1'):
                    if not i.endswith(('0','1')):
                        USB_COMM.hid_comm(device, target=0x21, nvs_status=0x01, cmd=0x01)
                    USB_COMM.hid_comm(device, target=gpio_mode_id_list[i], nvs_status=0x01, cmd=0x01)
                else:
                    if not i.endswith(('0','1')):
                        USB_COMM.hid_comm(device, target=0x21, cmd=0x06, ext_gpio_config=0x01)
                    USB_COMM.hid_comm(device, target=gpio_mode_id_list[i], cmd=0x06, ext_gpio_config=0x01)

            for i in m_not_checked:
                if i.startswith('1'):
                    USB_COMM.hid_comm(device, target=gpio_mode_id_list[i], nvs_status=0x01, cmd=0x00)
                else:
                    USB_COMM.hid_comm(device, target=gpio_mode_id_list[i], cmd=0x06, ext_gpio_config=0x00)

            if "12" in m_not_checked and "13" in m_not_checked:
                USB_COMM.hid_comm(device, target=0x21, nvs_status=0x01, cmd=0x00)
                
            if "22" in m_not_checked and "23" in m_not_checked:
                USB_COMM.hid_comm(device, target=0x21, cmd=0x06, ext_gpio_config=0x00)


            USB_COMM.hid_comm(device, target=0x00, cmd=0xfd)

            # USB_COMM.hid_comm(device, target=0x21, nvs_status=0x01, cmd=0x01)
            # USB_COMM.hid_comm(device, target=0x23, nvs_status=0x01, cmd=0x01)
            # pass
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