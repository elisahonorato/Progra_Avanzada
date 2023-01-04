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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(770, 493)
        MainWindow.setMinimumSize(QSize(770, 493))
        MainWindow.setMaximumSize(QSize(1920, 1200))
        font = QFont()
        font.setFamilies([u"Avenir"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	font: \"Helvetica\";\n"
"}\n"
"QLabel{\n"
"	font: \"Helvetica\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: none;\n"
"}\n"
"\n"
"QWidget#centralwidget{\n"
"	background-color:rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"	background-color: rgba(0, 0, 0,0);\n"
"	border:none;\n"
"	border-radius:none;\n"
"	border-bottom:2px solid rgb(181, 220, 207);\n"
"	color: rgba(255, 255,255, 230);\n"
"	padding-bottom:7px;\n"
"}\n"
"\n"
"\n"
"QFrame#caja{\n"
"	border: 2px solid rgb(233, 0, 126);\n"
"	background-image: none;\n"
"	background: none\n"
"}            \n"
"                \n"
"QPushButton#pushButton{\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:0.471, stop:0 rgba(166, 23, 23, 255), stop:1 rgba(233, 0, 126, 255));\n"
"	border-radius:8px;\n"
"	color: rgba(255, 255, 255,210);\n"
"	padding: 8px;\n"
"}\n"
"QPushButton#pushButton_2{\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:0.471, stop:0 rgba(166, 23, 23, 255), stop:1 rgba(233, 0"
                        ", 126, 255));\n"
"	border-radius:8px;\n"
"	color: rgba(255, 255, 255,210);\n"
"	padding: 8px;\n"
"}\n"
"QPushButton#pushButton_3{\n"
"	background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:0.471, stop:0 rgba(166, 23, 23, 255), stop:1 rgba(233, 0, 126, 255));\n"
"	border-radius:8px;\n"
"	color: rgba(255, 255, 255,210);\n"
"	padding: 8px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 2)
        self.centralwidget_2 = QWidget(self.centralwidget)
        self.centralwidget_2.setObjectName(u"centralwidget_2")
        self.centrarcaja = QHBoxLayout(self.centralwidget_2)
        self.centrarcaja.setSpacing(0)
        self.centrarcaja.setObjectName(u"centrarcaja")
        self.centrarcaja.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget_2)
        self.frame_2.setObjectName(u"frame_2")
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.frame_2.setFont(font1)
        self.frame_2.setStyleSheet(u"background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgb(100,100,100), stop:1 rgb(97, 97, 97))\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.musica3 = QPushButton(self.frame_2)
        self.musica3.setObjectName(u"musica3")
        self.musica3.setMinimumSize(QSize(200, 100))
        self.musica3.setMaximumSize(QSize(600, 600))
        self.musica3.setStyleSheet(u"background-color: rgb(245, 229, 236);\n"
"border-radius: 10px;\n"
"")
        self.musica3.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.musica3, 2, 0, 1, 1)

        self.musica1 = QPushButton(self.frame_2)
        self.musica1.setObjectName(u"musica1")
        self.musica1.setMinimumSize(QSize(200, 100))
        self.musica1.setMaximumSize(QSize(600, 600))
        self.musica1.setStyleSheet(u"background-color: rgb(245, 229, 236);\n"
"border-radius: 10px;\n"
"")
        self.musica1.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.musica1, 1, 0, 1, 1)

        self.img_2 = QLabel(self.frame_2)
        self.img_2.setObjectName(u"img_2")
        self.img_2.setMinimumSize(QSize(0, 0))
        self.img_2.setMaximumSize(QSize(30, 30))
        self.img_2.setPixmap(QPixmap(u"perfil.png"))
        self.img_2.setScaledContents(True)
        self.img_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.img_2, 0, 2, 1, 1)

        self.musica2 = QPushButton(self.frame_2)
        self.musica2.setObjectName(u"musica2")
        self.musica2.setMinimumSize(QSize(200, 100))
        self.musica2.setMaximumSize(QSize(600, 600))
        self.musica2.setStyleSheet(u"background-color: rgb(245, 229, 236);\n"
"border-radius: 10px;\n"
"")
        self.musica2.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.musica2, 1, 1, 1, 1)

        self.label_usuario = QLabel(self.frame_2)
        self.label_usuario.setObjectName(u"label_usuario")
        self.label_usuario.setMaximumSize(QSize(16777215, 30))
        self.label_usuario.setStyleSheet(u"background-color: none;")
        self.label_usuario.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_usuario, 0, 1, 1, 1)

        self.musica4 = QPushButton(self.frame_2)
        self.musica4.setObjectName(u"musica4")
        self.musica4.setMinimumSize(QSize(200, 100))
        self.musica4.setMaximumSize(QSize(600, 600))
        self.musica4.setStyleSheet(u"background-color: rgb(245, 229, 236);\n"
"border-radius: 10px;\n"
"")
        self.musica4.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.musica4, 2, 1, 1, 1)


        self.centrarcaja.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(265, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Avenir"])
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setItalic(False)
        self.label.setFont(font2)

        self.horizontalLayout.addWidget(self.label)

        self.img = QLabel(self.frame)
        self.img.setObjectName(u"img")
        self.img.setMinimumSize(QSize(0, 0))
        self.img.setMaximumSize(QSize(30, 30))
        self.img.setPixmap(QPixmap(u"amigos.png"))
        self.img.setScaledContents(True)
        self.img.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.img)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 237, 336))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea.setWidget(self.widget)

        self.verticalLayout.addWidget(self.scrollArea)


        self.centrarcaja.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.centralwidget_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 85))
        self.frame_3.setMaximumSize(QSize(16777215, 85))
        self.frame_3.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_caratula = QLabel(self.frame_3)
        self.label_caratula.setObjectName(u"label_caratula")
        self.label_caratula.setMinimumSize(QSize(60, 60))
        self.label_caratula.setMaximumSize(QSize(60, 60))
        self.label_caratula.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_caratula.setScaledContents(True)
        self.label_caratula.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_caratula)

        self.label_state = QLabel(self.frame_3)
        self.label_state.setObjectName(u"label_state")
        self.label_state.setMaximumSize(QSize(300, 16777215))
        self.label_state.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_state)

        self.button_anterior = QPushButton(self.frame_3)
        self.button_anterior.setObjectName(u"button_anterior")
        self.button_anterior.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u"anterior.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_anterior.setIcon(icon)
        self.button_anterior.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.button_anterior)

        self.button_play = QPushButton(self.frame_3)
        self.button_play.setObjectName(u"button_play")
        self.button_play.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u"play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_play.setIcon(icon1)
        self.button_play.setIconSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.button_play)

        self.button_siguiente = QPushButton(self.frame_3)
        self.button_siguiente.setObjectName(u"button_siguiente")
        self.button_siguiente.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u"siguiente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_siguiente.setIcon(icon2)
        self.button_siguiente.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.button_siguiente)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(300, 16777215))
        self.label_13.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(60, 60))
        self.label_14.setMaximumSize(QSize(60, 60))
        self.label_14.setStyleSheet(u"")
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_14)


        self.verticalLayout_2.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pantalla Principal", None))
#if QT_CONFIG(tooltip)
        self.frame_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.musica3.setText(QCoreApplication.translate("MainWindow", u"Nombre musica", None))
        self.musica1.setText(QCoreApplication.translate("MainWindow", u"Nombre musica", None))
        self.img_2.setText("")
        self.musica2.setText(QCoreApplication.translate("MainWindow", u"Nombre musica", None))
        self.label_usuario.setText(QCoreApplication.translate("MainWindow", u"Nombre Usuario", None))
        self.musica4.setText(QCoreApplication.translate("MainWindow", u"Nombre musica", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Otros usuarios", None))
        self.img.setText("")
        self.label_caratula.setText("")
        self.label_state.setText("")
        self.button_anterior.setText("")
        self.button_play.setText("")
        self.button_siguiente.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
    # retranslateUi

