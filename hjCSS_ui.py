# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hjCSS.ui'
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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(663, 511)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setEnabled(True)
        self.splitter.setGeometry(QtCore.QRect(1, 37, 661, 401))
        self.splitter.setFrameShape(QtGui.QFrame.NoFrame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ImportButton = QtGui.QPushButton(self.layoutWidget)
        self.ImportButton.setObjectName(_fromUtf8("ImportButton"))
        self.horizontalLayout_2.addWidget(self.ImportButton)
        self.SchedulingButton = QtGui.QPushButton(self.layoutWidget)
        self.SchedulingButton.setObjectName(_fromUtf8("SchedulingButton"))
        self.horizontalLayout_2.addWidget(self.SchedulingButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.AddButton = QtGui.QPushButton(self.layoutWidget)
        self.AddButton.setAutoFillBackground(False)
        self.AddButton.setFlat(False)
        self.AddButton.setObjectName(_fromUtf8("AddButton"))
        self.horizontalLayout_3.addWidget(self.AddButton)
        self.DeleteButton = QtGui.QPushButton(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(236, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.DeleteButton.setPalette(palette)
        self.DeleteButton.setObjectName(_fromUtf8("DeleteButton"))
        self.horizontalLayout_3.addWidget(self.DeleteButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tableView = QtGui.QTableView(self.layoutWidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout_2.addWidget(self.tableView)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.RMButton = QtGui.QRadioButton(self.layoutWidget1)
        self.RMButton.setObjectName(_fromUtf8("RMButton"))
        self.buttonGroup = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.RMButton)
        self.horizontalLayout_4.addWidget(self.RMButton)
        self.EDFButton = QtGui.QRadioButton(self.layoutWidget1)
        self.EDFButton.setObjectName(_fromUtf8("EDFButton"))
        self.buttonGroup.addButton(self.EDFButton)
        self.horizontalLayout_4.addWidget(self.EDFButton)
        self.UserButton = QtGui.QRadioButton(self.layoutWidget1)
        self.UserButton.setObjectName(_fromUtf8("UserButton"))
        self.buttonGroup.addButton(self.UserButton)
        self.horizontalLayout_4.addWidget(self.UserButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tableView_2 = QtGui.QTableView(self.layoutWidget1)
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))
        self.verticalLayout_3.addWidget(self.tableView_2)
        self.AvgDialog = QtGui.QLabel(self.layoutWidget1)
        self.AvgDialog.setObjectName(_fromUtf8("AvgDialog"))
        self.verticalLayout_3.addWidget(self.AvgDialog)
        self.WorstDialog = QtGui.QLabel(self.layoutWidget1)
        self.WorstDialog.setObjectName(_fromUtf8("WorstDialog"))
        self.verticalLayout_3.addWidget(self.WorstDialog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHjCSS_CPU_Scheduling_Simulator = QtGui.QMenu(self.menubar)
        self.menuHjCSS_CPU_Scheduling_Simulator.setObjectName(_fromUtf8("menuHjCSS_CPU_Scheduling_Simulator"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuHjCSS_CPU_Scheduling_Simulator.addSeparator()
        self.menubar.addAction(self.menuHjCSS_CPU_Scheduling_Simulator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.ImportButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.ImportFile)
        QtCore.QObject.connect(self.SchedulingButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.Scheduling)
        QtCore.QObject.connect(self.AddButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.AddTask)
        QtCore.QObject.connect(self.DeleteButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.DeleteTask)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ImportButton.setText(_translate("MainWindow", "Import", None))
        self.SchedulingButton.setText(_translate("MainWindow", "Scheduling", None))
        self.AddButton.setText(_translate("MainWindow", "Add", None))
        self.AddButton.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.DeleteButton.setText(_translate("MainWindow", "Delete", None))
        self.RMButton.setText(_translate("MainWindow", "RM", None))
        self.EDFButton.setText(_translate("MainWindow", "EDF", None))
        self.UserButton.setText(_translate("MainWindow", "User", None))
        self.AvgDialog.setText(_translate("MainWindow", "Avg Response Time : ", None))
        self.WorstDialog.setText(_translate("MainWindow", "Worst response Time : ", None))
        self.menuHjCSS_CPU_Scheduling_Simulator.setTitle(_translate("MainWindow", "hjCSS (CPU Scheduling Simulator)", None))
