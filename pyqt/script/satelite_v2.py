# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'satilite.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Satelite(object):
    def setupUi(self, Satelite):
        Satelite.setObjectName(_fromUtf8("Satelite"))
        Satelite.resize(821, 530)
        self.ul = QtGui.QLabel(Satelite)
        self.ul.setGeometry(QtCore.QRect(570, 20, 200, 200))
        self.ul.setObjectName(_fromUtf8("ul"))

        self.bl = QtGui.QLabel(Satelite)
        self.bl.setGeometry(QtCore.QRect(320, 20, 200, 200))
        self.bl.setObjectName(_fromUtf8("bl"))
        self.ur = QtGui.QLabel(Satelite)
        self.ur.setGeometry(QtCore.QRect(320, 260, 200, 200))
        self.ur.setObjectName(_fromUtf8("ur"))
        self.pushButton_4 = QtGui.QPushButton(Satelite)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 170, 85, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton = QtGui.QPushButton(Satelite)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 85, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(Satelite)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 170, 85, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_2 = QtGui.QPushButton(Satelite)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 120, 85, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.br = QtGui.QLabel(Satelite)
        self.br.setGeometry(QtCore.QRect(570, 260, 200, 200))
        self.br.setObjectName(_fromUtf8("br"))

        self.retranslateUi(Satelite)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.show_s1)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ur.show)
        QtCore.QMetaObject.connectSlotsByName(Satelite)

    def retranslateUi(self, Satelite):
        Satelite.setWindowTitle(_translate("Satelite", "Form", None))
        self.ul.setText(_translate("Satelite", "TextLabel", None))
        self.bl.setText(_translate("Satelite", "TextLabel", None))
        self.ur.setText(_translate("Satelite", "TextLabel", None))
        self.pushButton_4.setText(_translate("Satelite", "S4", None))
        self.pushButton.setText(_translate("Satelite", "S1", None))
        self.pushButton_3.setText(_translate("Satelite", "S3", None))
        self.pushButton_2.setText(_translate("Satelite", "S2", None))
        self.br.setText(_translate("Satelite", "TextLabel", None))
    def show_s1(self):
        self.ul.setScaledContents(True)
        self.ul.setPixmap(QPixmap("../images/0/AZ-1.png"))
        self.ur.setScaledContents(True)
        self.ur.setPixmap(QPixmap("../images/0/CN-1.png"))
        self.bl.setScaledContents(True)
        self.bl.setPixmap(QPixmap("../images/0/EL-1.png"))
        self.br.setScaledContents(True)
        self.br.setPixmap(QPixmap("../images/0/PR-1.png"))



app = QtGui.QApplication([])
wget = QtGui.QWidget()
form = Ui_Satelite()
form.setupUi(wget)
wget.show()
# exm = Ui_Form()
# form.show()
app.exec_()
