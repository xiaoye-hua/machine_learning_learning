# -*- coding: utf-8 -*-
# @File    : hellow_world.py
# @Author  : Hua Guo
# @Time    : 2019/3/30 上午9:15
# @Disc    :

import sys
import PyQt4
from PyQt4.QtGui import *
print(dir(PyQt4.QtCore))
print(dir(PyQt4.QtGui))
app = QApplication(sys.argv)
button = QPushButton("Hello World", None)
button.show()
app.exec_()