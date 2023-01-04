# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_inicio.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(778, 500)
        MainWindow.setMinimumSize(QSize(400, 400))
        MainWindow.setMaximumSize(QSize(1000, 1000))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_logo = QWidget(self.centralwidget)
        self.widget_logo.setObjectName(u"widget_logo")
        self.verticalLayout = QVBoxLayout(self.widget_logo)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addWidget(self.widget_logo, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(150, 100, 150, -1)
        self.boton_usuario = QLineEdit(self.centralwidget)
        self.boton_usuario.setObjectName(u"boton_usuario")

        self.verticalLayout_6.addWidget(self.boton_usuario)

        self.label_error = QLabel(self.centralwidget)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setEnabled(True)
        self.label_error.setMouseTracking(False)
        self.label_error.setStyleSheet(u"color: white; background-color: transparent")

        self.verticalLayout_6.addWidget(self.label_error)

        self.boton_jugar = QPushButton(self.centralwidget)
        self.boton_jugar.setObjectName(u"boton_jugar")
        self.boton_jugar.setStyleSheet(u"background-color: rgb(0,150,0);\n"
"color: white;\n"
"border-radius: rounded 3px")
        self.boton_jugar.setFlat(False)

        self.verticalLayout_6.addWidget(self.boton_jugar)

        self.boton_ranking = QPushButton(self.centralwidget)
        self.boton_ranking.setObjectName(u"boton_ranking")
        self.boton_ranking.setStyleSheet(u"background-color: rgb(0,150,0);\n"
"color: white;\n"
"border-radius: rounded 3px")

        self.verticalLayout_6.addWidget(self.boton_ranking)

        self.boton_salir = QPushButton(self.centralwidget)
        self.boton_salir.setObjectName(u"boton_salir")
        self.boton_salir.setStyleSheet(u"background-color: rgb(0,150,0);\n"
"color: white;\n"
"border-radius: rounded 3px")

        self.verticalLayout_6.addWidget(self.boton_salir)


        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_error.setText("")
        self.boton_jugar.setText(QCoreApplication.translate("MainWindow", u"Jugar", None))
        self.boton_ranking.setText(QCoreApplication.translate("MainWindow", u"Ranking", None))
        self.boton_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

