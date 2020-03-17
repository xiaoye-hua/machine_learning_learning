# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'satilite.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        self.gridLayout = QtGui.QGridLayout(Satelite)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ul = QtGui.QLabel(Satelite)
        self.ul.setObjectName(_fromUtf8("ul"))
        self.gridLayout.addWidget(self.ul, 0, 6, 1, 1)
        self.bl = QtGui.QLabel(Satelite)
        self.bl.setObjectName(_fromUtf8("bl"))
        self.gridLayout.addWidget(self.bl, 0, 5, 1, 1)
        self.ur = QtGui.QLabel(Satelite)
        self.ur.setObjectName(_fromUtf8("ur"))
        self.gridLayout.addWidget(self.ur, 1, 5, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(Satelite)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 1, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(Satelite)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(Satelite)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Satelite)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.br = QtGui.QLabel(Satelite)
        self.br.setObjectName(_fromUtf8("br"))
        self.gridLayout.addWidget(self.br, 1, 6, 1, 1)

        self.retranslateUi(Satelite)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ul.show)
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

app = QtGui.QApplication([])
wget = QtGui.QWidget()
form = Ui_Satelite()
form.setupUi(wget)
wget.show()
# exm = Ui_Form()
# form.show()
app.exec_()
