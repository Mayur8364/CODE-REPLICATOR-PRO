from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
import pandas as pd
from PyQt5.QtWidgets import QComboBox
import os

class CSVWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSV Bulk Replicator")
        self.setGeometry(500, 250, 500, 400)
        self.setFixedSize(500, 400)

        # Set Background Color
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#FFF3E0"))
        self.setPalette(palette)

        layout = QVBoxLayout()

        # Title
        title = QLabel("📂 CSV Bulk Replicator")
        title.setFont(QFont('Arial', 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #E65100; margin-bottom: 30px;")
        layout.addWidget(title)

        # Python file
        self.file_label = QLabel("Select Python File:")
        self.file_label.setFont(QFont('Arial', 12))
        layout.addWidget(self.file_label)

        self.file_input = QLineEdit()
        layout.addWidget(self.file_input)

        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_file)
        self.browse_button.setStyleSheet(self.button_style())
        layout.addWidget(self.browse_button)

        # CSV File
        self.csv_label = QLabel("Select CSV File (Name, RollNo):")
        self.csv_label.setFont(QFont('Arial', 12))
        layout.addWidget(self.csv_label)

        self.csv_input = QLineEdit()
        layout.addWidget(self.csv_input)

        self.csv_browse_button = QPushButton("Browse CSV")
        self.csv_browse_button.clicked.connect(self.browse_csv)
        self.csv_browse_button.setStyleSheet(self.button_style())
        layout.addWidget(self.csv_browse_button)

        self.format_label = QLabel("Select Output Format:")
        self.format_label.setFont(QFont('Arial', 12))
        layout.addWidget(self.format_label)

        self.format_combo = QComboBox()
        self.format_combo.addItems(["Python (.py)", "PDF (.pdf)"])
        layout.addWidget(self.format_combo)


        # Generate
        self.generate_button = QPushButton("Generate Files")
        self.generate_button.clicked.connect(self.generate_files)
        self.generate_button.setStyleSheet(self.button_style())
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def button_style(self):
        return """
            QPushButton {
                background-color: #FB8C00;
                color: white;
                padding: 12px;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #EF6C00;
            }
        """

    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Python File", "", "Python Files (*.py)")
        if file_name:
            self.file_input.setText(file_name)

    def browse_csv(self):
        csv_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
        if csv_name:
            self.csv_input.setText(csv_name)

    def generate_files(self):
        input_file = self.file_input.text()
        csv_file = self.csv_input.text()
        selected_format = self.format_combo.currentText()

        if not input_file or not csv_file:
            QMessageBox.warning(self, "Input Error", "Please select files!")
            return

        df = pd.read_csv(csv_file)

        with open(input_file, 'r') as file:
            template = file.read()

        output_dir = os.path.dirname(input_file)

        for index, row in df.iterrows():
            name = row['Name']
            roll = str(row['RollNo'])
            content = template.replace("Ganesh Wagh", name).replace("133", roll)
            base_filename = f"{name}_{roll}"

            if selected_format == "Python (.py)":
                output_file = os.path.join(output_dir, f"{base_filename}.py")
                with open(output_file, 'w') as f:
                    f.write(content)

            elif selected_format == "PDF (.pdf)":
                from fpdf import FPDF
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                for line in content.split('\n'):
                    pdf.cell(0, 10, line, ln=True)
                output_file = os.path.join(output_dir, f"{base_filename}.pdf")
                pdf.output(output_file)

        QMessageBox.information(self, "Success", "All Files Created Successfully!")


