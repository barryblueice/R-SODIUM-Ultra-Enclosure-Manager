from PySide6.QtCore import QObject, Signal

class VisibilityController(QObject):
    # 发射目标 widget，不再需要 visible 状态
    switch_signal = Signal(object)

    def __init__(self, all_widgets=None):
        super().__init__()
        self.all_widgets = all_widgets or []

    def set_all_widgets(self, widgets):
        self.all_widgets = widgets

    def activate_only(self, target_widget):
        self.switch_signal.emit(target_widget)
