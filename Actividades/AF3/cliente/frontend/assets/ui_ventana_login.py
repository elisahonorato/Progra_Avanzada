# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_ventanalogin(object):
    def setupUi(self, ventanalogin):
        if not ventanalogin.objectName():
            ventanalogin.setObjectName(u"ventanalogin")
        ventanalogin.resize(300, 420)
        ventanalogin.setMinimumSize(QSize(300, 420))
        ventanalogin.setMaximumSize(QSize(300, 420))
        self.widget = QWidget(ventanalogin)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 300, 420))
        self.widget.setMinimumSize(QSize(300, 420))
        self.widget.setMaximumSize(QSize(300, 420))
        self.widget.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(30, 215, 97);\n"
"	border-radius:8px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(30, 215, 97);\n"
"}")
        self.fondo_img = QLabel(self.widget)
        self.fondo_img.setObjectName(u"fondo_img")
        self.fondo_img.setGeometry(QRect(0, 0, 300, 420))
        self.fondo_img.setMinimumSize(QSize(300, 420))
        self.fondo_img.setMaximumSize(QSize(300, 420))
        self.fondo_img.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:0.466, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(54, 54, 54, 255));")
        self.fondo_img.setScaledContents(True)
        self.degrade = QLabel(self.widget)
        self.degrade.setObjectName(u"degrade")
        self.degrade.setGeometry(QRect(0, 0, 300, 420))
        self.degrade.setMinimumSize(QSize(300, 420))
        self.degrade.setMaximumSize(QSize(300, 420))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.degrade.setFont(font)
        self.degrade.setStyleSheet(u"\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.327273 rgba(0, 0, 0, 50), stop:0.835 rgba(0, 0, 0, 85));\n"
"")
        self.titulo = QLabel(self.widget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(14, 65, 261, 65))
        self.titulo.setMinimumSize(QSize(14, 65))
        self.titulo.setMaximumSize(QSize(261, 65))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setKerning(True)
        self.titulo.setFont(font1)
        self.titulo.setStyleSheet(u"background-color:none;\n"
"\n"
"")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.usuario = QLineEdit(self.widget)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(50, 135, 200, 40))
        self.usuario.setMinimumSize(QSize(200, 40))
        self.usuario.setMaximumSize(QSize(200, 40))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.usuario.setFont(font2)
        self.usuario.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"border:none;\n"
"border-radius:none;\n"
"border-bottom:2px solid rgb(181, 220, 207);\n"
"color: rgba(255, 255,255, 230);\n"
"padding-bottom:7px;\n"
"")
        self.usuario.setMaxLength(30)
        self.error = QLabel(self.widget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(50, 280, 201, 20))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(True)
        self.error.setFont(font3)
        self.error.setStyleSheet(u"color: rgb(255, 133, 113);")
        self.error.setAlignment(Qt.AlignCenter)
        self.password = QLineEdit(self.widget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(50, 220, 200, 40))
        self.password.setMinimumSize(QSize(200, 40))
        self.password.setMaximumSize(QSize(200, 40))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setItalic(False)
        self.password.setFont(font4)
        self.password.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"border:none;\n"
"border-radius:none;\n"
"border-bottom:2px solid rgb(181, 220, 207);\n"
"color: rgba(255, 255,255, 230);\n"
"padding-bottom:7px;\n"
"")
        self.password.setMaxLength(30)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText(u"*******")
        self.boton = QPushButton(self.widget)
        self.boton.setObjectName(u"boton")
        self.boton.setGeometry(QRect(75, 310, 150, 31))
        self.boton.setStyleSheet(u"background-color: rgb(217, 122, 218);")

        self.retranslateUi(ventanalogin)

        QMetaObject.connectSlotsByName(ventanalogin)
    # setupUi

    def retranslateUi(self, ventanalogin):
        ventanalogin.setWindowTitle(QCoreApplication.translate("ventanalogin", u"Form", None))
        self.fondo_img.setText("")
        self.degrade.setText("")
        self.titulo.setText(QCoreApplication.translate("ventanalogin", u"<html><head/><body><p><span style=\" color:#d977da;\">Iniciar Sesi\u00f3n </span></p></body></html>", None))
        self.usuario.setPlaceholderText(QCoreApplication.translate("ventanalogin", u"USUARIO", None))
        self.error.setText("")
        self.boton.setText(QCoreApplication.translate("ventanalogin", u"Ingresar", None))
    # retranslateUi

