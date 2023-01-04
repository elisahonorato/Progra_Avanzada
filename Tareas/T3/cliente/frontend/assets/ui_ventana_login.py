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
        ventanalogin.resize(700, 420)
        ventanalogin.setMinimumSize(QSize(700, 420))
        ventanalogin.setMaximumSize(QSize(700, 420))
        self.widget = QWidget(ventanalogin)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 700, 420))
        self.widget.setMinimumSize(QSize(700, 420))
        self.widget.setMaximumSize(QSize(600, 420))
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
        self.degrade = QLabel(self.widget)
        self.degrade.setObjectName(u"degrade")
        self.degrade.setGeometry(QRect(0, 0, 700, 420))
        self.degrade.setMinimumSize(QSize(700, 420))
        self.degrade.setMaximumSize(QSize(700, 420))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.degrade.setFont(font)
        self.degrade.setStyleSheet(u"\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.327273 rgba(0, 0, 0, 50), stop:0.835 rgba(0, 0, 0, 85));\n"
"")
        self.usuario = QLineEdit(self.widget)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(260, 290, 200, 40))
        self.usuario.setMinimumSize(QSize(200, 40))
        self.usuario.setMaximumSize(QSize(200, 40))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        self.usuario.setFont(font1)
        self.usuario.setStyleSheet(u"background-color: rgba(255,255,255,255);\n"
"border:none;\n"
"border-radius:none;\n"
"border-bottom:2px solid rgb(181, 220, 207);\n"
"color: rgba(0,0,0,0);\n"
"")
        self.usuario.setMaxLength(30)
        self.error = QLabel(self.widget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(50, 280, 201, 20))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(True)
        self.error.setFont(font2)
        self.error.setStyleSheet(u"color: rgb(255, 133, 113);")
        self.error.setAlignment(Qt.AlignCenter)
        self.boton = QPushButton(self.widget)
        self.boton.setObjectName(u"boton")
        self.boton.setGeometry(QRect(280, 350, 171, 41))
        self.boton.setStyleSheet(u"background-color: rgb(50, 60, 250);")
        self.fondo_img = QLabel(self.widget)
        self.fondo_img.setObjectName(u"fondo_img")
        self.fondo_img.setGeometry(QRect(0, 0, 700, 420))
        self.fondo_img.setMinimumSize(QSize(700, 420))
        self.fondo_img.setMaximumSize(QSize(700, 420))
        self.fondo_img.setAutoFillBackground(False)
        self.fondo_img.setStyleSheet(u"")
        self.fondo_img.setPixmap(QPixmap(u"../../sprites/background/index1.png"))
        self.fondo_img.setScaledContents(True)
        self.fondo_img.raise_()
        self.degrade.raise_()
        self.usuario.raise_()
        self.error.raise_()
        self.boton.raise_()

        self.retranslateUi(ventanalogin)

        QMetaObject.connectSlotsByName(ventanalogin)
    # setupUi

    def retranslateUi(self, ventanalogin):
        ventanalogin.setWindowTitle(QCoreApplication.translate("ventanalogin", u"Form", None))
        self.degrade.setText("")
        self.usuario.setPlaceholderText(QCoreApplication.translate("ventanalogin", u"Escribe tu nombre...", None))
        self.error.setText("")
        self.boton.setText(QCoreApplication.translate("ventanalogin", u"Ingresar", None))
        self.fondo_img.setText("")
    # retranslateUi

