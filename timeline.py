from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QSpacerItem, QSizePolicy, QSizePolicy
from PyQt6.QtCore import Qt

class TimeLine(QWidget):
    def __init__(self):
        super().__init__()
        time_line_layout = QVBoxLayout()
        
        for hour in range(1, 25):
            time_label = QLabel(f"{hour % 12 or 12}{'AM' if hour < 12 else 'PM'}")  
            time_line_layout.addWidget(time_label)
            time_label.setStyleSheet("color: black; font-family: Inter; font-size: 10")
            
            line = QFrame()
            line.setFrameShape(QFrame.Shape.HLine)
            line.setFrameShadow(QFrame.Shadow.Sunken)
            line.setStyleSheet("color: #E4D8CE; background-color: #E4D8CE;") 
            line.setFixedHeight(3) 
            time_line_layout.addWidget(line)
            time_line_layout.addSpacing(20)
            
        self.setLayout(time_line_layout)
        
    