from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PlotWidget(QWidget):
    def __init__(self, width=8, height=5, dpi=100):
        super().__init__()
        self.setLayout(QVBoxLayout())

        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.canvas = FigureCanvas(self.figure)
        self.layout().addWidget(self.canvas)

    def plot_bar(self, x_data, y_data, title="Bar Chart", xlabel="X", ylabel="Y"):
        ax = self.figure.subplots()
        ax.clear()
        ax.bar(x_data, y_data, color="steelblue")
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.tick_params(axis='x', rotation=45)
        self.canvas.draw()

    def export_png(self, filename):
        self.figure.savefig(filename)
