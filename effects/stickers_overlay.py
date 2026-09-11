import sys
import random
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QColor, QPen, QPolygon

# FIX: Match the exact name lookup from the filename layout
NAME = "stickers_overlay"

def draw(painter, src, w, h, intensity, log_w, log_h, pixel_ratio):
    painter.setPen(Qt.NoPen)
    font = painter.font()
    font.setFamily("Impact" if sys.platform == "win32" else "Helvetica")
    font.setBold(True)
    
    # ==========================================
    # STICKER 1: Top-Left Neon "HELLO" Name Tag
    # ==========================================
    painter.setBrush(QColor(255, 92, 0, 255))
    painter.drawRoundedRect(25, 25, 110, 75, 8, 8) 
    painter.setBrush(QColor(255, 255, 255, 255))
    painter.drawRect(25, 48, 110, 36)
    
    font.setPointSize(9)
    painter.setFont(font)
    painter.setPen(QColor(255, 255, 255))
    painter.drawText(42, 40, "HELLO")
    
    font.setPointSize(11)
    painter.setFont(font)
    painter.setPen(QColor(0, 0, 0))
    painter.drawText(38, 72, "MH2_Creator")
    
    # ==========================================
    # STICKER 2: Bottom-Left Industrial Barcode
    # ==========================================
    painter.setPen(Qt.NoPen)
    painter.setBrush(QColor(245, 245, 240, 245))
    painter.drawRect(30, log_h - 85, 130, 55)
    
    painter.setBrush(QColor(20, 20, 20, 240))
    bx = 40
    while bx < 150:
        # FIX: Put the original numbers back inside the choice brackets
        line_w = random.choice([2, 4, 6])
        painter.drawRect(bx, log_h - 75, line_w, 30)
        bx += line_w + random.choice([2, 4])
        
    font.setFamily("Courier New")
    font.setPointSize(7)
    painter.setFont(font)
    painter.setPen(QColor(40, 40, 40))
    painter.drawText(50, log_h - 36, "*VER 2.0*")

    # ==========================================
    # STICKER 3: Top-Right Danger Warning Triangle
    # ==========================================
    painter.setBrush(QColor(255, 180, 0, 235))
    tx, ty = log_w - 120, 30
    triangle = QPolygon([QPoint(tx + 45, ty), QPoint(tx, ty + 70), QPoint(tx + 90, ty + 70)])
    painter.drawPolygon(triangle)
    
    painter.setBrush(QColor(15, 15, 15, 255))
    painter.drawRect(tx + 42, ty + 25, 6, 25)
    painter.drawEllipse(tx + 42, ty + 56, 6, 6)

    # ==========================================
    # STICKER 4: Bottom-Right Round Pass Stamp
    # ==========================================
    painter.setPen(QPen(QColor(0, 180, 210, 230), 3, Qt.PenStyle.DashLine))
    painter.setBrush(QColor(20, 40, 50, 220))
    cx, cy = log_w - 95, log_h - 95
    painter.drawEllipse(cx, cy, 70, 70)
    
    painter.setPen(Qt.NoPen)
    painter.setBrush(QColor(0, 210, 255, 240))
    painter.drawEllipse(cx + 8, cy + 8, 54, 54)
    
    font.setFamily("Arial")
    font.setPointSize(9)
    font.setBold(True)
    painter.setFont(font)
    painter.setPen(QColor(255, 255, 255))
    painter.drawText(cx + 11, cy + 40, "PASSED")
    painter.setBrush(Qt.NoBrush)
