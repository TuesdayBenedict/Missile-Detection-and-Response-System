from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from utils.constants.image_strings import app_logo
from design.components.left_sidebar import LeftSidebar
from design.components.middle_display import MiddleDisplay
from design.components.right_sidebar import RightSidebar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title & icon
        self.setWindowTitle("Missile Threat Detection & Response System")
        self.setWindowIcon(QIcon(app_logo))

        # Remove minimize button and maximmize the window
        self.setWindowFlags(
            Qt.WindowType.Window
            | Qt.WindowType.WindowMinimizeButtonHint
            | Qt.WindowType.WindowCloseButtonHint
        )

        # Main widget
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        # Main layout (horizontal layout to hold left sidebar, middle content and right sidebar)
        main_layout = QHBoxLayout(self.main_widget)

        # Different Layouts sections
        self.left_sidebar = LeftSidebar()
        self.middle_display = MiddleDisplay()
        self.right_sidebar = RightSidebar()

        # add sections to layout
        main_layout.addWidget(self.left_sidebar)
        main_layout.addWidget(self.middle_display)
        main_layout.addWidget(self.right_sidebar)
