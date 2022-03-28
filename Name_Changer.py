# -*- coding:utf-8 -*-

# ======================================================================================================================
# NAME CHANGER
# AUTHOR: SUN
# DESCRIPTION: 主程序
# ======================================================================================================================
import public
from main_window import Ui_Form
from public import *
from PyQt5 import QtCore, QtWidgets
import os

__verson__ = '1.0.0'
# pyinstaller -F -w -i logo.ico Name_Changer.py


class Ui(Ui_Form, QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        self.path = ''
        self.list = name_list()

    def setupUi(self, form):
        super(Ui, self).setupUi(form)
        self.comboBox.addItems(['顺序', '倒序'])
        self.comboBox_2.addItems(['名称+集数', '仅集数'])
        self.pushButton.clicked.connect(self.choose_root)
        self.listWidget.itemClicked.connect(self.click_listwight)
        self.pushButton_6.clicked.connect(self.name_re)
        self.pushButton_8.clicked.connect(self.name_delete)
        self.pushButton_7.clicked.connect(self.name_replace)
        self.pushButton_9.clicked.connect(self.name_line)
        self.pushButton_4.clicked.connect(self.revocation)
        self.pushButton_2.clicked.connect(self.roll_back)
        self.pushButton_5.clicked.connect(self.rename)

    def choose_root(self):
        f = QtWidgets.QFileDialog()
        f.setFileMode(QtWidgets.QFileDialog.Directory)
        f.setFilter(QtCore.QDir.Files)
        if f.exec_():
            p = f.selectedFiles()[0]
            self.label.setText(p)
            self.path = p
            self.listWidget.clear()
            c = []
            for it in os.listdir(p):
                if os.path.isfile(os.path.join(p, it)):
                    self.listWidget.addItem(it)
                    c.append(it)
            self.list.set_org_names(c)

    def click_listwight(self, item):
        text, flag = QtWidgets.QInputDialog.getText(self, 'Name_Changer', '请输入新名称',
                                                    QtWidgets.QLineEdit.Normal, item.text())
        if flag:
            try:
                self.list.change_name(item.text(), text)
                item.setText(text)
            except public.name_change_exception:
                QtWidgets.QMessageBox.critical(self, 'Name_Changer', '出现同名文件！',
                                               QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def name_delete(self):
        try:
            self.listWidget.clear()
            self.listWidget.addItems(self.list.delete_words(self.lineEdit_3.text()))
        except public.name_change_exception:
            QtWidgets.QMessageBox.critical(self, 'Name_Changer', '出现同名文件！',
                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def name_replace(self):
        try:
            self.listWidget.clear()
            self.listWidget.addItems(self.list.replace_words(self.lineEdit_4.text(), self.lineEdit_5.text()))
        except public.name_change_exception:
            QtWidgets.QMessageBox.critical(self, 'Name_Changer', '出现同名文件！',
                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def name_re(self):
        try:
            self.listWidget.clear()
            self.listWidget.addItems(self.list.re_change(self.lineEdit.text(), self.lineEdit_2.text()))
        except public.name_change_exception:
            QtWidgets.QMessageBox.critical(self, 'Name_Changer', '出现同名文件！',
                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def name_line(self):
        self.listWidget.clear()
        order = True
        name = self.lineEdit_6.text()
        if self.comboBox.currentText() == '顺序':
            order = False
        if self.comboBox_2.currentText() == '仅集数':
            self.listWidget.addItems(self.list.list_replace(order))
        else:
            self.listWidget.addItems(self.list.list_replace(order, name))

    def revocation(self):
        self.listWidget.clear()
        self.listWidget.addItems(self.list.revocation())

    def roll_back(self):
        self.listWidget.clear()
        self.listWidget.addItems(self.list.roll_back())

    def rename(self):
        for old, new in dict(zip(self.list.org_name, self.list.last_names)).items():
            os.rename(os.path.join(self.path, old), os.path.join(self.path, new))
        QtWidgets.QMessageBox.information(self, 'Name_Changer', '名称修改完成',
                                          QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui()
    MainWindow.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
