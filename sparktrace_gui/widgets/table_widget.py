from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem
import pandas as pd

class TableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        self.table_view = QTableView()
        self.layout().addWidget(self.table_view)

    def set_dataframe(self, df: pd.DataFrame):
        model = QStandardItemModel()
        model.setColumnCount(len(df.columns))
        model.setHorizontalHeaderLabels(df.columns.tolist())

        for row in df.itertuples(index=False):
            items = [QStandardItem(str(cell)) for cell in row]
            model.appendRow(items)

        self.table_view.setModel(model)
