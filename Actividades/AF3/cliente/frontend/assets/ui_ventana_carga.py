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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_PantallaCarga(object):
    def setupUi(self, PantallaCarga):
        if not PantallaCarga.objectName():
            PantallaCarga.setObjectName(u"PantallaCarga")
        PantallaCarga.resize(669, 399)
        PantallaCarga.setMinimumSize(QSize(669, 399))
        PantallaCarga.setMaximumSize(QSize(669, 399))
        self.centralwidget = QWidget(PantallaCarga)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.marcocirculo = QFrame(self.centralwidget)
        self.marcocirculo.setObjectName(u"marcocirculo")
        self.marcocirculo.setStyleSheet(u"QFrame {	\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:0.466, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(54, 54, 54, 255));\n"
"	\n"
"\n"
"	border-radius: 8px;\n"
"}")
        self.marcocirculo.setFrameShape(QFrame.StyledPanel)
        self.marcocirculo.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.marcocirculo)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 280, 561, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgba(255, 255, 255,100);\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 8px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 8px;\n"
"	;\n"
"	background-color: rgb(239, 134, 236);\n"
"}")
        self.progressBar.setValue(24)
        self.label_cargando = QLabel(self.marcocirculo)
        self.label_cargando.setObjectName(u"label_cargando")
        self.label_cargando.setGeometry(QRect(0, 320, 661, 21))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.label_cargando.setFont(font)
        self.label_cargando.setStyleSheet(u"color: rgb(30, 215, 97);\n"
"background-color: none;")
        self.label_cargando.setAlignment(Qt.AlignCenter)
        self.logo = QLabel(self.marcocirculo)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(140, 50, 381, 80))
        self.logo.setMaximumSize(QSize(381, 131))
        self.logo.setStyleSheet(u"background-color: none;\n"
"")
        self.logo.setPixmap(QPixmap(u"Letra.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.label_descripcion = QLabel(self.marcocirculo)
        self.label_descripcion.setObjectName(u"label_descripcion")
        self.label_descripcion.setGeometry(QRect(-10, 220, 661, 21))
        self.label_descripcion.setFont(font)
        self.label_descripcion.setStyleSheet(u"color: rgb(255, 170, 255);\n"
"background-color: none;")
        self.label_descripcion.setAlignment(Qt.AlignCenter)
        self.logo_2 = QLabel(self.marcocirculo)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(300, 160, 51, 51))
        self.logo_2.setMaximumSize(QSize(381, 131))
        self.logo_2.setStyleSheet(u"background-color: none;\n"
"")
        self.logo_2.setPixmap(QPixmap(u"Logo.png"))
        self.logo_2.setScaledContents(True)
        self.logo_2.setWordWrap(False)

        self.verticalLayout.addWidget(self.marcocirculo)

        PantallaCarga.setCentralWidget(self.centralwidget)

        self.retranslateUi(PantallaCarga)

        QMetaObject.connectSlotsByName(PantallaCarga)
    # setupUi

    def retranslateUi(self, PantallaCarga):
        PantallaCarga.setWindowTitle(QCoreApplication.translate("PantallaCarga", u"MainWindow", None))
        self.label_cargando.setText(QCoreApplication.translate("PantallaCarga", u"<html><head/><body><p><span style=\" color:#ef86ec;\">cargando...</span></p></body></html>", None))
        self.logo.setText("")
        self.label_descripcion.setText(QCoreApplication.translate("PantallaCarga", u"<html><head/><body><p><span style=\" color:#ef86ec;\">\u00a1La musica esta en todos lados!</span></p></body></html>", None))
        self.logo_2.setText("")
    # retranslateUi

