from PyQt6.QtWidgets import QSplashScreen
from PyQt6.QtGui import QPixmap, QPainter, QFont, QColor
from PyQt6.QtCore import Qt


class SplashScreen(QSplashScreen):
    def __init__(
        self,
        image_path,
        text,
        text_color=QColor("white"),
        bg_color=QColor("black"),
    ):
        # Create base pixmap for setting background color and size
        pixmap = QPixmap(450, 350)
        pixmap.fill(bg_color)  # Set the background color

        # Initialize the painter before the QSplashScreen
        painter = QPainter(pixmap)

        # Load and scale the image
        self.image = QPixmap(image_path).scaled(
            200,
            200,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        # Draw the image at the center horizontally and a bit down from the top
        painter.drawPixmap(
            (pixmap.width() - self.image.width()) // 2, pixmap.height() // 4, self.image
        )

        # Set font and color for the text
        painter.setFont(QFont("Arial", 12))
        painter.setPen(text_color)

        # Draw the text centered at the bottom of the splash screen
        painter.drawText(
            pixmap.rect().adjusted(0, 0, 0, -20),  # Leave a small margin at the bottom
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter,
            text,
        )

        # End the painter session before passing to QSplashScreen
        painter.end()

        # Initialize teh QSplashScreen with custom we're creating
        super().__init__(pixmap)
