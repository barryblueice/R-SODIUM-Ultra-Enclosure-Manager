import sys
import os
import win32process
import win32api
import signal
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010

PROCESS_NAME = "R-SODIUM-Ultra-SSD-Enclosure-Manager.exe".lower()

def enum_process_names():
    pids = win32process.EnumProcesses()
    names = []
    for pid in pids:
        try:
            hProcess = win32api.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
            exe_name = win32process.GetModuleFileNameEx(hProcess, 0)
            names.append((pid, exe_name))
            win32api.CloseHandle(hProcess)
        except Exception:
            pass
    return names

def history_instance_running():
    current_pid = win32api.GetCurrentProcessId()
    for pid, exe_path in enum_process_names():
        if exe_path.lower().endswith(PROCESS_NAME) and pid != current_pid:
            return pid
    return None

def kill_process(pid):
    try:
        os.kill(pid, signal.SIGTERM)
    except Exception as e:
        pass

def check_single_instance_and_handle(parent=None):
    pid = history_instance_running()
    if pid:
        msg_box = QMessageBox(parent)
        msg_box.setWindowTitle("Application Already Running")
        msg_box.setText("The application is already running.\nDo you want to terminate the existing instance and start a new one?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        msg_box.setWindowIcon(QIcon("icon.ico"))
        reply = msg_box.exec()
        if reply == QMessageBox.Yes:
            kill_process(pid)
            return True
        else:
            sys.exit(0)
    return True
