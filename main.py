from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QMessageBox,
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys


class PositionSizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Futures Position Sizer")
        self.setFixedSize(300, 420)
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #ffffff;
                font-family: 'Segoe UI';
            }
            QLabel {
                font-size: 14px;
            }
            QLineEdit {
                background-color: #1e1e1e;
                border: 1px solid #333;
                border-radius: 6px;
                padding: 6px;
                color: white;
            }
            QPushButton {
                background-color: #2d2d2d;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
                font-size: 14px;
                color: white;
            }
            QPushButton:hover {
                background-color: #444444;
            }
            QPushButton:pressed {
                background-color: #222222;
            }
            QComboBox {
                background-color: #1e1e1e;
                border: 1px solid #333;
                border-radius: 6px;
                padding: 6px;
                color: white;
            }
            QComboBox QAbstractItemView {
                background-color: #1e1e1e;
                color: white;
                selection-background-color: #333;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Title
        title = QLabel("FUTURES POSITION SIZER")
        title.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Dropdown for Symbols
        self.symbol_dropdown = QComboBox()
        self.symbol_dropdown.addItems(["NQ", "MNQ", "ES", "MES", "GC", "MGC"])
        self.symbol_dropdown.currentTextChanged.connect(self.update_point_value)
        layout.addWidget(QLabel("Select Symbol:"))
        layout.addWidget(self.symbol_dropdown)

        # Inputs
        self.entry_sl = self.make_input(layout, "Stop Loss (points):", "50")
        self.entry_risk = self.make_input(layout, "Risk ($):", "500")
        self.entry_point_value = self.make_input(layout, "Point Value ($):", "2.00")
        self.entry_point_value.setReadOnly(True)

        # Button
        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self.calculate_position_size)
        layout.addWidget(calc_btn)

        # Result
        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Initialize default point value for first selection
        self.update_point_value(self.symbol_dropdown.currentText())

    def make_input(self, layout, label_text, default):
        layout.addWidget(QLabel(label_text))
        entry = QLineEdit()
        entry.setText(default)
        layout.addWidget(entry)
        return entry

    def update_point_value(self, symbol):
        point_values = {
            "NQ": 20,
            "MNQ": 2,
            "ES": 50,
            "MES": 5,
            "GC": 100,
            "MGC": 10,
        }
        if symbol in point_values:
            self.entry_point_value.setText(str(point_values[symbol]))

    def calculate_position_size(self):
        try:
            stop_loss = float(self.entry_sl.text())
            risk_amount = float(self.entry_risk.text())
            point_value = float(self.entry_point_value.text())

            if stop_loss <= 0 or risk_amount <= 0 or point_value <= 0:
                raise ValueError

            contracts = risk_amount / (stop_loss * point_value)
            symbol = self.symbol_dropdown.currentText()
            self.result_label.setText(f"{contracts:.2f} {symbol} Contracts")

        except ValueError:
            QMessageBox.critical(self, "Input Error", "❌ Please enter valid numbers.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PositionSizer()
    window.show()
    sys.exit(app.exec())
