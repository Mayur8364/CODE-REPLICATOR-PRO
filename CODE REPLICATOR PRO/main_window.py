from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
from custom_window import CustomWindow
from csv_window import CSVWindow
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Code Replicator Pro - Home")
        self.setGeometry(450, 200, 600, 400)
        self.setFixedSize(600, 400)

        # Set Background Color
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#E0F7FA"))
        self.setPalette(palette)

        layout = QVBoxLayout()

        # Title Label
        self.title = QLabel("✨ CODE REPLICATOR PRO ✨")
        self.title.setFont(QFont('Arial', 22, QFont.Bold))
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: #212121; margin-bottom: 40px;")

        layout.addWidget(self.title)

        # Custom Button
        self.custom_button = QPushButton("🎯 Custom Mode")
        self.custom_button.setFont(QFont('Arial', 14))
        self.custom_button.setStyleSheet("""
            QPushButton {
                background-color: #0288D1;
                color: white;
                padding: 15px;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #0277BD;
            }
        """)
        self.custom_button.clicked.connect(self.open_custom)
        layout.addWidget(self.custom_button)

        # CSV Button
        self.csv_button = QPushButton("📂 CSV Mode")
        self.csv_button.setFont(QFont('Arial', 14))
        self.csv_button.setStyleSheet("""
            QPushButton {
                background-color: #0288D1;
                color: white;
                padding: 15px;
                border-radius: 15px;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #0277BD;
            }
        """)
        self.csv_button.clicked.connect(self.open_csv)
        layout.addWidget(self.csv_button)

        self.setLayout(layout)

    def open_custom(self):
        self.custom_window = CustomWindow()
        self.custom_window.show()

    def open_csv(self):
        self.csv_window = CSVWindow()
        self.csv_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
