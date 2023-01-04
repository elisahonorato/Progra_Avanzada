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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

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
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 20)
        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 20))

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.verticalWidget, 0, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(150, 1, 150, -1)
        self.boton_plantar = QPushButton(self.widget)
        self.boton_plantar.setObjectName(u"boton_plantar")
        self.boton_plantar.setStyleSheet(u"background-color: rgb(0,150,0);\n"
"color: white;\n"
"border-radius: rounded 50px;\n"
"padding: 5px;\n"
"margin: 5px;")

        self.verticalLayout_6.addWidget(self.boton_plantar)


        self.gridLayout.addWidget(self.widget, 2, 0, 1, 1)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout = QVBoxLayout(self.widget1)
#ifndef Q_OS_MAC
        self.verticalLayout.setSpacing(-1)
#endif
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_nocturno = QLabel(self.widget1)
        self.label_nocturno.setObjectName(u"label_nocturno")

        self.verticalLayout_3.addWidget(self.label_nocturno)

        self.boton_nocturno = QCheckBox(self.widget1)
        self.boton_nocturno.setObjectName(u"boton_nocturno")

        self.verticalLayout_3.addWidget(self.boton_nocturno)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_abuela = QLabel(self.widget1)
        self.label_abuela.setObjectName(u"label_abuela")

        self.verticalLayout_4.addWidget(self.label_abuela)

        self.boton_abuela = QCheckBox(self.widget1)
        self.boton_abuela.setObjectName(u"boton_abuela")

        self.verticalLayout_4.addWidget(self.boton_abuela)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_error = QLabel(self.widget1)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.label_error)


        self.gridLayout.addWidget(self.widget1, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Elige el ambiente de juego", None))
        self.boton_plantar.setText(QCoreApplication.translate("MainWindow", u"A plantar!", None))
        self.label_nocturno.setText("")
        self.boton_nocturno.setText(QCoreApplication.translate("MainWindow", u"Salida Nocturna", None))
        self.label_abuela.setText("")
        self.boton_abuela.setText(QCoreApplication.translate("MainWindow", u"Jard\u00edn de la Abuela", None))
        self.label_error.setText("")
    # retranslateUi

