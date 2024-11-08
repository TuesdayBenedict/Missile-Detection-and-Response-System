# middle_display.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class MiddleDisplay(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        
        # Radar display
        self.radar_display = QLabel("Radar Scanning Animation")
        
        # Sensor Data Display
        self.sensor_display = QLabel("Sensor Data & Graphs")
        
        layout.addWidget(self.radar_display)
        layout.addWidget(self.sensor_display)
