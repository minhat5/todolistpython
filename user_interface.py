# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(987, 489)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(140, 390, 1141, 101))
        self.widget.setStyleSheet(u"background-color: rgb(251, 247, 244);")
        self.notification_widget = QWidget(self.widget)
        self.notification_widget.setObjectName(u"notification_widget")
        self.notification_widget.setGeometry(QRect(-10, 0, 221, 91))
        self.notification_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.notification_label = QLabel(self.notification_widget)
        self.notification_label.setObjectName(u"notification_label")
        self.notification_label.setGeometry(QRect(20, 20, 191, 51))
        font = QFont()
        font.setFamilies([u"Inter Display ExtraBold"])
        font.setPointSize(12)
        font.setBold(True)
        self.notification_label.setFont(font)
        self.notification_label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.notification_label.setTextFormat(Qt.AutoText)
        self.date_widget = QWidget(self.centralwidget)
        self.date_widget.setObjectName(u"date_widget")
        self.date_widget.setGeometry(QRect(140, 70, 1141, 71))
        self.date_widget.setStyleSheet(u"background-color: rgb(251, 247, 244);")
        self.monday_label = QLabel(self.date_widget)
        self.monday_label.setObjectName(u"monday_label")
        self.monday_label.setGeometry(QRect(100, 40, 51, 21))
        self.monday_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"color: rgb(220, 205, 194);")
        self.tuesday_label = QLabel(self.date_widget)
        self.tuesday_label.setObjectName(u"tuesday_label")
        self.tuesday_label.setGeometry(QRect(190, 40, 51, 21))
        self.tuesday_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"color: rgb(220, 205, 194);")
        self.wednesday_label = QLabel(self.date_widget)
        self.wednesday_label.setObjectName(u"wednesday_label")
        self.wednesday_label.setGeometry(QRect(300, 40, 51, 21))
        self.wednesday_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"color: rgb(220, 205, 194);")
        self.thursday_label = QLabel(self.date_widget)
        self.thursday_label.setObjectName(u"thursday_label")
        self.thursday_label.setGeometry(QRect(410, 40, 51, 21))
        self.thursday_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"color: rgb(220, 205, 194);")
        self.friday_label = QLabel(self.date_widget)
        self.friday_label.setObjectName(u"friday_label")
        self.friday_label.setGeometry(QRect(530, 40, 51, 21))
        self.friday_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"Color: rgb(220, 205, 194);")
        self.saturday_label = QLabel(self.date_widget)
        self.saturday_label.setObjectName(u"saturday_label")
        self.saturday_label.setGeometry(QRect(640, 40, 51, 21))
        self.saturday_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"color: rgb(220, 205, 194);")
        self.sunday_label = QLabel(self.date_widget)
        self.sunday_label.setObjectName(u"sunday_label")
        self.sunday_label.setGeometry(QRect(740, 40, 51, 21))
        self.sunday_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"color: rgb(220, 205, 194);")
        self.first_day_label = QLabel(self.date_widget)
        self.first_day_label.setObjectName(u"first_day_label")
        self.first_day_label.setGeometry(QRect(110, 10, 31, 21))
        self.first_day_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"color: rgb(220, 205, 194);")
        self.second_day_label = QLabel(self.date_widget)
        self.second_day_label.setObjectName(u"second_day_label")
        self.second_day_label.setGeometry(QRect(200, 10, 31, 21))
        self.second_day_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"color: rgb(220, 205, 194);")
        self.third_day_label = QLabel(self.date_widget)
        self.third_day_label.setObjectName(u"third_day_label")
        self.third_day_label.setGeometry(QRect(310, 10, 51, 21))
        self.third_day_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"color: rgb(220, 205, 194);")
        self.fourth_day_label = QLabel(self.date_widget)
        self.fourth_day_label.setObjectName(u"fourth_day_label")
        self.fourth_day_label.setGeometry(QRect(420, 10, 51, 21))
        self.fourth_day_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"color: rgb(220, 205, 194);")
        self.fifth_day_label = QLabel(self.date_widget)
        self.fifth_day_label.setObjectName(u"fifth_day_label")
        self.fifth_day_label.setGeometry(QRect(530, 10, 51, 21))
        self.fifth_day_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"color: rgb(220, 205, 194);")
        self.sixth_day_label = QLabel(self.date_widget)
        self.sixth_day_label.setObjectName(u"sixth_day_label")
        self.sixth_day_label.setGeometry(QRect(640, 10, 51, 21))
        self.sixth_day_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"color: rgb(220, 205, 194);")
        self.seventh_day_label = QLabel(self.date_widget)
        self.seventh_day_label.setObjectName(u"seventh_day_label")
        self.seventh_day_label.setGeometry(QRect(750, 10, 51, 21))
        self.seventh_day_label.setStyleSheet(u"font: 75 11pt \"Inter\";\n"
"color: rgb(220, 205, 194);")
        self.action_widget = QWidget(self.centralwidget)
        self.action_widget.setObjectName(u"action_widget")
        self.action_widget.setGeometry(QRect(140, 0, 1141, 71))
        self.action_widget.setStyleSheet(u"background-color: rgb(251, 247, 244);")
        self.month_year_label = QLabel(self.action_widget)
        self.month_year_label.setObjectName(u"month_year_label")
        self.month_year_label.setGeometry(QRect(10, 20, 211, 51))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        self.month_year_label.setFont(font1)
        self.month_year_label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.todayButton = QPushButton(self.action_widget)
        self.todayButton.setObjectName(u"todayButton")
        self.todayButton.setGeometry(QRect(560, 20, 75, 23))
        font2 = QFont()
        font2.setFamilies([u"Inter ExtraBold"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.todayButton.setFont(font2)
        self.todayButton.setFocusPolicy(Qt.StrongFocus)
        self.todayButton.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 81 8pt \"Inter ExtraBold\";\n"
"    background-color: rgb(220, 205, 194);\n"
"    border: 2px solid rgb(220, 205, 194);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 180, 170); \n"
"    border: 2px solid rgb(200, 180, 170);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 160, 150); \n"
"    border: 2px solid rgb(180, 160, 150);\n"
"}")
        self.addButton = QPushButton(self.action_widget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(670, 20, 75, 23))
        font3 = QFont()
        font3.setFamilies([u"Inter Display ExtraBold"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.addButton.setFont(font3)
        self.addButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 81 8pt \"Inter Display ExtraBold\";\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(0, 0, 0);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50); \n"
"    border: 2px solid rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(80, 80, 80); \n"
"    border: 2px solid rgb(80, 80, 80);\n"
"}")
        self.task_scrollArea = QScrollArea(self.centralwidget)
        self.task_scrollArea.setObjectName(u"task_scrollArea")
        self.task_scrollArea.setGeometry(QRect(140, 140, 851, 251))
        self.task_scrollArea.setStyleSheet(u"QScrollArea#task_scrollArea {\n"
"    background-color: rgb(251, 247, 244);  \n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #7b7b7b;                 \n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}\n"
"QWidget {\n"
"    background-color: transparent;      \n"
"}")
        self.task_scrollArea.setFrameShape(QFrame.NoFrame)
        self.task_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 851, 251))
        self.task_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-1, -1, 141, 491))
        self.widget_2.setStyleSheet(u"background-color: rgb(251, 247, 244);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.notification_label.setText(QCoreApplication.translate("MainWindow", u"Today have n tasks", None))
        self.monday_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Mon</span></p></body></html>", None))
        self.tuesday_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Tue</span></p></body></html>", None))
        self.wednesday_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Wed</span></p></body></html>", None))
        self.thursday_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Thu</span></p></body></html>", None))
        self.friday_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Fri</span></p></body></html>", None))
        self.saturday_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Sat</span></p><p><br/></p></body></html>", None))
        self.sunday_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Sun</span></p><p><br/></p></body></html>", None))
        self.first_day_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">04</span></p></body></html>", None))
        self.second_day_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">05</span></p></body></html>", None))
        self.third_day_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">06</span></p><p><br/></p></body></html><?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QLabel\" name=\"monday_label_2\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>180</x>\n"
"     <y>30</y>\n"
"     <width>51</width>\n"
"     <height>21</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">font: 75 11pt &quot;Inter&quot;;</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:16pt; font-weight:600;&quot;&gt;04&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"", None))
        self.fourth_day_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">07</span></p><p><br/></p></body></html>", None))
        self.fifth_day_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">08</span></p></body></html><?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QLabel\" name=\"monday_label_2\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>180</x>\n"
"     <y>30</y>\n"
"     <width>51</width>\n"
"     <height>21</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">font: 75 11pt &quot;Inter&quot;;</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:16pt; font-weight:600;&quot;&gt;04&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"", None))
        self.sixth_day_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">09</span></p></body></html>", None))
        self.seventh_day_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">10</span></p></body></html>", None))
        self.month_year_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">November 2024</span></p></body></html>", None))
        self.todayButton.setText(QCoreApplication.translate("MainWindow", u"TODAY", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
    # retranslateUi

