import qt6_main_interface
from PyQt6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setQuitOnLastWindowClosed(False)
    window = qt6_main_interface.MainWindow()
    window.show()
    app.exec()
