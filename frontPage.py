from PySide6.QtWidgets import QMainWindow, QMenu, QLabel, QVBoxLayout
from PySide6.QtGui import QAction
from user_interface import Ui_MainWindow
from timeline import TimeLine
class MyToDoList(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ToDo List App")
        
        time_line = TimeLine()
        self.task_scrollArea.setWidget(time_line)
        