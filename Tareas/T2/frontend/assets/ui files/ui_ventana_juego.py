# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_juego.ui'
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
        MainWindow.resize(1000, 505)
        MainWindow.setMinimumSize(QSize(400, 400))
        MainWindow.setMaximumSize(QSize(1000, 1000))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 0))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_tienda_juego = QWidget(self.centralwidget)
        self.label_tienda_juego.setObjectName(u"label_tienda_juego")
        self.label_tienda_juego.setMaximumSize(QSize(150, 16777215))
        self.label_tienda_juego.setAutoFillBackground(False)
        self.label_tienda_juego.setStyleSheet(u"background-color: rgb(0,200,0)")
        self.verticalLayout_4 = QVBoxLayout(self.label_tienda_juego)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_planta_girasol = QWidget(self.label_tienda_juego)
        self.label_planta_girasol.setObjectName(u"label_planta_girasol")
        self.label_planta_girasol.setMinimumSize(QSize(150, 100))
        self.label_planta_girasol.setMaximumSize(QSize(100, 100))
        self.horizontalLayout_4 = QHBoxLayout(self.label_planta_girasol)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.label_planta_girasol)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../../../sprites/Plantas/girasol_1.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label)

        self.icono_soles_planta_girasol = QLabel(self.label_planta_girasol)
        self.icono_soles_planta_girasol.setObjectName(u"icono_soles_planta_girasol")
        self.icono_soles_planta_girasol.setEnabled(True)
        self.icono_soles_planta_girasol.setMinimumSize(QSize(20, 20))
        self.icono_soles_planta_girasol.setMaximumSize(QSize(20, 20))
        self.icono_soles_planta_girasol.setLineWidth(0)
        self.icono_soles_planta_girasol.setPixmap(QPixmap(u"../../../sprites/Elementos de juego/sol.png"))
        self.icono_soles_planta_girasol.setScaledContents(True)
        self.icono_soles_planta_girasol.setWordWrap(False)
        self.icono_soles_planta_girasol.setIndent(0)

        self.horizontalLayout_4.addWidget(self.icono_soles_planta_girasol)

        self.soles_planta_girasol = QLabel(self.label_planta_girasol)
        self.soles_planta_girasol.setObjectName(u"soles_planta_girasol")

        self.horizontalLayout_4.addWidget(self.soles_planta_girasol)


        self.verticalLayout_4.addWidget(self.label_planta_girasol)

        self.label_planta_clasica = QWidget(self.label_tienda_juego)
        self.label_planta_clasica.setObjectName(u"label_planta_clasica")
        self.label_planta_clasica.setMinimumSize(QSize(150, 100))
        self.label_planta_clasica.setMaximumSize(QSize(100, 100))
        self.horizontalLayout_7 = QHBoxLayout(self.label_planta_clasica)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.label_planta_clasica)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"../../../sprites/Plantas/lanzaguisantes_1.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.icono_soles_planta_clasica = QLabel(self.label_planta_clasica)
        self.icono_soles_planta_clasica.setObjectName(u"icono_soles_planta_clasica")
        self.icono_soles_planta_clasica.setEnabled(True)
        self.icono_soles_planta_clasica.setMinimumSize(QSize(20, 20))
        self.icono_soles_planta_clasica.setMaximumSize(QSize(20, 20))
        self.icono_soles_planta_clasica.setLineWidth(0)
        self.icono_soles_planta_clasica.setPixmap(QPixmap(u"../../../sprites/Elementos de juego/sol.png"))
        self.icono_soles_planta_clasica.setScaledContents(True)
        self.icono_soles_planta_clasica.setWordWrap(False)
        self.icono_soles_planta_clasica.setIndent(0)

        self.horizontalLayout_7.addWidget(self.icono_soles_planta_clasica)

        self.soles_planta_clasica = QLabel(self.label_planta_clasica)
        self.soles_planta_clasica.setObjectName(u"soles_planta_clasica")

        self.horizontalLayout_7.addWidget(self.soles_planta_clasica)


        self.verticalLayout_4.addWidget(self.label_planta_clasica)

        self.label_planta_azul = QWidget(self.label_tienda_juego)
        self.label_planta_azul.setObjectName(u"label_planta_azul")
        self.label_planta_azul.setMinimumSize(QSize(150, 100))
        self.label_planta_azul.setMaximumSize(QSize(100, 100))
        self.horizontalLayout_5 = QHBoxLayout(self.label_planta_azul)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.label_planta_azul)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"../../../sprites/Plantas/lanzaguisantesHielo_1.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.icono_soles_planta_azul = QLabel(self.label_planta_azul)
        self.icono_soles_planta_azul.setObjectName(u"icono_soles_planta_azul")
        self.icono_soles_planta_azul.setEnabled(True)
        self.icono_soles_planta_azul.setMinimumSize(QSize(20, 20))
        self.icono_soles_planta_azul.setMaximumSize(QSize(20, 20))
        self.icono_soles_planta_azul.setLineWidth(0)
        self.icono_soles_planta_azul.setPixmap(QPixmap(u"../../../sprites/Elementos de juego/sol.png"))
        self.icono_soles_planta_azul.setScaledContents(True)
        self.icono_soles_planta_azul.setWordWrap(False)
        self.icono_soles_planta_azul.setIndent(0)

        self.horizontalLayout_5.addWidget(self.icono_soles_planta_azul)

        self.soles_planta_azul = QLabel(self.label_planta_azul)
        self.soles_planta_azul.setObjectName(u"soles_planta_azul")

        self.horizontalLayout_5.addWidget(self.soles_planta_azul)


        self.verticalLayout_4.addWidget(self.label_planta_azul)

        self.label_planta_papa = QWidget(self.label_tienda_juego)
        self.label_planta_papa.setObjectName(u"label_planta_papa")
        self.label_planta_papa.setMinimumSize(QSize(150, 100))
        self.label_planta_papa.setMaximumSize(QSize(100, 100))
        self.horizontalLayout_11 = QHBoxLayout(self.label_planta_papa)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.label_planta_papa)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u"../../../sprites/Plantas/papa_1.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_4)

        self.icono_soles_planta_papa = QLabel(self.label_planta_papa)
        self.icono_soles_planta_papa.setObjectName(u"icono_soles_planta_papa")
        self.icono_soles_planta_papa.setEnabled(True)
        self.icono_soles_planta_papa.setMinimumSize(QSize(20, 20))
        self.icono_soles_planta_papa.setMaximumSize(QSize(20, 20))
        self.icono_soles_planta_papa.setLineWidth(0)
        self.icono_soles_planta_papa.setPixmap(QPixmap(u"../../../sprites/Elementos de juego/sol.png"))
        self.icono_soles_planta_papa.setScaledContents(True)
        self.icono_soles_planta_papa.setWordWrap(False)
        self.icono_soles_planta_papa.setIndent(0)

        self.horizontalLayout_11.addWidget(self.icono_soles_planta_papa)

        self.soles_planta_papa = QLabel(self.label_planta_papa)
        self.soles_planta_papa.setObjectName(u"soles_planta_papa")

        self.horizontalLayout_11.addWidget(self.soles_planta_papa)


        self.verticalLayout_4.addWidget(self.label_planta_papa)

        self.label_margen = QWidget(self.label_tienda_juego)
        self.label_margen.setObjectName(u"label_margen")
        self.label_margen.setMinimumSize(QSize(150, 100))
        self.label_margen.setMaximumSize(QSize(100, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.label_margen)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_4.addWidget(self.label_margen)


        self.horizontalLayout.addWidget(self.label_tienda_juego)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_fondo_juego = QWidget(self.centralwidget)
        self.widget_fondo_juego.setObjectName(u"widget_fondo_juego")
        self.widget_fondo_juego.setMaximumSize(QSize(900, 500))
        self.label_fondo_juego = QLabel(self.widget_fondo_juego)
        self.label_fondo_juego.setObjectName(u"label_fondo_juego")
        self.label_fondo_juego.setGeometry(QRect(0, -5, 900, 350))
        self.label_fondo_juego.setMinimumSize(QSize(800, 350))
        self.label_fondo_juego.setMaximumSize(QSize(900, 350))
        self.label_fondo_juego.setPixmap(QPixmap(u"../sprites/Fondos/jardinAbuela.png"))
        self.label_fondo_juego.setScaledContents(True)
        self.label_sector_plantas = QWidget(self.widget_fondo_juego)
        self.label_sector_plantas.setObjectName(u"label_sector_plantas")
        self.label_sector_plantas.setGeometry(QRect(160, 119, 471, 111))
        self.sector_juego = QGridLayout(self.label_sector_plantas)
        self.sector_juego.setObjectName(u"sector_juego")
        self.label_planta_10 = QLabel(self.label_sector_plantas)
        self.label_planta_10.setObjectName(u"label_planta_10")
        self.label_planta_10.setMinimumSize(QSize(40, 50))
        self.label_planta_10.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_10, 0, 9, 1, 1)

        self.label_planta_11 = QLabel(self.label_sector_plantas)
        self.label_planta_11.setObjectName(u"label_planta_11")
        self.label_planta_11.setMinimumSize(QSize(40, 50))
        self.label_planta_11.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_11, 1, 0, 1, 1)

        self.label_planta_19 = QLabel(self.label_sector_plantas)
        self.label_planta_19.setObjectName(u"label_planta_19")
        self.label_planta_19.setMinimumSize(QSize(40, 50))
        self.label_planta_19.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_19, 1, 8, 1, 1)

        self.label_planta_6 = QLabel(self.label_sector_plantas)
        self.label_planta_6.setObjectName(u"label_planta_6")
        self.label_planta_6.setMinimumSize(QSize(40, 50))
        self.label_planta_6.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_6, 0, 5, 1, 1)

        self.label_planta_9 = QLabel(self.label_sector_plantas)
        self.label_planta_9.setObjectName(u"label_planta_9")
        self.label_planta_9.setMinimumSize(QSize(40, 50))
        self.label_planta_9.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_9, 0, 8, 1, 1)

        self.label_planta_4 = QLabel(self.label_sector_plantas)
        self.label_planta_4.setObjectName(u"label_planta_4")
        self.label_planta_4.setMinimumSize(QSize(40, 50))
        self.label_planta_4.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_4, 0, 3, 1, 1)

        self.label_planta_13 = QLabel(self.label_sector_plantas)
        self.label_planta_13.setObjectName(u"label_planta_13")
        self.label_planta_13.setMinimumSize(QSize(40, 50))
        self.label_planta_13.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_13, 1, 2, 1, 1)

        self.label_planta_18 = QLabel(self.label_sector_plantas)
        self.label_planta_18.setObjectName(u"label_planta_18")
        self.label_planta_18.setMinimumSize(QSize(40, 50))
        self.label_planta_18.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_18, 1, 7, 1, 1)

        self.label_planta_1 = QLabel(self.label_sector_plantas)
        self.label_planta_1.setObjectName(u"label_planta_1")
        self.label_planta_1.setMinimumSize(QSize(40, 50))
        self.label_planta_1.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_1, 0, 0, 1, 1)

        self.label_planta_20 = QLabel(self.label_sector_plantas)
        self.label_planta_20.setObjectName(u"label_planta_20")
        self.label_planta_20.setMinimumSize(QSize(40, 50))
        self.label_planta_20.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_20, 1, 9, 1, 1)

        self.label_planta_8 = QLabel(self.label_sector_plantas)
        self.label_planta_8.setObjectName(u"label_planta_8")
        self.label_planta_8.setMinimumSize(QSize(40, 50))
        self.label_planta_8.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_8, 0, 7, 1, 1)

        self.label_planta_14 = QLabel(self.label_sector_plantas)
        self.label_planta_14.setObjectName(u"label_planta_14")
        self.label_planta_14.setMinimumSize(QSize(40, 50))
        self.label_planta_14.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_14, 1, 3, 1, 1)

        self.label_planta_3 = QLabel(self.label_sector_plantas)
        self.label_planta_3.setObjectName(u"label_planta_3")
        self.label_planta_3.setMinimumSize(QSize(40, 50))
        self.label_planta_3.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_3, 0, 2, 1, 1)

        self.label_planta_12 = QLabel(self.label_sector_plantas)
        self.label_planta_12.setObjectName(u"label_planta_12")
        self.label_planta_12.setMinimumSize(QSize(40, 50))
        self.label_planta_12.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_12, 1, 1, 1, 1)

        self.label_planta_2 = QLabel(self.label_sector_plantas)
        self.label_planta_2.setObjectName(u"label_planta_2")
        self.label_planta_2.setMinimumSize(QSize(40, 50))
        self.label_planta_2.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_2, 0, 1, 1, 1)

        self.label_planta_5 = QLabel(self.label_sector_plantas)
        self.label_planta_5.setObjectName(u"label_planta_5")
        self.label_planta_5.setMinimumSize(QSize(40, 50))
        self.label_planta_5.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_5, 0, 4, 1, 1)

        self.label_planta_7 = QLabel(self.label_sector_plantas)
        self.label_planta_7.setObjectName(u"label_planta_7")
        self.label_planta_7.setMinimumSize(QSize(40, 50))
        self.label_planta_7.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_7, 0, 6, 1, 1)

        self.label_planta_15 = QLabel(self.label_sector_plantas)
        self.label_planta_15.setObjectName(u"label_planta_15")
        self.label_planta_15.setMinimumSize(QSize(40, 50))
        self.label_planta_15.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_15, 1, 4, 1, 1)

        self.label_planta_17 = QLabel(self.label_sector_plantas)
        self.label_planta_17.setObjectName(u"label_planta_17")
        self.label_planta_17.setMinimumSize(QSize(40, 50))
        self.label_planta_17.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_17, 1, 6, 1, 1)

        self.label_planta_16 = QLabel(self.label_sector_plantas)
        self.label_planta_16.setObjectName(u"label_planta_16")
        self.label_planta_16.setMinimumSize(QSize(40, 50))
        self.label_planta_16.setMaximumSize(QSize(40, 50))

        self.sector_juego.addWidget(self.label_planta_16, 1, 5, 1, 1)

        self.label_sector_zombie = QWidget(self.widget_fondo_juego)
        self.label_sector_zombie.setObjectName(u"label_sector_zombie")
        self.label_sector_zombie.setGeometry(QRect(640, 119, 91, 111))
        self.verticalLayout_2 = QVBoxLayout(self.label_sector_zombie)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.carril_zombie_1 = QLabel(self.label_sector_zombie)
        self.carril_zombie_1.setObjectName(u"carril_zombie_1")

        self.verticalLayout_2.addWidget(self.carril_zombie_1)

        self.carril_zombie_2 = QLabel(self.label_sector_zombie)
        self.carril_zombie_2.setObjectName(u"carril_zombie_2")

        self.verticalLayout_2.addWidget(self.carril_zombie_2)


        self.gridLayout_4.addWidget(self.widget_fondo_juego, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_4)

        self.horizontalWidget = QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget = QWidget(self.horizontalWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(0,150,0)")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.boton_pausa = QPushButton(self.widget)
        self.boton_pausa.setObjectName(u"boton_pausa")
        self.boton_pausa.setMaximumSize(QSize(80, 16777215))
        self.boton_pausa.setStyleSheet(u"color: white; background-color: rgb(0,200,0);border : 2px solid white; border-radius : 20px; padding: 10")

        self.gridLayout_3.addWidget(self.boton_pausa, 1, 0, 1, 1)

        self.boton_avanzar = QPushButton(self.widget)
        self.boton_avanzar.setObjectName(u"boton_avanzar")
        self.boton_avanzar.setMaximumSize(QSize(80, 16777215))
        self.boton_avanzar.setStyleSheet(u"color: white; background-color: rgb(0,200,0);border : 2px solid white; border-radius : 20px; padding: 10")

        self.gridLayout_3.addWidget(self.boton_avanzar, 0, 1, 1, 1)

        self.boton_iniciar = QPushButton(self.widget)
        self.boton_iniciar.setObjectName(u"boton_iniciar")
        self.boton_iniciar.setMaximumSize(QSize(80, 16777215))
        self.boton_iniciar.setStyleSheet(u"color: white; background-color: rgb(0,200,0);border : 2px solid white; border-radius : 20px; padding: 10")

        self.gridLayout_3.addWidget(self.boton_iniciar, 0, 0, 1, 1)

        self.boton_salir = QPushButton(self.widget)
        self.boton_salir.setObjectName(u"boton_salir")
        self.boton_salir.setMaximumSize(QSize(80, 16777215))
        self.boton_salir.setStyleSheet(u"color: white; background-color: rgb(0,200,0);border : 2px solid white; border-radius : 20px; padding: 10")

        self.gridLayout_3.addWidget(self.boton_salir, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 5, 1, 1)

        self.verticalWidget_3 = QWidget(self.widget)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalWidget_3.setMaximumSize(QSize(140, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.verticalWidget_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_15 = QLabel(self.verticalWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(100, 16777215))
        self.label_15.setStyleSheet(u"font-weight: light;\n"
"color: white;\n"
"")

        self.horizontalLayout_8.addWidget(self.label_15, 0, Qt.AlignRight)

        self.label_nivel = QLabel(self.verticalWidget_3)
        self.label_nivel.setObjectName(u"label_nivel")
        self.label_nivel.setMaximumSize(QSize(100, 16777215))
        self.label_nivel.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"")

        self.horizontalLayout_8.addWidget(self.label_nivel, 0, Qt.AlignLeft)


        self.gridLayout_2.addWidget(self.verticalWidget_3, 1, 1, 1, 1)

        self.verticalWidget = QWidget(self.widget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setMaximumSize(QSize(140, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.verticalWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.verticalWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(34, 136))
        self.label_5.setStyleSheet(u"font-weight: light;\n"
"color: white;\n"
"")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.label_soles = QLabel(self.verticalWidget)
        self.label_soles.setObjectName(u"label_soles")
        self.label_soles.setMaximumSize(QSize(65, 136))
        self.label_soles.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"")

        self.horizontalLayout_6.addWidget(self.label_soles)


        self.gridLayout_2.addWidget(self.verticalWidget, 1, 0, 1, 1)

        self.verticalWidget_2 = QWidget(self.widget)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalWidget_2.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.verticalWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font-weight: light;\n"
"color: white;\n"
"")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.label_zombies_destruidos = QLabel(self.verticalWidget_2)
        self.label_zombies_destruidos.setObjectName(u"label_zombies_destruidos")
        self.label_zombies_destruidos.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"")

        self.horizontalLayout_9.addWidget(self.label_zombies_destruidos, 0, Qt.AlignLeft)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.verticalWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-weight: light;\n"
"color: white;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.label_zombies_restantes = QLabel(self.verticalWidget_2)
        self.label_zombies_restantes.setObjectName(u"label_zombies_restantes")
        self.label_zombies_restantes.setStyleSheet(u"font-weight: bold;\n"
"color: white;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_zombies_restantes, 0, Qt.AlignLeft)


        self.verticalLayout.addLayout(self.horizontalLayout_10)


        self.gridLayout_2.addWidget(self.verticalWidget_2, 1, 2, 1, 1)


        self.verticalLayout_6.addWidget(self.widget)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addWidget(self.horizontalWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.icono_soles_planta_girasol.setText("")
        self.soles_planta_girasol.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_2.setText("")
        self.icono_soles_planta_clasica.setText("")
        self.soles_planta_clasica.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_3.setText("")
        self.icono_soles_planta_azul.setText("")
        self.soles_planta_azul.setText(QCoreApplication.translate("MainWindow", u"150", None))
        self.label_4.setText("")
        self.icono_soles_planta_papa.setText("")
        self.soles_planta_papa.setText(QCoreApplication.translate("MainWindow", u"75", None))
        self.label_fondo_juego.setText("")
        self.label_planta_10.setText("")
        self.label_planta_11.setText("")
        self.label_planta_19.setText("")
        self.label_planta_6.setText("")
        self.label_planta_9.setText("")
        self.label_planta_4.setText("")
        self.label_planta_13.setText("")
        self.label_planta_18.setText("")
        self.label_planta_1.setText("")
        self.label_planta_20.setText("")
        self.label_planta_8.setText("")
        self.label_planta_14.setText("")
        self.label_planta_3.setText("")
        self.label_planta_12.setText("")
        self.label_planta_2.setText("")
        self.label_planta_5.setText("")
        self.label_planta_7.setText("")
        self.label_planta_15.setText("")
        self.label_planta_17.setText("")
        self.label_planta_16.setText("")
        self.carril_zombie_1.setText("")
        self.carril_zombie_2.setText("")
        self.boton_pausa.setText(QCoreApplication.translate("MainWindow", u"Pausa", None))
        self.boton_avanzar.setText(QCoreApplication.translate("MainWindow", u"Avanzar", None))
        self.boton_iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.boton_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nivel", None))
        self.label_nivel.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Soles", None))
        self.label_soles.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Zombies Destruidos", None))
        self.label_zombies_destruidos.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Zombies Restantes", None))
        self.label_zombies_restantes.setText("")
    # retranslateUi

