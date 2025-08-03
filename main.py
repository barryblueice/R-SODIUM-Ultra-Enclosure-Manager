import main_windows
from interface import MainInterfaceController
from PySide6 import QtWidgets
from qt_material import apply_stylesheet

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setQuitOnLastWindowClosed(False)
    window = main_windows.MainWindow()

    controller = MainInterfaceController(window)
    controller.ui_initialized()

    apply_stylesheet(app, theme='light_blue.xml')

    window.show()
    app.exec()
