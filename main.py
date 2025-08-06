import sys
import instance_check
import main_windows
from interface import MainInterfaceController
from PySide6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    instance_check.check_single_instance_and_handle()

    app.setQuitOnLastWindowClosed(False)
    window = main_windows.MainWindow()

    controller = MainInterfaceController(window)
    controller.ui_initialized()

    window.show()
    app.exec()
