from PySide6.QtWidgets import QApplication
from frontPage import MyToDoList
import sys

app = QApplication(sys.argv)
window = MyToDoList()
window.show()
app.exec()