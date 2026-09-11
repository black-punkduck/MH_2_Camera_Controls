import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor

NAME = "Chromatic Aberration"

def draw(painter, src, w, h, intensity, log_w, log_h, pixel_ratio):
    painter.fillRect(0, 0, w, h, QColor(0, 0, 0, 255))

    cyan_img = src.copy()
    cyan_arr = np.frombuffer(cyan_img.bits(), dtype=np.uint8).reshape((h, w, 4))
    cyan_arr[:, :, 2] = 0  
    
    red_img = src.copy()
    red_arr = np.frombuffer(red_img.bits(), dtype=np.uint8).reshape((h, w, 4))
    red_arr[:, :, 0] = 0  
    red_arr[:, :, 1] = 0  

    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
    painter.drawImage(intensity, 0, cyan_img)
    
    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Plus)
    painter.drawImage(-intensity, 0, red_img)
