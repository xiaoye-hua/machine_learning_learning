# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final_satellite.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("卫星状态"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 4, 2, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_3.addWidget(self.pushButton_4, 3, 2, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_3.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 2, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.show_image)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("卫星状态", "卫星状态", None))
        self.label_2.setText(_translate("卫星状态", "TextLabel", None))
        self.label_4.setText(_translate("卫星状态", "TextLabel", None))
        self.label_3.setText(_translate("卫星状态", "TextLabel", None))
        self.label.setText(_translate("卫星状态", "TextLabel", None))
        self.pushButton_2.setText(_translate("卫星状态", "Satellite", None))
        self.pushButton_3.setText(_translate("卫星状态", "Satellite", None))
        self.pushButton.setText(_translate("卫星状态", "Satellite 0", None))
        self.pushButton_4.setText(_translate("卫星状态", "Satellite", None))
        self.pushButton_5.setText(_translate("卫星状态", "Satellite", None))

    def show_image(self):
        source = QtCore.QObject.sender(self.centralwidget)
        dir_name = source.text().split(' ')[-1]
        file_path = '../images/' + dir_name + '/'
        print(file_path)
        pixmap1 = QtGui.QPixmap(file_path + "AZ-1.png")
        pixmap1 = pixmap1.scaled(self.label.width(), self.label.height())
        self.label.setPixmap((pixmap1))
        pixmap1 = QtGui.QPixmap(file_path + "CN-1.png")
        pixmap1 = pixmap1.scaled(self.label_2.width(), self.label_2.height())
        self.label_2.setPixmap((pixmap1))
        pixmap1 = QtGui.QPixmap(file_path + "EL-1.png")
        pixmap1 = pixmap1.scaled(self.label_3.width(), self.label_3.height())
        self.label_3.setPixmap((pixmap1))
        pixmap1 = QtGui.QPixmap(file_path + "PR-1.png")
        pixmap1 = pixmap1.scaled(self.label_4.width(), self.label_4.height())
        self.label_4.setPixmap((pixmap1))

app = QtGui.QApplication([])
wget = QtGui.QMainWindow()
form = Ui_MainWindow()
form.setupUi(wget)
wget.show()
# exm = Ui_Form()
# form.show()
app.exec_()
