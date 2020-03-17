# -*- coding: utf-8 -*-
# @File    : PushButton.py
# @Author  : Hua Guo
# @Time    : 2019/3/30 下午1:53
# @Disc    :


import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.color = QtGui.QColor(0, 0, 0)



        self.red = QtGui.QPushButton('Red', self)
        self.red.setCheckable(True)
        self.red.move(10, 10)

        self.connect(self.red, QtCore.SIGNAL('clicked()'), self.setColor)

        self.green = QtGui.QPushButton('Green', self)
        self.green.setCheckable(True)
        self.green.move(10, 60)

        self.connect(self.green, QtCore.SIGNAL('clicked()'), self.setColor)

        self.blue = QtGui.QPushButton('Blue', self)
        self.blue.setCheckable(True)
        self.blue.move(10, 110)

        self.connect(self.blue, QtCore.SIGNAL('clicked()'), self.setColor)

        self.square = QtGui.QWidget(self)
        self.square.setGeometry(150, 20, 100, 100)

        self.square.setStyleSheet("QWidget { background-color: %s }" %
            self.color.name())

        self.setWindowTitle('ToggleButton')
        self.setGeometry(0, 0, 3000, 3000)


    def setColor(self):

        source = self.sender()

        if source.text() == "Red":
            if self.red.isChecked():
                # self.color.setRed(255)
                hbox = QtGui.QHBoxLayout(self)
                pixmap = QtGui.QPixmap("img.png")

                label = QtGui.QLabel(self)
                label.setPixmap(pixmap)

                hbox.addWidget(label)
                self.setLayout(hbox)

                self.setWindowTitle("image_red")
                self.move(0, 0)
            # else:
            #     self.color.setRed(0)

        elif source.text() == "Green":
            if self.green.isChecked():
                hbox = QtGui.QHBoxLayout(self)
                pixmap = QtGui.QPixmap("img.png")

                label = QtGui.QLabel(self)
                label.setPixmap(pixmap)

                hbox.addWidget(label)
                self.setLayout(hbox)

                self.setWindowTitle("image_green")
                self.move(0, 0)

        else:
            if self.blue.isChecked():
                self.color.setBlue(255)
            else: self.color.setBlue(0)

        self.square.setStyleSheet("QWidget { background-color: %s }" %
            self.color.name())



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()