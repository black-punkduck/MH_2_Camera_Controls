import random
from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor, QPainter

NAME = "90s Camcorder"

def draw(painter, src, w, h, intensity, log_w, log_h, pixel_ratio):
    font = painter.font()
    font.setFamily("Courier New")
    font.setBold(True)
    font.setPointSize(13)
    painter.setFont(font)
    
    if intensity % 2 == 0:
        painter.setBrush(QColor(255, 30, 30, 240))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(30, 25, 12, 12)
    
    painter.setPen(QPen(QColor(255, 255, 255, 210)))
    painter.drawText(50, 36, "REC")
    
    painter.setBrush(Qt.BrushStyle.NoBrush)
    painter.setPen(QPen(QColor(255, 255, 255, 210), 2))
    painter.drawRect(log_w - 75, 24, 35, 16) 
    painter.fillRect(log_w - 40, 29, 3, 6, QColor(255, 255, 255, 210)) 
    
    bar_count = 3 if intensity > 10 else (2 if intensity > 4 else 1)
    for i in range(bar_count):
        painter.fillRect(log_w - 71 + (i * 9), 28, 7, 8, QColor(255, 255, 255, 210))
    
    painter.drawText(30, log_h - 30, "AUTO")
    painter.drawText(30, log_h - 55, "SP")
    painter.drawText(log_w - 150, log_h - 30, "12:04:15 PM")
    painter.drawText(log_w - 150, log_h - 55, "SEP. 19 1996")
    
    painter.setPen(QPen(QColor(255, 255, 255, 45), 1, Qt.PenStyle.SolidLine))
    for _ in range(int(intensity * 1.5)):
        noise_y = random.randint(0, log_h)
        painter.drawLine(0, noise_y, log_w, noise_y)
        
    painter.setPen(QPen(QColor(255, 255, 255, 140), 2, Qt.PenStyle.DashLine))
    for _ in range(max(1, int(intensity / 8))):
        thick_y = random.randint(0, log_h)
        for offset in range(-4, 5, 2):
            painter.drawLine(random.randint(10, 50), thick_y + offset, log_w - random.randint(10, 50), thick_y + offset)
