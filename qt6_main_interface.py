from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu
from pyqttoast import Toast, ToastIcon

from Ui_ultra_ssdbox_manager import Ui_Dialog
import usm_rc
import usb_monitor

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui_state(False)
        self.monitor_thread = usb_monitor.DeviceMonitorThread()
        self.monitor_thread.device_event.connect(self.on_device_status_changed)
        self.monitor_thread.start()

        self.tray_icon = QSystemTrayIcon(QIcon("icon.ico"), self)
        self.tray_icon.setToolTip("Ultra SSDBox Manager")

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

    def ui_state(self,status: bool):
        self.ui.raidconfig.setEnabled(status)

        self.ui.SATA_Interface_button.setEnabled(status)
        self.ui.boxmode_button.setEnabled(status)
        # self.ui.raidconfig.setVisible(False)

    def on_device_status_changed(self, status: bool):
        toast = Toast(self)
        toast.setAlwaysOnMainScreen(True)
        self.ui_state(status=status)
        if status:
            toast.setText('A new Ultra-SSDBox device has been plugged in!')
            toast.setIcon(ToastIcon.SUCCESS)
        else:
            toast.setText('The Ultra-SSDBox device has been removed!')
            toast.setIcon(ToastIcon.INFORMATION)
        toast.setIconColor(None)
        toast.setShowIcon(True)
        toast.setShowDurationBar(False)
        toast.setDuration(3000)
        toast.show()

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
