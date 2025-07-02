from PySide6.QtCore import QObject
from PySide6.QtCore import Signal as pyqtSignal
from PySide6.QtWidgets import QGroupBox

class GroupVisibilityController(QObject):
    switch_signal = pyqtSignal(object)

    def __init__(self, all_widgets=None):
        super().__init__()
        self.all_widgets = all_widgets or []

    def set_all_widgets(self, widgets):
        self.all_widgets = widgets

    def activate_only(self, target_widget: QGroupBox):
        self.switch_signal.emit(target_widget)
