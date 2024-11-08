import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from utils.constants.image_strings import app_logo
from design.splash_screen.splash_screen import SplashScreen
from design.main_window import MainWindow

class MissileDetectionApp:
    def __init__(self):
        # Initialize the QApplication
        self.app = QApplication(sys.argv)

        # Initialize and display the splash screen
        self.splash = SplashScreen(app_logo, "Loading...")
        self.splash.show()

        # Initialize main window and display after splash
        self.main_window = MainWindow()
        QTimer.singleShot(5000, self.show_main_window)

        self.app.exec()

    def show_main_window(self):
        self.splash.close()
        self.main_window.showMaximized()

    def run(self):
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app_instance = MissileDetectionApp()
    app_instance.run()
