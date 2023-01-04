# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_ranking.ui'
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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

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
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(150, 100, 150, -1)
        self.boton_volver = QPushButton(self.centralwidget)
        self.boton_volver.setObjectName(u"boton_volver")
        self.boton_volver.setStyleSheet(u"background-color: rgb(0,150,0);\n"
"color: white;\n"
"border-radius: rounded 3px")
        self.boton_volver.setFlat(False)

        self.verticalLayout_6.addWidget(self.boton_volver)


        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icono_sol = QLabel(self.centralwidget)
        self.icono_sol.setObjectName(u"icono_sol")
        self.icono_sol.setEnabled(True)
        self.icono_sol.setMinimumSize(QSize(20, 20))
        self.icono_sol.setMaximumSize(QSize(100, 100))
        self.icono_sol.setAutoFillBackground(False)
        self.icono_sol.setFrameShape(QFrame.NoFrame)
        self.icono_sol.setTextFormat(Qt.RichText)
        self.icono_sol.setScaledContents(True)
        self.icono_sol.setMargin(10)

        self.horizontalLayout_2.addWidget(self.icono_sol)

        self.texto_ranking = QLabel(self.centralwidget)
        self.texto_ranking.setObjectName(u"texto_ranking")

        self.horizontalLayout_2.addWidget(self.texto_ranking)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boton_volver.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.icono_sol.setText("")
        self.texto_ranking.setText(QCoreApplication.translate("MainWindow", u"Ranking", None))
    # retranslateUi

