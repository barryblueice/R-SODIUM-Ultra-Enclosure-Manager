# from PySide6 import QtWidgets
# from PySide6.QtGui import QIcon
# from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QGroupBox
# from pyqttoast import Toast, ToastIcon

# from Ui_ultra_enclosure_manager import Ui_main_interface
from main_windows import MainWindow

from enclosure_mode_handle import on_boxmode_execute_clicked

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

        ui.boxmode_execute.clicked.connect(lambda: on_boxmode_execute_clicked(self.main_window))
        ui.sata_execute.clicked.connect(self.on_sata_excute_clicked)
        
        ui.combinemode.clicked.connect(self.enclosure_mode_group_changed)
        ui.nvmeonly.clicked.connect(self.enclosure_mode_group_changed)
        ui.sataonly.clicked.connect(self.enclosure_mode_group_changed)
        ui.hubonly.clicked.connect(self.enclosure_mode_group_changed)

        ui.combinemode.mode_id = 0
        ui.nvmeonly.mode_id = 1
        ui.sataonly.mode_id = 2
        ui.hubonly.mode_id = 3

        ui.nvme_self_power_checkbox.mode_id = "11"
        ui.sata1_self_power_checkbox.mode_id = "12"
        ui.sata2_self_power_checkbox.mode_id = "13"

        ui.nvme_ext_power_checkbox.mode_id = "21"
        ui.sata1_ext_power_checkbox.mode_id = "22"
        ui.sata2_ext_power_checkbox.mode_id = "23"

    def enclosure_mode_group_changed(self):
        if self.main_window.ui.combinemode.isChecked():
            self.main_window.ui.selfpowered_groupbox.setEnabled(True)
            self.main_window.ui.extpowered_groupbox.setEnabled(True)
        else:
            self.main_window.ui.selfpowered_groupbox.setEnabled(False)
            self.main_window.ui.extpowered_groupbox.setEnabled(False)