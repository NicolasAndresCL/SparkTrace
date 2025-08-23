from PySide6.QtWidgets import QFileDialog

def open_csv_dialog(parent=None) -> str:
    """
    Opens a file dialog to select a CSV file.
    Returns the selected file path or an empty string.
    """
    file_path, _ = QFileDialog.getOpenFileName(
        parent,
        "Select CSV File",
        "",
        "CSV Files (*.csv);;All Files (*)"
    )
    return file_path

def save_markdown_dialog(parent=None, default_name="export.md") -> str:
    """
    Opens a file dialog to save a Markdown file.
    Returns the selected file path or an empty string.
    """
    file_path, _ = QFileDialog.getSaveFileName(
        parent,
        "Save Markdown File",
        default_name,
        "Markdown Files (*.md);;All Files (*)"
    )
    return file_path

def save_png_dialog(parent=None, default_name="chart.png") -> str:
    """
    Opens a file dialog to save a PNG image.
    Returns the selected file path or an empty string.
    """
    file_path, _ = QFileDialog.getSaveFileName(
        parent,
        "Save PNG Image",
        default_name,
        "PNG Files (*.png);;All Files (*)"
    )
    return file_path
