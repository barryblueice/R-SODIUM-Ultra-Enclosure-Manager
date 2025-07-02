import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QProgressBar
from PySide6.QtCore import QTimer, Qt, QThread, Signal


# 子线程类，用于模拟耗时任务
class Worker(QThread):
    progress = Signal(int)
    finished = Signal()

    def run(self):
        for i in range(101):
            self.msleep(30)  # 模拟耗时任务
            self.progress.emit(i)
        self.finished.emit()


class ProgressWindow(QWidget):
    def __init__(self, main_window=None):
        super().__init__()

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("Progress")
        self.resize(200, 100)

        # 美化窗口背景
        self.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 10px;
        """)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)

        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        # 美化进度条样式
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: #ffffff;
                border: 2px solid #bcbcbc;
                border-radius: 5px;
            }
            QProgressBar::chunk {
                background-color: #06b025;
                width: 20px;
            }
        """)

        self.layout.addWidget(self.progress_bar)
        self.main_window = main_window
        self.worker = None

    def progressbar_start(self):
        self.progress_bar.setValue(0)
        self.show()
        self.raise_()
        self.activateWindow()

        if self.main_window:
            self.main_window.setEnabled(False)
            mw_geo = self.main_window.geometry()
            x = mw_geo.x() + (mw_geo.width() - self.width()) // 2
            y = mw_geo.y() + (mw_geo.height() - self.height()) // 2
            self.move(x, y)

        self.worker = Worker()
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.finished.connect(self.on_finished)
        self.worker.start()

    def on_finished(self):
        self.close()
        if self.main_window:
            self.main_window.setEnabled(True)
