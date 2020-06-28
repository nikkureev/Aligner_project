# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Aligner\source.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 500)
        self.PushButton = QtWidgets.QPushButton(Dialog)
        self.PushButton.setGeometry(QtCore.QRect(10, 217, 85, 30))
        self.PushButton.setObjectName("PushButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 500, 200))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 250, 500, 200))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFontFamily("Consolas")
        self.textBrowser.setFont(QtGui.QFont("Consolas", 7))
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(600, 10, 80, 30))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(600, 37, 80, 30))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setChecked(True)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(600, 70, 60, 40))
        self.spinBox.setMinimum(-99)
        self.spinBox.setProperty("value", 2)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(600, 120, 60, 40))
        self.spinBox_2.setMinimum(-99)
        self.spinBox_2.setProperty("value", -1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setGeometry(QtCore.QRect(600, 170, 60, 40))
        self.spinBox_3.setMinimum(-99)
        self.spinBox_3.setProperty("value", -1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(670, 70, 47, 25))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(670, 120, 100, 25))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(670, 170, 47, 25))
        self.label_3.setObjectName("label_3")

        # Drawing graph
        self.figure = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.axis("off")
        self.plot_widget = QtWidgets.QWidget(Dialog)
        self.plot_widget.setGeometry(520, 210, 250, 250)
        plot_box = QtWidgets.QVBoxLayout()
        plot_box.addWidget(self.canvas)
        self.plot_widget.setLayout(plot_box)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def Plot(self, x, y):
        self.ax.clear()
        self.ax.plot(x, y)
        self.canvas.draw()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Aligner 2000"))
        self.PushButton.setText(_translate("Dialog", "Submit"))
        self.radioButton.setText(_translate("Dialog", "Global"))
        self.radioButton_2.setText(_translate("Dialog", "Local"))
        self.label.setText(_translate("Dialog", "Match"))
        self.label_2.setText(_translate("Dialog", "Mismatch"))
        self.label_3.setText(_translate("Dialog", "Gap"))
