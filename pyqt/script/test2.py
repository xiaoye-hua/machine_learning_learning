# -*- coding: utf-8 -*-
# @File    : test2.py
# @Author  : Hua Guo
# @Time    : 2019/3/30 下午1:36
# @Disc    :


import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QWidget


# 定义窗口函数window
def window():
    # 我事实上不太明白干嘛要这一句话，只是pyqt窗口的建立都必须调用QApplication方法
    app = QWidget.QApplication(sys.argv)
    # 新建一个窗口，名字叫做w
    w = QWidget.QWidget()
    # 定义w的大小
    w.setGeometry(100, 100, 300, 200)
    # 给w一个Title
    w.setWindowTitle('lesson 2')
    # 在窗口w中，新建一个lable，名字叫做l1
    l1 = QWidget.QLabel(w)
    # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
    png = QtGui.QPixmap('img.jpg')
    # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
    l1.setPixmap(png)

    # 在窗口w中，新建另一个label，名字叫做l2
    l2 = QWidget.QLabel(w)
    # 用open方法打开一个文本文件，并且调用read命令，将其内容读入到file_text中
    file = open('img.log')
    file_text = file.read()
    # 调用setText命令，在l2中显示刚才的内容
    l2.setText(file_text)

    # 调整l1和l2的位置
    l1.move(100, 20)
    l2.move(140, 120)
    # 显示整个窗口
    w.show()
    # 退出整个app
    app.exit(app.exec_())


window()