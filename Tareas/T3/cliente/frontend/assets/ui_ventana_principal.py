# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
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
        self.degrade.setGeometry(QRect(20, 20, 640, 380))
        self.degrade.setMinimumSize(QSize(640, 380))
        self.degrade.setMaximumSize(QSize(640, 380))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.degrade.setFont(font)
        self.degrade.setStyleSheet(u"border-radius: 20;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.327273 rgba(0, 0, 0, 50), stop:0.835 rgba(0, 0, 0, 85));\n"
"")
        self.boton_seleccionar = QPushButton(self.widget)
        self.boton_seleccionar.setObjectName(u"boton_seleccionar")
        self.boton_seleccionar.setGeometry(QRect(530, 340, 100, 60))
        self.boton_seleccionar.setMinimumSize(QSize(100, 60))
        self.boton_seleccionar.setMaximumSize(QSize(100, 60))
        self.boton_seleccionar.setStyleSheet(u"background-color: red; border-radius: 20px;")
        self.boton_seleccionar.setIconSize(QSize(120, 80))
        self.fondo_img = QLabel(self.widget)
        self.fondo_img.setObjectName(u"fondo_img")
        self.fondo_img.setGeometry(QRect(0, 0, 700, 420))
        self.fondo_img.setMinimumSize(QSize(700, 420))
        self.fondo_img.setMaximumSize(QSize(700, 420))
        self.fondo_img.setAutoFillBackground(False)
        self.fondo_img.setStyleSheet(u"")
        self.fondo_img.setPixmap(QPixmap(u"../../sprites/background/fight.png"))
        self.fondo_img.setScaledContents(True)
        self.label_oponente = QLabel(self.widget)
        self.label_oponente.setObjectName(u"label_oponente")
        self.label_oponente.setGeometry(QRect(140, 110, 141, 181))
        self.label_oponente.setStyleSheet(u"color: black; background-color: white; border-radius: 20; ")
        self.label_oponente.setPixmap(QPixmap(u"../../sprites/cartas/back.png"))
        self.label_oponente.setScaledContents(True)
        self.label_oponente.setAlignment(Qt.AlignCenter)
        self.label_jugador = QLabel(self.widget)
        self.label_jugador.setObjectName(u"label_jugador")
        self.label_jugador.setGeometry(QRect(420, 110, 141, 181))
        self.label_jugador.setStyleSheet(u"color: black; background-color: white; border-radius: 20; ")
        self.label_jugador.setPixmap(QPixmap(u"../../sprites/cartas/back.png"))
        self.label_jugador.setScaledContents(True)
        self.label_jugador.setAlignment(Qt.AlignCenter)
        self.label_contador = QLabel(self.widget)
        self.label_contador.setObjectName(u"label_contador")
        self.label_contador.setGeometry(QRect(280, 30, 141, 91))
        self.label_contador.setStyleSheet(u"color: white; background-color: transparent; font-size:40px;border-radius: 20; ")
        self.label_contador.setAlignment(Qt.AlignCenter)
        self.label_tabla = QLabel(self.widget)
        self.label_tabla.setObjectName(u"label_tabla")
        self.label_tabla.setGeometry(QRect(20, 0, 661, 421))
        self.label_tabla.setStyleSheet(u"background-color: transparent")
        self.label_tabla.setPixmap(QPixmap(u"../../sprites/background/table.png"))
        self.label_tabla.setScaledContents(True)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 100, 31, 51))
        self.label.setPixmap(QPixmap(u"../../sprites/cartas/back.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 130, 31, 51))
        self.label_2.setPixmap(QPixmap(u"../../sprites/cartas/back.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 160, 31, 51))
        self.label_3.setPixmap(QPixmap(u"../../sprites/cartas/back.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 190, 31, 51))
        self.label_4.setPixmap(QPixmap(u"../../sprites/cartas/back.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 220, 31, 51))
        self.label_5.setPixmap(QPixmap(u"../../sprites/cartas/back.png"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 70, 91, 21))
        self.label_6.setStyleSheet(u"color: white; font-size: 16px; font-weight: bold; background-color: rgb(0,0,0); border-radius: 20;")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(450, 70, 91, 21))
        self.label_7.setStyleSheet(u"color: white; font-size: 16px; font-weight: bold; background-color: rgb(0,0,0); border-radius: 20;")
        self.fondo_img.raise_()
        self.degrade.raise_()
        self.label_oponente.raise_()
        self.label_jugador.raise_()
        self.label_contador.raise_()
        self.label_tabla.raise_()
        self.boton_seleccionar.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()

        self.retranslateUi(ventanalogin)

        QMetaObject.connectSlotsByName(ventanalogin)
    # setupUi

    def retranslateUi(self, ventanalogin):
        ventanalogin.setWindowTitle(QCoreApplication.translate("ventanalogin", u"Form", None))
        self.degrade.setText("")
        self.boton_seleccionar.setText(QCoreApplication.translate("ventanalogin", u"Seleccionar", None))
        self.fondo_img.setText("")
        self.label_oponente.setText("")
        self.label_jugador.setText("")
        self.label_contador.setText("")
        self.label_tabla.setText("")
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("ventanalogin", u"OPONENTE", None))
        self.label_7.setText(QCoreApplication.translate("ventanalogin", u"JUGADOR", None))
    # retranslateUi

