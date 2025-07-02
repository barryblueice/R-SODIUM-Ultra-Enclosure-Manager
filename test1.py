from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGroupBox, QLabel
import sys
from test2 import VisibilityController

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exclusive GroupBox Visibility")
        self.resize(300, 250)

        layout = QVBoxLayout(self)

        # 控制器
        self.groupbox_list = []
        self.controller = VisibilityController()
        self.controller.switch_signal.connect(self.show_only_one)

        # GroupBox 1
        self.groupbox1 = QGroupBox("GroupBox 1")
        self.groupbox1.setLayout(QVBoxLayout())
        self.groupbox1.layout().addWidget(QLabel("Content of GroupBox 1"))
        self.groupbox_list.append(self.groupbox1)

        # GroupBox 2
        self.groupbox2 = QGroupBox("GroupBox 2")
        self.groupbox2.setLayout(QVBoxLayout())
        self.groupbox2.layout().addWidget(QLabel("Content of GroupBox 2"))
        self.groupbox_list.append(self.groupbox2)

        # GroupBox 3（可扩展）
        self.groupbox3 = QGroupBox("GroupBox 3")
        self.groupbox3.setLayout(QVBoxLayout())
        self.groupbox3.layout().addWidget(QLabel("Content of GroupBox 3"))
        self.groupbox_list.append(self.groupbox3)

        # 注册所有 groupbox 给控制器
        self.controller.set_all_widgets(self.groupbox_list)

        # 按钮 1
        btn1 = QPushButton("Show GroupBox 1")
        btn1.clicked.connect(lambda: self.controller.activate_only(self.groupbox1))

        # 按钮 2
        btn2 = QPushButton("Show GroupBox 2")
        btn2.clicked.connect(lambda: self.controller.activate_only(self.groupbox2))

        # 按钮 3
        btn3 = QPushButton("Show GroupBox 3")
        btn3.clicked.connect(lambda: self.controller.activate_only(self.groupbox3))

        # 添加到布局
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(self.groupbox1)
        layout.addWidget(self.groupbox2)
        layout.addWidget(self.groupbox3)

        # 初始显示 groupbox1，其它隐藏
        self.show_only_one(self.groupbox1)

    def show_only_one(self, target_widget):
        for gb in self.groupbox_list:
            gb.setVisible(gb == target_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
