# -*- coding: utf-8 -*-
# @File    : test1.py
# @Author  : Hua Guo
# @Time    : 2019/3/30 上午11:33
# @Disc    :
#!/usr/bin/python

# simple.py

from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap("img.png")

        label = QtGui.QLabel(self)
        label.setPixmap(pixmap)

        hbox.addWidget(label)
        self.setLayout(hbox)

        self.setWindowTitle("image")
        self.move(0, 0)


def main():

    app = QtGui.QApplication([])
    exm = Example()
    exm.show()
    app.exec_()
if __name__ == '__main__':
    main()