#-*- encoding: UTF-8 -*-
import sys, os
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFileDialog
from hjCSS_ui import *

class Form(QtGui.QMainWindow) :
    def __init__(self, parent=None) :
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.file_name = ""

    def ImportFile(self) :
        print >> sys.stderr, "ImportFile"
        self.file_name = QFileDialog.getOpenFileName()
        print >> sys.stderr, self.file_name

    def Scheduling(self) :
        print >> sys.stderr, "Scheduling"
        os.system("./hjCSS " + str(self.file_name) + " 1")

    def AddTask(self) :
        print >> sys.stderr, "AddTask"

    def DeleteTask(self) :
        print >> sys.stderr, "DeleteTask"

if __name__ == '__main__' :
    app = QtGui.QApplication(sys.argv)
    myapp = Form()
    myapp.show()
    app.exec_()
