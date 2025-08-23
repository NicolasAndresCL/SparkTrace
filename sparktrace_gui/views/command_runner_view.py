from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTextEdit, QMessageBox
)
from PySide6.QtCore import QProcess
from datetime import datetime
import os
from sparktrace_gui.utils.file_dialogs import save_markdown_dialog

class CommandRunnerView(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())

        # Botones para comandos Django
        self.cmd_buttons = {
            "📦 cargar_productos": "python manage.py cargar_productos",
            "🚀 subir_a_tiendita": "python manage.py subir_a_tiendita",
            "⚡ run_spark_job": "python manage.py run_spark_job"
        }

        # Boton exportar de forma manual Log a Markdown
        self.manual_export_button = QPushButton("📥 Export Log to Markdown")
        self.manual_export_button.clicked.connect(self.export_log)
        self.layout().addWidget(self.manual_export_button)

        for label, command in self.cmd_buttons.items():
            btn = QPushButton(label)
            btn.clicked.connect(lambda _, cmd=command: self.run_command(cmd))
            self.layout().addWidget(btn)

        # Área de texto para mostrar logs
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.layout().addWidget(self.output_area)

        # Proceso para ejecutar comandos
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.command_finished)

    def run_command(self, command: str):
        self.output_area.clear()
        self.output_area.append(f"▶ Running: {command}\n")
        self.process.start(command)

    def handle_stdout(self):
        data = self.process.readAllStandardOutput().data().decode()
        self.output_area.append(data)

    def handle_stderr(self):
        data = self.process.readAllStandardError().data().decode()
        self.output_area.append(f"[ERROR] {data}")

    def command_finished(self):
        self.output_area.append("\n✅ Command finished.")
        self.export_log()

    def export_log(self):
        filename = save_markdown_dialog(self, default_name="command_log.md")
        if not filename:
            return

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("# Command Log\n\n")
                f.write(self.output_area.toPlainText())
            self.output_area.append(f"\n📝 Log saved to: {filename}")
        except Exception as e:
            QMessageBox.critical(self, "Export Error", f"Failed to save log:\n{str(e)}")
