# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from sys import argv as ar
from sys import exit as ex
from os import curdir as crd
from os.path import abspath as pab
from source import Ui_Dialog
from AlignSource import main_func

# Creating application
app = QtWidgets.QApplication(ar)

# Initialization
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# Logic
way = pab(crd)
file = way + '/tech_file'


def get_sequences():
    if ui.radioButton.isChecked():
        method = 'global'
    else:
        method = 'local'

    m = ui.spinBox.value()
    ms = ui.spinBox_2.value()
    g = ui.spinBox_3.value()

    input_sequences = ui.textEdit.toPlainText()
    with open(file, 'w') as f:
        f.writelines(input_sequences)
    s1, s2, align, idents, gaps, mismatches, drawing_list= main_func(file, m, ms, g, method=method)
    stt = ''
    if len(align) > 50:
        n = 0
        while n < len(align):
            stt += s1[n: n + 50] + '\n'
            stt += align[n: n + 50] + '\n'
            stt += s2[n: n + 50] + '\n\n'
            n += 50
    else:
        stt = s1 + '\n' + align + '\n' + s2
    ui.textBrowser.setText(stt)
    ui.Plot(drawing_list[0], drawing_list[1])

ui.PushButton.clicked.connect(get_sequences)

# Main loop
ex(app.exec_())
