from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QFileDialog,
    QTableView, QMessageBox
)
from PySide6.QtGui import QStandardItemModel, QStandardItem
import pandas as pd
from datetime import datetime
import os
from sparktrace_gui.utils.file_dialogs import open_csv_dialog

REQUIRED_COLUMNS = {"nombre","imagen", "precio", "stock"}

class CsvLoaderView(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

        # Botón para cargar CSV
        self.load_button = QPushButton("📂 Load CSV")
        self.load_button.clicked.connect(self.load_csv)
        self.layout().addWidget(self.load_button)

        # Tabla para mostrar datos
        self.table_view = QTableView()
        self.layout().addWidget(self.table_view)

        # Botón para exportar a Markdown
        self.export_button = QPushButton("📝 Export to Markdown")
        self.export_button.clicked.connect(self.export_to_markdown)
        self.layout().addWidget(self.export_button)

        self.last_dataframe = None

    def load_csv(self):
        file_path = open_csv_dialog(self)
        if not file_path:
            return

        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load CSV:\n{str(e)}")
            return

        if not self.validate_structure(df):
            return

        self.last_dataframe = df
        self.display_dataframe(df)

    def validate_structure(self, df: pd.DataFrame) -> bool:
        missing = REQUIRED_COLUMNS - set(df.columns)
        if missing:
            QMessageBox.warning(
                self, "Invalid CSV",
                f"Missing columns: {', '.join(missing)}"
            )
            return False
        return True

    def display_dataframe(self, df: pd.DataFrame):
        model = QStandardItemModel()
        model.setColumnCount(len(df.columns))
        model.setHorizontalHeaderLabels(df.columns.tolist())

        for row in df.itertuples(index=False):
            items = [QStandardItem(str(cell)) for cell in row]
            model.appendRow(items)

        self.table_view.setModel(model)

    def export_to_markdown(self):
        if self.last_dataframe is None:
            QMessageBox.information(self, "No Data", "Please load a CSV first.")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"exports/csv_export_{timestamp}.md"
        os.makedirs("exports", exist_ok=True)

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("# CSV Export\n\n")
                f.write(self.last_dataframe.to_markdown(index=False))
            QMessageBox.information(self, "Exported", f"Markdown saved to:\n{filename}")
        except Exception as e:
            QMessageBox.critical(self, "Export Error", f"Failed to export:\n{str(e)}")
