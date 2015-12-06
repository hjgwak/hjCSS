#-*- encoding: UTF-8 -*-
import sys, os
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from hjCSS_ui import *

def getInitialModel() :
    model = QStandardItemModel()
    model.setColumnCount(8)
    headerNames = ["TaskName", "Periodic", "Start_time", "Request_time", \
                    "Period", "Task_Count", "Deadline", "Priority"]
    model.setHorizontalHeaderLabels(headerNames)

    return model

def getInitialResultModel() :
    model = QStandardItemModel()
    model.setColumnCount(4)
    headerNames = ["Time", "taskName", "Status", "OnTime"]
    model.setHorizontalHeaderLabels(headerNames)

    return model

def setFileTable(form) :
    _file = open(form.file_name, 'r')
    magic = True
    for line in _file.readlines() :
        line = line.rstrip('\r\n')
        items = line.split(' ')

        if len(items) < 8 :
            magic = False
            QMessageBox.about(form, "Incorrect Inputfile!", "Incorrect Inputfile!\n(Arguments Missing!)")
            break
        elif len(items) > 8 :
            magic = False
            QMessageBox.about(form, "Incorrect Inputfile!", "Incorrect Inputfile!\n(Too many arguments!)")
            break

        new_row = []
        for item in items :
            new_item = QStandardItem(item)
            #new_item.setEditable(False)
            new_row.append(new_item)
        form.cur_model.appendRow(new_row)
    _file.close()
    if magic :
        form.ui.tableView.setModel(form.cur_model)

def setResultTable(form) :
    _file = open('output.txt', 'r')
    for line in _file.readlines() :
        line = line.rstrip('\r\n')
        
        if line[0] == '#' :
            if line.startswith('#Avg: ') :
                avg = line.split(' ')[1]
                new_label = "Avg Response Time : " + avg
                form.ui.AvgDialog.setText(new_label)
            elif line.startswith('#Worst: ') :
                worst = line.split(' ')[1]
                new_label = "Worst response Time : " + worst
                form.ui.WorstDialog.setText(new_label)
            elif line.startswith('#OnTime/total: ') :
                ontime = line.split(' ')[1]
                new_label = "OnTime / total : " + ontime
                form.ui.OnTimeDialog.setText(new_label)
        else :
            items = line.split('\t')

            new_row = []
            colored = False
            brush = ""
            if items[-1] == 'False' :
                colored = True
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            elif items[-1] == 'True' :
                colored = True
                brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
            elif items[-2] == 'add.' :
                colored = True
                brush = QtGui.QBrush(QtGui.QColor(54, 137, 251))

            for item in items :
                new_item = QStandardItem(item)
                new_item.setEditable(False)
                if colored :
                    new_item.setBackground(brush)
                new_row.append(new_item)
            form.cur_result_model.appendRow(new_row)
    _file.close()
    form.ui.tableView_2.setModel(form.cur_result_model)

class Form(QtGui.QMainWindow) :
    def __init__(self, parent=None) :
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.file_name = ""
        self.checked_button = -1
        self.cur_model = getInitialModel()
        self.cur_result_model = getInitialResultModel()
        self.ui.tableView.setModel(self.cur_model)
        self.ui.tableView.setColumnWidth(2, 85)
        self.ui.tableView.setColumnWidth(3, 90)
        self.ui.tableView.setColumnWidth(4, 85)
        self.ui.tableView.setColumnWidth(6, 85)
        self.ui.tableView.setColumnWidth(7, 85)
        self.ui.tableView_2.setModel(self.cur_result_model)
        self.ui.tableView_2.setColumnWidth(0, 60)
        self.ui.tableView_2.setColumnWidth(1, 230)
        self.ui.tableView_2.setColumnWidth(2, 220)
        self.ui.tableView_2.setColumnWidth(3, 220)
        #self.leftWidth = 480
        #self.rightWidth = 800 - self.leftWidth
        #self.ui.splitter.setSizes([self.leftWidth, self.rightWidth])

    def ImportFile(self) :
        print >> sys.stderr, "ImportFile"
        self.file_name = QFileDialog.getOpenFileName()
        print >> sys.stderr, self.file_name
        self.cur_model = getInitialModel()
        setFileTable(self)

    def Scheduling(self) :
        print >> sys.stderr, "Scheduling"
        self.checked_button = self.ui.buttonGroup.checkedId();
        
        if self.cur_model.rowCount() == 0 :
            QMessageBox.about(self, "No Input", "Input data does not exist!")
            return ;
        elif self.checked_button == -1 :
            QMessageBox.about(self, "Incorrect Mode", "Scheduling mode does not selected!")
            return ;

        o_file = open('input.txt', 'w')
        for i in range(self.cur_model.rowCount()) :
            items = self.cur_model.takeRow(i)
            data = [str(item.text()) for item in items]
            o_file.write(' '.join(data) + '\n')
            self.cur_model.insertRow(i, items)
        o_file.close()
        print >> sys.stderr, "./hjCSS input.txt " + str(self.checked_button) + " > output.txt"
        os.system("./hjCSS input.txt " + str(self.checked_button) + " > output.txt")
        self.cur_result_model = getInitialResultModel()
        setResultTable(self)

    def AddTask(self) :
        print >> sys.stderr, "AddTask"
        new_row = []
        for i in range(8) :
            new_item = QStandardItem("")
            new_row.append(new_item)
        self.cur_model.appendRow(new_row)
        self.ui.tableView.setModel(self.cur_model)

    def DeleteTask(self) :
        print >> sys.stderr, "DeleteTask"
        indexes = self.ui.tableView.selectionModel().selectedRows()
        for index in indexes :
            self.cur_model.removeRows(index.row(), 1)

if __name__ == '__main__' :
    app = QtGui.QApplication(sys.argv)
    myapp = Form()
    myapp.show()
    app.exec_()
