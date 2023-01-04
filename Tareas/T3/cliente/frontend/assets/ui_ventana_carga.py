# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_carga.ui'
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
        self.degrade = QLabel(self.widget)
        self.degrade.setObjectName(u"degrade")
        self.degrade.setGeometry(QRect(20, 20, 660, 380))
        self.degrade.setMinimumSize(QSize(660, 380))
        self.degrade.setMaximumSize(QSize(660, 380))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.degrade.setFont(font)
        self.degrade.setStyleSheet(u"border-radius: 20;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.327273 rgba(0, 0, 0, 50), stop:0.835 rgba(0, 0, 0, 85));\n"
"")
        self.boton_volver = QPushButton(self.widget)
        self.boton_volver.setObjectName(u"boton_volver")
        self.boton_volver.setGeometry(QRect(290, 310, 120, 80))
        self.boton_volver.setMinimumSize(QSize(120, 80))
        self.boton_volver.setMaximumSize(QSize(120, 80))
        self.boton_volver.setStyleSheet(u"background-color: transparent")
        icon = QIcon()
        icon.addFile(u"../../sprites/background/back_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_volver.setIcon(icon)
        self.boton_volver.setIconSize(QSize(120, 80))
        self.fondo_img = QLabel(self.widget)
        self.fondo_img.setObjectName(u"fondo_img")
        self.fondo_img.setGeometry(QRect(0, 0, 700, 420))
        self.fondo_img.setMinimumSize(QSize(700, 420))
        self.fondo_img.setMaximumSize(QSize(700, 420))
        self.fondo_img.setAutoFillBackground(False)
        self.fondo_img.setStyleSheet(u"")
        self.fondo_img.setPixmap(QPixmap(u"../../sprites/background/index3.png"))
        self.fondo_img.setScaledContents(True)
        self.label_jugador_1 = QLabel(self.widget)
        self.label_jugador_1.setObjectName(u"label_jugador_1")
        self.label_jugador_1.setGeometry(QRect(140, 160, 141, 131))
        self.label_jugador_1.setStyleSheet(u"color: black; background-color: white; border-radius: 20; ")
        self.label_jugador_1.setAlignment(Qt.AlignCenter)
        self.label_jugador_2 = QLabel(self.widget)
        self.label_jugador_2.setObjectName(u"label_jugador_2")
        self.label_jugador_2.setGeometry(QRect(420, 160, 141, 131))
        self.label_jugador_2.setStyleSheet(u"color: black; background-color: white; border-radius: 20; ")
        self.label_jugador_2.setAlignment(Qt.AlignCenter)
        self.label_contador = QLabel(self.widget)
        self.label_contador.setObjectName(u"label_contador")
        self.label_contador.setGeometry(QRect(280, 30, 141, 91))
        self.label_contador.setStyleSheet(u"color: white; background-color: transparent; font-size:40px;border-radius: 20; ")
        self.label_contador.setAlignment(Qt.AlignCenter)
        self.fondo_img.raise_()
        self.degrade.raise_()
        self.boton_volver.raise_()
        self.label_jugador_1.raise_()
        self.label_jugador_2.raise_()
        self.label_contador.raise_()

        self.retranslateUi(ventanalogin)

        QMetaObject.connectSlotsByName(ventanalogin)
    # setupUi

    def retranslateUi(self, ventanalogin):
        ventanalogin.setWindowTitle(QCoreApplication.translate("ventanalogin", u"Form", None))
        self.degrade.setText("")
        self.boton_volver.setText("")
        self.fondo_img.setText("")
        self.label_jugador_1.setText(QCoreApplication.translate("ventanalogin", u"Jugador 1", None))
        self.label_jugador_2.setText(QCoreApplication.translate("ventanalogin", u"Jugador 2", None))
        self.label_contador.setText("")
    # retranslateUi

