from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox
import os

class CustomWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Replicator")
        self.setGeometry(500, 250, 500, 400)
        self.setFixedSize(500, 400)

        # Set Background Color
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#F1F8E9"))
        self.setPalette(palette)

        layout = QVBoxLayout()

        # Labels and Inputs
        title = QLabel("🎯 Custom Replicator")
        title.setFont(QFont('Arial', 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #33691E; margin-bottom: 30px;")
        layout.addWidget(title)

        self.file_label = QLabel("Select Python File:")
        self.file_label.setFont(QFont('Arial', 12))
        layout.addWidget(self.file_label)

        self.file_input = QLineEdit()
        layout.addWidget(self.file_input)

        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_file)
        self.browse_button.setStyleSheet(self.button_style())
        layout.addWidget(self.browse_button)

        self.name_label = QLabel("Enter New Name:")
        self.name_label.setFont(QFont('Arial', 12))
        layout.addWidget(self.name_label)

        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        self.roll_label = QLabel("Enter New Roll Number:")
        self.roll_label.setFont(QFont('Arial', 12))
        layout.addWidget(self.roll_label)

        self.roll_input = QLineEdit()
        layout.addWidget(self.roll_input)

        self.format_label = QLabel("Select Output Format:")
        self.format_label.setFont(QFont('Arial', 12))
        layout.addWidget(self.format_label)

        self.format_combo = QComboBox()
        self.format_combo.addItems(["Python (.py)", "PDF (.pdf)"])
        layout.addWidget(self.format_combo)


        self.generate_button = QPushButton("Generate New File")
        self.generate_button.clicked.connect(self.generate_file)
        self.generate_button.setStyleSheet(self.button_style())
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def button_style(self):
        return """
            QPushButton {
                background-color: #689F38;
                color: white;
                padding: 12px;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #558B2F;
            }
        """

    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Python File", "", "Python Files (*.py)")
        if file_name:
            self.file_input.setText(file_name)

    def generate_file(self):
        input_file = self.file_input.text()
        new_name = self.name_input.text()
        new_roll = self.roll_input.text()
        selected_format = self.format_combo.currentText()

        if not input_file or not new_name or not new_roll:
            QMessageBox.warning(self, "Input Error", "Please fill all fields!")
            return

        with open(input_file, 'r') as file:
            content = file.read()

        # Replace Name and Roll
        content = content.replace("Ganesh Wagh", new_name)
        content = content.replace("133", new_roll)

        output_dir = os.path.dirname(input_file)
        base_filename = f"{new_name}_{new_roll}"

        if selected_format == "Python (.py)":
            output_file = os.path.join(output_dir, f"{base_filename}.py")
            with open(output_file, 'w') as file:
                file.write(content)

        elif selected_format == "PDF (.pdf)":
            from fpdf import FPDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in content.split('\n'):
                pdf.cell(0, 10, line, ln=True)
            output_file = os.path.join(output_dir, f"{base_filename}.pdf")
            pdf.output(output_file)

        
        QMessageBox.information(self, "Success", f"File Created Successfully!\nSaved as: {output_file}")
