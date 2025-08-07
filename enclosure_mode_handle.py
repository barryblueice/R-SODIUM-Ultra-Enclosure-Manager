from PySide6.QtCore import QObject, Signal, Slot, QThread

from progressbar import ProgressWindow
from main_windows import MainWindow
from usb_module import USBCommunicatorThread

import time

gpio_mode_id_list = {
    "11": 0x23,
    "12": 0x26,
    "13": 0x22,
    "21": 0x23,
    "22": 0x26,
    "23": 0x22,
}

class EnclosureModeHandler(QObject):
    finished = Signal()

    def __init__(self, main_window: MainWindow, device):
        super().__init__()
        self.main_window = main_window
        self.device = device

    @Slot()
    def run(self):
        m_checked = []
        m_not_checked = []
        device = USBCommunicatorThread.dev
        for i in [
            self.main_window.ui.combinemode,
            self.main_window.ui.nvmeonly,
            self.main_window.ui.sataonly,
            self.main_window.ui.hubonly
        ]:
            n = 0
            if i.isChecked():
                n = i.mode_id
                break

        USBCommunicatorThread.hid_comm(device, target=n, cmd=0x05)

        if self.main_window.ui.suspend_enable.isChecked():
            USBCommunicatorThread.hid_comm(device, target=0x01, cmd=0x0A)
        else:
            USBCommunicatorThread.hid_comm(device, target=0x00, cmd=0x0A)

        if self.main_window.ui.unmounted_suspend_enable.isChecked():
            USBCommunicatorThread.hid_comm(device, target=0x01, cmd=0x0C)
        else:
            USBCommunicatorThread.hid_comm(device, target=0x00, cmd=0x0C)

        match n:
            case 0: # COMBINE MODE
                for i in [
                    self.main_window.ui.nvme_self_power_checkbox,
                    self.main_window.ui.sata1_self_power_checkbox,
                    self.main_window.ui.sata2_self_power_checkbox,
                    self.main_window.ui.nvme_ext_power_checkbox,
                    self.main_window.ui.sata1_ext_power_checkbox,
                    self.main_window.ui.sata2_ext_power_checkbox,
                ]:
                    if i.isChecked():
                        m_checked.append(i.mode_id)
                    else:
                        m_not_checked.append(i.mode_id)

                for i in m_checked:

                    if i.startswith('1'):
                        if not i.endswith(('0','1')):
                            USBCommunicatorThread.hid_comm(device, target=0x21, nvs_status=0x01, cmd=0x01)
                        USBCommunicatorThread.hid_comm(device, target=gpio_mode_id_list[i], nvs_status=0x01, cmd=0x01)
                    else:
                        if not i.endswith(('0','1')):
                            USBCommunicatorThread.hid_comm(device, target=0x21, cmd=0x06, ext_gpio_config=0x01)
                        USBCommunicatorThread.hid_comm(device, target=gpio_mode_id_list[i], cmd=0x06, ext_gpio_config=0x01)

                for i in m_not_checked:
                    if i.startswith('1'):
                        USBCommunicatorThread.hid_comm(device, target=gpio_mode_id_list[i], nvs_status=0x01, cmd=0x00)
                    else:
                        USBCommunicatorThread.hid_comm(device, target=gpio_mode_id_list[i], cmd=0x06, ext_gpio_config=0x00)

                if "12" in m_not_checked and "13" in m_not_checked:
                    USBCommunicatorThread.hid_comm(device, target=0x21, nvs_status=0x01, cmd=0x00)

                if "22" in m_not_checked and "23" in m_not_checked:
                    USBCommunicatorThread.hid_comm(device, target=0x21, cmd=0x06, ext_gpio_config=0x00)


                USBCommunicatorThread.hid_comm(device, target=0x00, cmd=0xfd)

            case 1: # ASM2362 ONLY
                USBCommunicatorThread.hid_comm(device, target=0x21, nvs_status=0x01, cmd=0x00)
                USBCommunicatorThread.hid_comm(device, target=0x22, nvs_status=0x01, cmd=0x00)
                USBCommunicatorThread.hid_comm(device, target=0x23, nvs_status=0x01, cmd=0x01)
                USBCommunicatorThread.hid_comm(device, target=0x26, nvs_status=0x01, cmd=0x00)
            case 2: # ASM1352R ONLY
                USBCommunicatorThread.hid_comm(device, target=0x21, nvs_status=0x01, cmd=0x01)
                USBCommunicatorThread.hid_comm(device, target=0x22, nvs_status=0x01, cmd=0x01)
                USBCommunicatorThread.hid_comm(device, target=0x23, nvs_status=0x01, cmd=0x00)
                USBCommunicatorThread.hid_comm(device, target=0x26, nvs_status=0x01, cmd=0x01)
            case _: # HUB ONLY or other condition
                USBCommunicatorThread.hid_comm(device, target=0x21, nvs_status=0x01, cmd=0x00)
                USBCommunicatorThread.hid_comm(device, target=0x22, nvs_status=0x01, cmd=0x00)
                USBCommunicatorThread.hid_comm(device, target=0x23, nvs_status=0x01, cmd=0x00)
                USBCommunicatorThread.hid_comm(device, target=0x26, nvs_status=0x01, cmd=0x00)

        self.finished.emit()

def on_boxmode_execute_clicked(main_window: MainWindow):
    device = USBCommunicatorThread.dev
    main_window.progress_window = ProgressWindow(main_window=main_window)
    main_window.progress_window.progressbar_start()

    thread = QThread()
    worker = EnclosureModeHandler(main_window, device)
    worker.moveToThread(thread)

    main_window.boxmode_thread = thread
    main_window.boxmode_worker = worker

    thread.started.connect(worker.run)

    def cleanup():
        main_window.boxmode_thread = None
        main_window.boxmode_worker = None

    worker.finished.connect(thread.quit)
    worker.finished.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)
    thread.finished.connect(cleanup)

    thread.start()