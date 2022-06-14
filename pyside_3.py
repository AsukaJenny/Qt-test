#!/usr/bin/python

import sys

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QPushButton,QFileDialog
from PySide2.QtCore import Slot
@Slot()
def say_hello():
 print("Button clicked, Hello!")
@Slot()
def do_file():
 fname = QtWidgets.QFileDialog.getOpenFileName(filter = "Excel Files(*.csv;*.xls)")
 print(fname)
 msg = ""
 if fname[1] != 'Excel Files(*.csv;*.xls)':
  msg = " Error! This is not a csv file"
  print(msg)
 else:
  msg = "This is a csv file"
  print (fname[0])
# Create the Qt Application
app = QApplication(sys.argv)
# Create a button, connect it and show it
button = QPushButton("Open the file dialog")
button.clicked.connect(do_file)
button.show()
# Run the main Qt loop
app.exec_()
# from PySide import QtCore,QtGui
#
# def do_file():
#     fname = QtGui.QFileDialog.getOpenFileName()
#     print fname
#
# app = QtGui.QApplication([])
#
# button = QtGui.QPushButton("Test File")
# button.clicked.connect(do_file)
# button.show()
#
# app.exec_()