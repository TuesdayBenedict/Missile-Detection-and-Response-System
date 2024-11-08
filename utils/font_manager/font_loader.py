# font_loader.py
from PyQt6.QtGui import QFontDatabase

def load_custom_fonts():
    QFontDatabase.addApplicationFont("assets/fonts/Roboto-Regular.ttf")
