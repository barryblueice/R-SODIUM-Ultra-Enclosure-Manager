from progressbar import ProgressWindow
from interface import MainWindow

def on_boxmode_execute_clicked(main_window: MainWindow):
    for i in [
        main_window.ui.combinemode,
        main_window.ui.hubonly,
        main_window.ui.sataonly,
        main_window.ui.nvmeonly
    ]:
        if i.isChecked():
            print(i.text())
            break
    main_window.progress_window = ProgressWindow(main_window=main_window)
    main_window.progress_window.progressbar_start()