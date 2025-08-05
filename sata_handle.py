from progressbar import ProgressWindow
from main_windows import MainWindow

def on_sata_execute_clicked(main_window: MainWindow):
    main_window.progress_window = ProgressWindow(main_window=main_window.main_window)
    main_window.progress_window.progressbar_start()