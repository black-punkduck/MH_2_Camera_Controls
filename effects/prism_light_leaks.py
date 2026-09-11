from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QLinearGradient

NAME = "Prism Light Leaks"

def draw(painter, src, w, h, intensity, log_w, log_h, pixel_ratio):
    leak_grad = QLinearGradient(0, 0, int(w), int(h / 3))
    leak_grad.setColorAt(0.0, QColor(255, 50, 50, int(intensity * 4)))
    leak_grad.setColorAt(0.4, QColor(255, 200, 0, int(intensity * 2)))
    leak_grad.setColorAt(0.7, QColor(50, 255, 100, int(intensity * 3)))
    leak_grad.setColorAt(1.0, QColor(50, 100, 255, int(intensity * 4)))
    
    painter.setPen(Qt.NoPen)
    painter.setBrush(leak_grad)
    painter.drawRect(0, 0, w, h)
