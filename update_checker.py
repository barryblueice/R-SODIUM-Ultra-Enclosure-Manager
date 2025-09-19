import sys
import requests
from PySide6.QtCore import QThread, Signal

class UpdateChecker(QThread):
    update_found = Signal(str, str, str)
    no_update = Signal()

    def __init__(self, 
                current_version: str, 
                _update_type: str, 
                parent=None):
        super().__init__(parent)
        self.current_version = current_version
        self._update_type = _update_type

    def run(self):
            
        if self._update_type == "software":
            url = "https://api.github.com/repos/barryblueice/R-SODIUM-Ultra-Enclosure-Manager/releases/latest"
        else:
            url = "https://api.github.com/repos/barryblueice/R-SODIUM-Ultra-Enclosure-1.0-Firmware/releases/latest"

        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            data = resp.json()

            latest_version = data.get("tag_name", "")
            latest_url = data.get("html_url", "")

            if latest_version and latest_version != self.current_version:
                self.update_found.emit(latest_version, latest_url, self._update_type)

        except:
            pass