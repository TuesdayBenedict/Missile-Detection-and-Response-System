# theme_loader.py
from PyQt6.QtWidgets import QApplication

def load_theme(app: QApplication, theme_path: str):
    with open(theme_path, "r") as file:
        app.setStyleSheet(file.read())
