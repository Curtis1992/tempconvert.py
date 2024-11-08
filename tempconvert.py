import sys
from PySide6.QtWidgets import (
  QApplication, QWidget, QLabel, QLineEdit, QPushButton,
  QVBoxLayout, QHBoxLayout, QMainWindow
)
from PySide6 import QtCore

class TemperatureConverterApp(QMainWindow):
  def __init__(self):
    super().__init__() 
    self.init_ui()
  
  def init_ui(self):
    self.setWindowTitle("Temperature Converter")
    self.setGeometry(100, 100, 400, 100) 
    
    self.lbl_fahrenheit = QLabel("Fahrenheit:")
    self.edit_fahrenheit = QLineEdit()
    fahrenheit_layout = QVBoxLayout()
    fahrenheit_layout.addWidget(self.lbl_fahrenheit)
    fahrenheit_layout.addWidget(self.edit_fahrenheit)
    
    self.lbl_celsius = QLabel("Celsius:")
    self.edit_celsius = QLineEdit()
    celsius_layout = QVBoxLayout()
    celsius_layout.addWidget(self.lbl_celsius)
    celsius_layout.addWidget(self.edit_celsius)
    
    self.btn_to_celsius = QPushButton("\u2192") 
    self.btn_to_celsius.setFixedWidth(50)
    self.btn_to_fahrenheit = QPushButton("\u2190") 
    self.btn_to_fahrenheit.setFixedWidth(50)
    button_layout = QVBoxLayout()
    button_layout.addWidget(self.btn_to_celsius)
    button_layout.addWidget(self.btn_to_fahrenheit)
    
    
    self.error_label = QLabel("")
    self.error_label.setStyleSheet("color: red")
    
    top_layout = QHBoxLayout()
    top_layout.addLayout(fahrenheit_layout)
    top_layout.addLayout(button_layout)
    top_layout.addLayout(celsius_layout)
    
    main_layout = QVBoxLayout()
    main_layout.addLayout(top_layout)
    main_layout.addWidget(self.error_label, alignment=QtCore.Qt.AlignCenter)
    main_widget = QWidget()
    main_widget.setLayout(main_layout)
    self.setCentralWidget(main_widget)
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  converter_app = TemperatureConverterApp()
  converter_app.show()
  sys.exit(app.exec())