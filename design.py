# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'korzinochka.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1054, 728)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.WheelFocus)
        MainWindow.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(95, 198, 203, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(98, 203, 163, 255), stop:1 rgba(255, 255, 255, 255));\n"
"text-decoration: underline;\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(800, 670, 171, 41))
        self.label_2.setStyleSheet("font: 12pt \"Matura MT Script Capitals\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(98, 203, 163, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.label_2.setObjectName("label_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setGeometry(QtCore.QRect(30, 80, 371, 581))
        self.treeWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 246, 246, 246), stop:1 rgba(255, 255, 255, 255));\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border-width: 8px;\n"
"border-style: outset;\n"
"border-color: beige;\n"
"padding: 5px")
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.selectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectBtn.setEnabled(True)
        self.selectBtn.setGeometry(QtCore.QRect(30, 20, 371, 51))
        self.selectBtn.setAutoFillBackground(False)
        self.selectBtn.setStyleSheet("font: 20pt \"Mistral\";\n"
"border-radius: 10px;\n"
"border-width: 6px;\n"
"border-style: outset;\n"
"border-color: beige;\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.selectBtn.setObjectName("selectBtn")
        self.runBtn = QtWidgets.QPushButton(self.centralwidget)
        self.runBtn.setEnabled(True)
        self.runBtn.setGeometry(QtCore.QRect(440, 20, 141, 51))
        self.runBtn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"text-decoration: underline;\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.runBtn.setObjectName("runBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setEnabled(True)
        self.stopBtn.setGeometry(QtCore.QRect(580, 20, 131, 51))
        self.stopBtn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.stopBtn.setObjectName("stopBtn")
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setEnabled(True)
        self.clearBtn.setGeometry(QtCore.QRect(860, 20, 151, 51))
        self.clearBtn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.clearBtn.setObjectName("clearBtn")
        self.listWidget = QtWidgets.QTextBrowser(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(445, 81, 571, 581))
        self.listWidget.setMouseTracking(True)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 246, 246, 246), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 670, 161, 41))
        self.label_3.setStyleSheet("font: 12pt \"Matura MT Script Capitals\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(98, 203, 163, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige")
        self.label_3.setObjectName("label_3")
        self.refreshBtn = QtWidgets.QPushButton(self.centralwidget)
        self.refreshBtn.setGeometry(QtCore.QRect(710, 20, 151, 51))
        self.refreshBtn.setStyleSheet("font: 20pt \"Mistral\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"border-width: 4px;\n"
"border-style: outset;\n"
"border-color: beige\n"
"")
        self.refreshBtn.setObjectName("refreshBtn")
        self.Check = QtWidgets.QPushButton(self.centralwidget)
        self.Check.setGeometry(QtCore.QRect(40, 670, 161, 41))
        self.Check.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Check.setObjectName("Check")
        self.Uncheck = QtWidgets.QPushButton(self.centralwidget)
        self.Uncheck.setGeometry(QtCore.QRect(220, 670, 171, 41))
        self.Uncheck.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(84, 203, 9, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Uncheck.setObjectName("Uncheck")
        self.selectBtn.raise_()
        self.runBtn.raise_()
        self.stopBtn.raise_()
        self.clearBtn.raise_()
        self.label_2.raise_()
        self.treeWidget.raise_()
        self.listWidget.raise_()
        self.label_3.raise_()
        self.refreshBtn.raise_()
        self.Check.raise_()
        self.Uncheck.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Vlaeria Basov"))
        self.selectBtn.setText(_translate("MainWindow", "Select Files"))
        self.runBtn.setText(_translate("MainWindow", "Run"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.clearBtn.setText(_translate("MainWindow", "Clear"))
        self.label_3.setText(_translate("MainWindow", "Iliya Livshets"))
        self.refreshBtn.setText(_translate("MainWindow", "Refresh"))
        self.Check.setText(_translate("MainWindow", "check All"))
        self.Uncheck.setText(_translate("MainWindow", "Uncheck"))
