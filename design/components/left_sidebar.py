# left_sidebar.py
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QListWidgetItem,
)
from PyQt6.QtCore import Qt, pyqtSignal


class LeftSidebar(QWidget):
    # Signal to communicate with the main window
    item_selected = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setFixedWidth(300)  # Fixed width for the sidebar
        self.setStyleSheet("background-color: #2E2E2E; color: white;")

        # Main layout for the sidebar
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(5)

        # Military Hierarchy section
        self.military_title = QLabel("Military Hierarchy")
        self.military_title.setStyleSheet("font-weight: bold; padding: 5px;")
        self.military_title.mousePressEvent = lambda event: self.toggle_section(
            self.military_list
        )

        self.military_list = QListWidget()
        self.military_list.addItems(["General", "Colonel", "Major", "Captain"])
        # self.military_list.itemClicked.connect(self.display_item)

        # Weapons Information section
        self.weapons_title = QLabel("Weapon Information")
        self.weapons_title.setStyleSheet("font-weight: bold; padding: 5px;")
        self.weapons_title.mousePressEvent = lambda event: self.toggle_section(
            self.weapons_list
        )

        self.weapons_list = QListWidget()
        self.weapons_list.addItems(["Missiles", "Rockets", "Guns", "Artillery"])
        # self.weapons_list.itemClicked.connect(self.display_item)

        # Add sections to the main layout
        self.layout.addWidget(self.military_title)
        self.layout.addWidget(self.military_list)
        self.layout.addWidget(self.weapons_title)
        self.layout.addWidget(self.weapons_list)

        # Initially, both lists are visible
