from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from Ui_ultra_enclosure_manager import Ui_main_interface
from PySide6.QtWidgets import QSystemTrayIcon, QGroupBox
from pyqttoast import Toast, ToastIcon

import usb_module
import groupboxcontroller

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

    def ui_state(self,status: bool):
        self.ui.boxmode.setEnabled(status)
        self.ui.sataconfig.setEnabled(status)
        self.ui.SATA_Interface_button.setEnabled(status)
        self.ui.boxmode_button.setEnabled(status)

    def on_device_status_changed(self, status: bool):
        toast = Toast(self)
        toast.setAlwaysOnMainScreen(True)
        self.ui_state(status=status)
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

        self.ui.nvme_status.setText("True")
        self.ui.nvme_status.setStyleSheet("color: #00FF00;")

    def show_only_one(self, target_widget):
        gb: QGroupBox
        for gb in self.groupbox_list:
            gb.setVisible(gb == target_widget)