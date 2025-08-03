# from PySide6 import QtWidgets
# from PySide6.QtGui import QIcon
# from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QGroupBox
# from pyqttoast import Toast, ToastIcon

# from Ui_ultra_enclosure_manager import Ui_main_interface
from progressbar import ProgressWindow
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

    def on_sata_excute_clicked(self):
        self.progress_window = ProgressWindow(main_window=self.main_window)
        self.progress_window.progressbar_start()