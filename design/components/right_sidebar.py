# right_sidebar.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget


class RightSidebar(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Radar Information
        self.info_label = QLabel("Radar Information")
        self.info_list = QListWidget()

        layout.addWidget(self.info_label)
        layout.addWidget(self.info_list)
