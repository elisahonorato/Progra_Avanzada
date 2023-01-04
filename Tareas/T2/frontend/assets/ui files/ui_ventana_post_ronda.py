# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_post_ronda.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 500)
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
        self.label = QLabel(self.widget_logo)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_ronda = QLabel(self.widget_logo)
        self.label_ronda.setObjectName(u"label_ronda")

        self.horizontalLayout_2.addWidget(self.label_ronda)

        self.Ronda_actual = QLabel(self.widget_logo)
        self.Ronda_actual.setObjectName(u"Ronda_actual")

        self.horizontalLayout_2.addWidget(self.Ronda_actual)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget_logo)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_soles = QLabel(self.widget_logo)
        self.label_soles.setObjectName(u"label_soles")

        self.horizontalLayout_3.addWidget(self.label_soles)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget_logo)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_zombies = QLabel(self.widget_logo)
        self.label_zombies.setObjectName(u"label_zombies")

        self.horizontalLayout_4.addWidget(self.label_zombies)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.widget_logo)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.label_puntaje = QLabel(self.widget_logo)
        self.label_puntaje.setObjectName(u"label_puntaje")

        self.horizontalLayout_5.addWidget(self.label_puntaje)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.widget_logo)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.label_puntaje_acumulado = QLabel(self.widget_logo)
        self.label_puntaje_acumulado.setObjectName(u"label_puntaje_acumulado")

        self.horizontalLayout_6.addWidget(self.label_puntaje_acumulado)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.gridLayout.addWidget(self.widget_logo, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, 0, 50, -1)
        self.boton_salir = QPushButton(self.centralwidget)
        self.boton_salir.setObjectName(u"boton_salir")
        self.boton_salir.setStyleSheet(u"background-color: rgb(0,150,0);\n"
"color: white;\n"
"border-radius: rounded 3px")

        self.horizontalLayout.addWidget(self.boton_salir)

        self.boton_siguiente_ronda = QPushButton(self.centralwidget)
        self.boton_siguiente_ronda.setObjectName(u"boton_siguiente_ronda")
        self.boton_siguiente_ronda.setStyleSheet(u"background-color: rgb(0,150,0);\n"
"color: white;\n"
"border-radius: rounded 3px")
        self.boton_siguiente_ronda.setFlat(False)

        self.horizontalLayout.addWidget(self.boton_siguiente_ronda)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.label_ganador = QLabel(self.centralwidget)
        self.label_ganador.setObjectName(u"label_ganador")

        self.gridLayout.addWidget(self.label_ganador, 2, 0, 1, 1)

        self.label_perdedor = QLabel(self.centralwidget)
        self.label_perdedor.setObjectName(u"label_perdedor")

        self.gridLayout.addWidget(self.label_perdedor, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Resumen de Ronda", None))
        self.label_ronda.setText(QCoreApplication.translate("MainWindow", u"Ronda Actual", None))
        self.Ronda_actual.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Soles Restantes", None))
        self.label_soles.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Zombies Destruidos", None))
        self.label_zombies.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Puntaje Ronda", None))
        self.label_puntaje.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Puntaje Total", None))
        self.label_puntaje_acumulado.setText("")
        self.boton_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.boton_siguiente_ronda.setText(QCoreApplication.translate("MainWindow", u"Siguiente Ronda", None))
        self.label_ganador.setText(QCoreApplication.translate("MainWindow", u"Ganaste, Puedes combatir la siguiente oleada!", None))
        self.label_perdedor.setText(QCoreApplication.translate("MainWindow", u"Perdiste", None))
    # retranslateUi

