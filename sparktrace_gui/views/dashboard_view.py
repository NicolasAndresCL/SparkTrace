from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import os
from datetime import datetime
from sparktrace_gui.utils.file_dialogs import save_png_dialog


class DashboardView(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

        # Botón para generar gráfico
        self.plot_button = QPushButton("📊 Generate Dashboard")
        self.plot_button.clicked.connect(self.generate_plot)
        self.layout().addWidget(self.plot_button)

        # Botón para exportar gráfico
        self.export_button = QPushButton("📥 Export Chart as PNG")
        self.export_button.clicked.connect(self.export_chart)
        self.layout().addWidget(self.export_button)

        # Canvas para mostrar gráfico
        self.canvas = FigureCanvas(Figure(figsize=(8, 5)))
        self.layout().addWidget(self.canvas)

    def export_chart(self):
        filename = save_png_dialog(self, default_name="chart.png")
        if not filename:
            return

        try:
            self.canvas.figure.savefig(filename)
            QMessageBox.information(self, "Exported", f"Chart saved to:\n{filename}")
        except Exception as e:
            QMessageBox.critical(self, "Export Error", f"Failed to save chart:\n{str(e)}")


    def generate_plot(self):
        # Buscar el último CSV exportado por CsvLoaderView
        try:
            latest_file = self.get_latest_csv_export()
            df = pd.read_csv(latest_file)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data:\n{str(e)}")
            return

        # Validar columnas necesarias
        if not {"nombre", "imagen", "precio", "stock"}.issubset(df.columns):
            QMessageBox.warning(self, "Invalid Data", "Required columns missing: nombre, imagen, precio, stock")
            return

        # Generar gráfico de barras: nombre vs stock
        ax = self.canvas.figure.subplots()
        ax.clear()
        ax.bar(df["nombre"], df["stock"], color="skyblue")
        ax.set_title("Stock por producto")
        ax.set_xlabel("Producto")
        ax.set_ylabel("Cantidad en stock")
        ax.tick_params(axis='x', rotation=45)
        self.canvas.draw()

    def get_latest_csv_export(self):
        export_dir = "exports"
        files = [f for f in os.listdir(export_dir) if f.endswith(".csv")]
        if not files:
            raise FileNotFoundError("No CSV exports found.")
        files.sort(key=lambda f: os.path.getmtime(os.path.join(export_dir, f)), reverse=True)
        return os.path.join(export_dir, files[0])
