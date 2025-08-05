from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from Ui_ultra_enclosure_manager import Ui_main_interface
from PySide6.QtWidgets import QSystemTrayIcon, QGroupBox, QMenu
from pyqttoast import Toast, ToastIcon

import usb_module
import groupboxcontroller

device = usb_module.USBCommunicatorThread.dev

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main_interface()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui_state(False)

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
        if status:
            toast.setText('A new Ultra SSD Enclosure device has detected!')
            toast.setIcon(ToastIcon.SUCCESS)
        else:
            toast.setText('The Ultra SSD Enclosure device has been removed!')
            toast.setIcon(ToastIcon.INFORMATION)
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
            
        if status:

            resp = usb_module.USBCommunicatorThread.hid_comm(
                device, 
                target=0x22, 
                nvs_status=0x00, 
                cmd=0x03)
            
            if resp == b'HIGH':

                self.ui.sata1_status.setText("True")
                self.ui.sata1_status.setStyleSheet("color: #06B025;")

            else:

                self.ui.sata1_status.setText("False")
                self.ui.sata1_status.setStyleSheet("color: #FF0000;")

            resp = usb_module.USBCommunicatorThread.hid_comm(
                device, 
                target=0x26, 
                nvs_status=0x00, 
                cmd=0x03)
            
            if resp == b'HIGH':

                self.ui.sata2_status.setText("True")
                self.ui.sata2_status.setStyleSheet("color: #06B025;")

            else:

                self.ui.sata2_status.setText("False")
                self.ui.sata2_status.setStyleSheet("color: #FF0000;")

            resp = usb_module.USBCommunicatorThread.hid_comm(
                device, 
                target=0x23, 
                nvs_status=0x00, 
                cmd=0x03)
            
            if resp == b'HIGH':

                self.ui.nvme_status.setText("True")
                self.ui.nvme_status.setStyleSheet("color: #06B025;")

            else:

                self.ui.nvme_status.setText("False")
                self.ui.nvme_status.setStyleSheet("color: #FF0000;")

            resp = usb_module.USBCommunicatorThread.hid_comm(
                device, 
                target=0x01, 
                nvs_status=0x00, 
                cmd=0x03)
            
            if resp == b'HIGH':

                self.ui.ext_power_status.setText("True")
                self.ui.ext_power_status.setStyleSheet("color: #06B025;")

            else:

                self.ui.ext_power_status.setText("False")
                self.ui.ext_power_status.setStyleSheet("color: #FF0000;")

        else:

            self.ui.nvme_status.setText("None")
            self.ui.nvme_status.setStyleSheet("color: #000000;")
            self.ui.sata1_status.setText("None")
            self.ui.sata1_status.setStyleSheet("color: #000000;")
            self.ui.sata2_status.setText("None")
            self.ui.sata2_status.setStyleSheet("color: #000000;")
            self.ui.ext_power_status.setText("None")
            self.ui.ext_power_status.setStyleSheet("color: #000000;")