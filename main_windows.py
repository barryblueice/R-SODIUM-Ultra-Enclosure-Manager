from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from Ui_ultra_enclosure_manager import Ui_main_interface
from PySide6.QtWidgets import QSystemTrayIcon, QGroupBox, QMenu
from pyqttoast import Toast, ToastIcon

import usb_module
import groupboxcontroller
import time

device = usb_module.USBCommunicatorThread.dev

gpio_mode_id_list = {
    "11": 0x23,
    "12": 0x26,
    "13": 0x22,
    "21": 0x23,
    "22": 0x26,
    "23": 0x22,
}

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main_interface()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui_state(False)
        self.global_status = False

        self.monitor_thread = usb_module.USBCommunicatorThread()
        self.monitor_thread.device_event.connect(self.on_device_status_changed)
        self.monitor_thread.start()

        self.groupbox_list = []
        self.groupbox_list.append(self.ui.overview)
        self.groupbox_list.append(self.ui.sataconfig)
        self.groupbox_list.append(self.ui.boxmode)
        self.groupbox_list.append(self.ui.about)
        self.controller = groupboxcontroller.GroupVisibilityController()
        self.controller.switch_signal.connect(self.show_only_one)
        self.controller.set_all_widgets(self.groupbox_list)

        self.ui.sataconfig.setVisible(False)
        self.ui.boxmode.setVisible(False)
        self.ui.about.setVisible(False)

        self.tray_icon = QSystemTrayIcon(QIcon("icon.ico"), self)
        self.tray_icon.setToolTip("R-SODIUM Ultra Enclosure Manager")

        tray_menu = QMenu()
        show_action = tray_menu.addAction("Show")
        quit_action = tray_menu.addAction("Exit")

        show_action.triggered.connect(self.show)
        quit_action.triggered.connect(QtWidgets.QApplication.quit)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.tray_icon.activated.connect(self.on_tray_icon_activated)

    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.show()
            self.activateWindow()

    def closeEvent(self, event):
        toast = Toast(self)
        toast.setAlwaysOnMainScreen(True)
        toast.setText('The program has minimized to tray.')
        toast.setIcon(ToastIcon.INFORMATION)
        toast.setIconColor(None)
        toast.setShowIcon(True)
        toast.setShowDurationBar(False)
        toast.setDuration(3000)
        toast.show()

        if self.monitor_thread.isRunning():
            self.monitor_thread.stop()
            self.monitor_thread.wait()
            event.accept()

    def ui_state(self,status: bool):
        self.ui.boxmode.setEnabled(status)
        self.ui.sataconfig.setEnabled(status)
        self.ui.SATA_Interface_button.setEnabled(status)
        self.ui.boxmode_button.setEnabled(status)

    def on_device_status_changed(self, status: bool):
        toast = Toast(self)
        toast.setAlwaysOnMainScreen(True)
        self.ui_state(status=status)
        self.overview_status_changed(status=status)
        self.connect_event_handle(status=status)
        if status:
            if self.global_status != status:
                toast.setText('A new Ultra SSD Enclosure device has detected!')
                toast.setIcon(ToastIcon.SUCCESS)
        else:
            toast.setText('The Ultra SSD Enclosure device has been removed!')
            toast.setIcon(ToastIcon.INFORMATION)
            self.global_status = False
        toast.setIconColor(None)
        toast.setShowIcon(True)
        toast.setShowDurationBar(False)
        toast.setDuration(3000)
        toast.show()

    def show_only_one(self, target_widget):
        gb: QGroupBox
        for gb in self.groupbox_list:
            gb.setVisible(gb == target_widget)

    def overview_status_changed(self, status: bool):

        a = {}
            
        if status:

            # try:

                for i in [0x01,0x22,0x23,0x26]:
                        
                    while True:
                        target,resp = usb_module.USBCommunicatorThread.hid_comm(
                        device, 
                        target=i,
                        cmd=0x03)

                        if target == i:

                            if resp == b'HIGH':

                                a.update({i:["True","#06B025"]})

                            else:

                                a.update({i:["False","#FF0000"]})

                        break

                for i in a.keys():

                    match i:

                        case 0x01:

                            self.ui.ext_power_status.setText(a[i][0])
                            self.ui.ext_power_status.setStyleSheet(f"color: {a[i][1]};")

                        case 0x22:

                            self.ui.sata2_status.setText(a[i][0])
                            self.ui.sata2_status.setStyleSheet(f"color: {a[i][1]};")

                        case 0x23:

                            self.ui.nvme_status.setText(a[i][0])
                            self.ui.nvme_status.setStyleSheet(f"color: {a[i][1]};")

                        case 0x26:

                            self.ui.sata1_status.setText(a[i][0])
                            self.ui.sata1_status.setStyleSheet(f"color: {a[i][1]};")

                        case _:

                            pass

            # except:

            #     pass
                
            # try:

            #     target,resp = usb_module.USBCommunicatorThread.hid_comm(
            #         device, 
            #         target=0x26,
            #         cmd=0x02)
                
            #     if resp == b'HIGH':

            #         self.ui.sata1_status.setText("True")
            #         self.ui.sata1_status.setStyleSheet("color: #06B025;")

            #     else:

            #         self.ui.sata1_status.setText("False")
            #         self.ui.sata1_status.setStyleSheet("color: #FF0000;")

            #     target,resp = usb_module.USBCommunicatorThread.hid_comm(
            #         device, 
            #         target=0x22,
            #         cmd=0x02)
                
            #     if resp == b'HIGH':

            #         self.ui.sata2_status.setText("True")
            #         self.ui.sata2_status.setStyleSheet("color: #06B025;")

            #     else:

            #         self.ui.sata2_status.setText("False")
            #         self.ui.sata2_status.setStyleSheet("color: #FF0000;")

            #     target,resp = usb_module.USBCommunicatorThread.hid_comm(
            #         device, 
            #         target=0x23,
            #         cmd=0x02)
                
            #     if resp == b'HIGH':

            #         self.ui.nvme_status.setText("True")
            #         self.ui.nvme_status.setStyleSheet("color: #06B025;")

            #     else:

            #         self.ui.nvme_status.setText("False")
            #         self.ui.nvme_status.setStyleSheet("color: #FF0000;")

            #     target,resp = usb_module.USBCommunicatorThread.hid_comm(
            #         device, 
            #         target=0x01, 
            #         cmd=0x03)
                
            #     if resp == b'HIGH':

            #         self.ui.ext_power_status.setText("True")
            #         self.ui.ext_power_status.setStyleSheet("color: #06B025;")

            #     else:

            #         self.ui.ext_power_status.setText("False")
            #         self.ui.ext_power_status.setStyleSheet("color: #FF0000;")

            # except:
                
            #     pass

        else:

            self.ui.nvme_status.setText("None")
            self.ui.nvme_status.setStyleSheet("color: #000000;")
            self.ui.sata1_status.setText("None")
            self.ui.sata1_status.setStyleSheet("color: #000000;")
            self.ui.sata2_status.setText("None")
            self.ui.sata2_status.setStyleSheet("color: #000000;")
            self.ui.ext_power_status.setText("None")
            self.ui.ext_power_status.setStyleSheet("color: #000000;")

    def connect_event_handle(self, status: bool):
        try:

            if status:

                target,resp = usb_module.USBCommunicatorThread.hid_comm(
                    device, 
                    target=0x00, 
                    nvs_status=0x00, 
                    cmd=0x04)
                
                for i in [
                    self.ui.combinemode,
                    self.ui.nvmeonly,
                    self.ui.sataonly,
                    self.ui.hubonly
                ]:
                    if getattr(i, 'mode_id', None) == int.from_bytes(resp, byteorder='big'):
                        i.setChecked(True)
                        break

                if resp == bytes(0):
                    self.ui.selfpowered_groupbox.setEnabled(True)
                    self.ui.extpowered_groupbox.setEnabled(True)
                else:
                    self.ui.selfpowered_groupbox.setEnabled(False)
                    self.ui.extpowered_groupbox.setEnabled(False)

                m_checked = []

                for i in gpio_mode_id_list:
                    if i.startswith("1"):
                        target,resp = usb_module.USBCommunicatorThread.hid_comm(
                            device, 
                            target=gpio_mode_id_list[i],
                            cmd=0x02)
                    else:
                        target,resp = usb_module.USBCommunicatorThread.hid_comm(
                            device, 
                            target=gpio_mode_id_list[i],
                            cmd=0x07)
                        
                    if resp == b"HIGH":
                        m_checked.append(i)

                    # print (resp)

                for i in [
                    self.ui.nvme_self_power_checkbox,
                    self.ui.sata1_self_power_checkbox,
                    self.ui.sata2_self_power_checkbox,
                    self.ui.nvme_ext_power_checkbox,
                    self.ui.sata1_ext_power_checkbox,
                    self.ui.sata2_ext_power_checkbox
                ]:
                    if getattr(i, 'mode_id', None) in m_checked:
                        i.setChecked(True)
                    else:
                        i.setChecked(False)

                target,resp = usb_module.USBCommunicatorThread.hid_comm(
                    device, 
                    cmd=0x09)
                
                self.ui.powertime.setValue(int.from_bytes(resp, byteorder='big'))

                target,resp = usb_module.USBCommunicatorThread.hid_comm(
                    device, 
                    cmd=0x0B)
                
                if resp == b'HIGH':
                    self.ui.suspend_enable.setChecked(True)
                else:
                    self.ui.suspend_enable.setChecked(False)

                target,resp = usb_module.USBCommunicatorThread.hid_comm(
                    device, 
                    cmd=0x0D)
                
                if resp == b'HIGH':
                    self.ui.unmounted_suspend_enable.setChecked(True)
                else:
                    self.ui.unmounted_suspend_enable.setChecked(False)

                target,resp1 = usb_module.USBCommunicatorThread.hid_comm(device,target=0x24,cmd=0x02)
                target,resp2 = usb_module.USBCommunicatorThread.hid_comm(device,target=0x25,cmd=0x02)

                for i in [
                    self.ui.R0,
                    self.ui.R1,
                    self.ui.PM,
                    self.ui.JBOD
                ]:
                    i.setChecked(False)

                if resp1 == b"LOW" and resp2 == b"LOW":
                    self.ui.JBOD.setChecked(True)
                elif resp1 == b"HIGH" and resp2 == b"LOW":
                    self.ui.R1.setChecked(True)
                elif resp1 == b"LOW" and resp2 == b"HIGH":
                    self.ui.R0.setChecked(True)
                else:
                    self.ui.PM.setChecked(True)

        except:

            pass