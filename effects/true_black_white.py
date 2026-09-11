from PySide6.QtGui import QImage, QPainter

NAME = "True Black and White"

def draw(painter, src, w, h, intensity, log_w, log_h, pixel_ratio):
    # 1. Force convert the screenshot viewport data to an 8-bit grayscale format
    grayscale_img = src.convertToFormat(QImage.Format.Format_Grayscale8)
    
    # 2. Re-assign to a full 32-bit ARGB space layout profile so the active QPainter surface can compile it
    monochrome_img = grayscale_img.convertToFormat(QImage.Format.Format_ARGB32)
    
    # 3. Overwrite the viewport target buffer with the desaturated image array
    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
    painter.drawImage(0, 0, monochrome_img)
