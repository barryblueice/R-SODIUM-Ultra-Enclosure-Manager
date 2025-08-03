from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QGroupBox
from pyqttoast import Toast, ToastIcon

from Ui_ultra_enclosure_manager import Ui_main_interface
from progressbar import ProgressWindow
import usm_rc

import usb_module
import groupboxcontroller

# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)

# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_main_interface()
#         self.ui.setupUi(self)
#         self.setFixedSize(self.width(), self.height())
#         self.ui_state(False)

#         self.monitor_thread = usb_module.USBCommunicatorThread()
#         self.monitor_thread.device_event.connect(self.on_device_status_changed)
#         self.monitor_thread.start()

#         self.groupbox_list = []
#         self.groupbox_list.append(self.ui.overview)
#         self.groupbox_list.append(self.ui.sataconfig)
#         self.groupbox_list.append(self.ui.boxmode)
#         self.groupbox_list.append(self.ui.about)
#         self.controller = groupboxcontroller.GroupVisibilityController()
#         self.controller.switch_signal.connect(self.show_only_one)
#         self.controller.set_all_widgets(self.groupbox_list)

#         self.ui.sataconfig.setVisible(False)
#         self.ui.boxmode.setVisible(False)
#         self.ui.about.setVisible(False)

#         self.tray_icon = QSystemTrayIcon(QIcon("icon.ico"), self)
#         self.tray_icon.setToolTip("R-SODIUM Ultra Enclosure Manager")

#         self.ui.overview_button.clicked.connect(lambda: self.controller.activate_only(self.ui.overview))
#         self.ui.SATA_Interface_button.clicked.connect(lambda:self.controller.activate_only(self.ui.sataconfig))
#         self.ui.boxmode_button.clicked.connect(lambda: self.controller.activate_only(self.ui.boxmode))
#         self.ui.about_button.clicked.connect(lambda: self.controller.activate_only(self.ui.about))
#         self.ui.boxmode_execute.clicked.connect(self.on_boxmode_execute_clicked)
#         self.ui.sata_execute.clicked.connect(self.on_sata_excute_clicked)

#         tray_menu = QMenu()
#         show_action = tray_menu.addAction("Show")
#         quit_action = tray_menu.addAction("Exit")

#         show_action.triggered.connect(self.show)
#         quit_action.triggered.connect(QtWidgets.QApplication.quit)

#         self.tray_icon.setContextMenu(tray_menu)
#         self.tray_icon.show()

#         self.tray_icon.activated.connect(self.on_tray_icon_activated)

#     def on_tray_icon_activated(self, reason):
#         if reason == QSystemTrayIcon.ActivationReason.Trigger:
#             self.show()
#             self.activateWindow()

#     def ui_state(self,status: bool):
#         self.ui.boxmode.setEnabled(status)
#         self.ui.sataconfig.setEnabled(status)
#         self.ui.SATA_Interface_button.setEnabled(status)
#         self.ui.boxmode_button.setEnabled(status)

#     def handle_visibility_change(self, widget: QGroupBox, visible):
#         widget.setVisible(visible)

#     def show_only_one(self, target_widget):
#         gb: QGroupBox
#         for gb in self.groupbox_list:
#             gb.setVisible(gb == target_widget)

#     def on_device_status_changed(self, status: bool):
#         toast = Toast(self)
#         toast.setAlwaysOnMainScreen(True)
#         self.ui_state(status=status)
#         if status:
#             toast.setText('A new Ultra SSD Enclosure device has detected!')
#             toast.setIcon(ToastIcon.SUCCESS)
#         else:
#             toast.setText('The Ultra SSD Enclosure device has been removed!')
#             toast.setIcon(ToastIcon.INFORMATION)
#         toast.setIconColor(None)
#         toast.setShowIcon(True)
#         toast.setShowDurationBar(False)
#         toast.setDuration(3000)
#         toast.show()

#     def closeEvent(self, event):
#         toast = Toast(self)
#         toast.setAlwaysOnMainScreen(True)
#         toast.setText('The program has minimized to tray.')
#         toast.setIcon(ToastIcon.INFORMATION)
#         toast.setIconColor(None)
#         toast.setShowIcon(True)
#         toast.setShowDurationBar(False)
#         toast.setDuration(3000)
#         toast.show()

#     def on_boxmode_execute_clicked(self):
#         for i in [
#             self.ui.combinemode,
#             self.ui.hubonly,
#             self.ui.sataonly,
#             self.ui.nvmeonly
#         ]:
#             if i.isChecked():
#                 print(i.text())
#                 break
#         self.progress_window = ProgressWindow(main_window=self)
#         self.progress_window.progressbar_start()

#     def on_sata_excute_clicked(self):
#         self.progress_window = ProgressWindow(main_window=self)
#         self.progress_window.progressbar_start()

from main_windows import MainWindow

class MainInterfaceController:
    def __init__(self, main_window: MainWindow):
        self.main_window = main_window

    def ui_initialized(self):
        ui = self.main_window.ui
        controller = self.main_window.controller

        ui.overview_button.clicked.connect(lambda: controller.activate_only(ui.overview))
        ui.SATA_Interface_button.clicked.connect(lambda: controller.activate_only(ui.sataconfig))
        ui.boxmode_button.clicked.connect(lambda: controller.activate_only(ui.boxmode))
        ui.about_button.clicked.connect(lambda: controller.activate_only(ui.about))

        ui.boxmode_execute.clicked.connect(self.on_boxmode_execute_clicked)
        ui.sata_execute.clicked.connect(self.on_sata_excute_clicked)

    def on_boxmode_execute_clicked(self):
        for i in [
            self.main_window.ui.combinemode,
            self.main_window.ui.hubonly,
            self.main_window.ui.sataonly,
            self.main_window.ui.nvmeonly
        ]:
            if i.isChecked():
                print(i.text())
                break
        self.progress_window = ProgressWindow(main_window=self.main_window)
        self.progress_window.progressbar_start()

    def on_sata_excute_clicked(self):
        self.progress_window = ProgressWindow(main_window=self.main_window)
        self.progress_window.progressbar_start()