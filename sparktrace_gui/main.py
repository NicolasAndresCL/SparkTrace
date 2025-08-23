from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget
from sparktrace_gui.views.csv_loader_view import CsvLoaderView
from sparktrace_gui.views.dashboard_view import DashboardView
from sparktrace_gui.views.command_runner_view import CommandRunnerView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SparkTrace GUI")
        self.setMinimumSize(1000, 700)

        tabs = QTabWidget()
        tabs.addTab(CsvLoaderView(), "📂 CSV Loader")
        tabs.addTab(DashboardView(), "📊 Dashboard")
        tabs.addTab(CommandRunnerView(), "⚙️ Commands")

        self.setCentralWidget(tabs)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
