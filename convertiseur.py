# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convertiseur.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 370)
        MainWindow.setMinimumSize(QtCore.QSize(500, 370))
        MainWindow.setMaximumSize(QtCore.QSize(500, 370))
        MainWindow.setStyleSheet("background-color: rgb(26, 95, 180);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(31, 161, 73, 29))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(31, 221, 91, 29))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.devise = QtWidgets.QLineEdit(self.centralwidget)
        self.devise.setGeometry(QtCore.QRect(150, 160, 261, 26))
        self.devise.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.devise.setObjectName("devise")
        self.montant = QtWidgets.QLineEdit(self.centralwidget)
        self.montant.setGeometry(QtCore.QRect(150, 220, 261, 26))
        self.montant.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.montant.setObjectName("montant")
        self.btn_convertir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_convertir.setGeometry(QtCore.QRect(200, 290, 151, 41))
        self.btn_convertir.setStyleSheet("background-color: rgb(0, 140, 102);\n"
"color: rgb(255, 255, 255);")
        self.btn_convertir.setObjectName("btn_convertir")
        self.resultat = QtWidgets.QLabel(self.centralwidget)
        self.resultat.setGeometry(QtCore.QRect(120, 80, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.resultat.setFont(font)
        self.resultat.setText("")
        self.resultat.setObjectName("resultat")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Convertiseur de device"))
        self.label.setText(_translate("MainWindow", "Convertiseur de device EURO/CFA"))
        self.label_2.setText(_translate("MainWindow", "Devise"))
        self.label_3.setText(_translate("MainWindow", "Montant"))
        self.btn_convertir.setText(_translate("MainWindow", "Convertir"))



