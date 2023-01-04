# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_final.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

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
        self.label_texto = QLabel(self.widget)
        self.label_texto.setObjectName(u"label_texto")
        self.label_texto.setGeometry(QRect(20, 20, 640, 380))
        self.label_texto.setMinimumSize(QSize(640, 380))
        self.label_texto.setMaximumSize(QSize(640, 380))
        font = QFont()
        self.label_texto.setFont(font)
        self.label_texto.setStyleSheet(u"color: black; border-radius: 20;\n"
"background-color: white")
        self.label_texto.setAlignment(Qt.AlignCenter)
        self.fondo_img = QLabel(self.widget)
        self.fondo_img.setObjectName(u"fondo_img")
        self.fondo_img.setGeometry(QRect(0, 0, 700, 420))
        self.fondo_img.setMinimumSize(QSize(700, 420))
        self.fondo_img.setMaximumSize(QSize(700, 420))
        self.fondo_img.setAutoFillBackground(False)
        self.fondo_img.setStyleSheet(u"")
        self.fondo_img.setPixmap(QPixmap(u"../../sprites/background/fight.png"))
        self.fondo_img.setScaledContents(True)
        self.boton_volver = QPushButton(self.widget)
        self.boton_volver.setObjectName(u"boton_volver")
        self.boton_volver.setGeometry(QRect(300, 300, 120, 80))
        self.boton_volver.setMinimumSize(QSize(120, 80))
        self.boton_volver.setMaximumSize(QSize(120, 80))
        self.boton_volver.setStyleSheet(u"background-color: transparent")
        icon = QIcon()
        icon.addFile(u"../../sprites/background/back_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_volver.setIcon(icon)
        self.boton_volver.setIconSize(QSize(120, 80))
        self.fondo_img.raise_()
        self.label_texto.raise_()
        self.boton_volver.raise_()

        self.retranslateUi(ventanalogin)

        QMetaObject.connectSlotsByName(ventanalogin)
    # setupUi

    def retranslateUi(self, ventanalogin):
        ventanalogin.setWindowTitle(QCoreApplication.translate("ventanalogin", u"Form", None))
        self.label_texto.setText("")
        self.fondo_img.setText("")
        self.boton_volver.setText("")
    # retranslateUi

