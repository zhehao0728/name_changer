# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 520)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 35, 411, 478))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 501, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(520, 6, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(430, 30, 161, 101))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 141, 77))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_6)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 140, 161, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 141, 51))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.pushButton_8 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_8)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(430, 220, 161, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 141, 77))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_7)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(430, 330, 161, 121))
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_4)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(9, 16, 141, 103))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget_4)
        self.comboBox.setObjectName("comboBox")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget_4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.pushButton_9 = QtWidgets.QPushButton(self.formLayoutWidget_4)
        self.pushButton_9.setObjectName("pushButton_9")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_9)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(430, 460, 160, 54))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Name_Changer"))
        self.pushButton.setText(_translate("Form", "选择文件"))
        self.groupBox.setTitle(_translate("Form", "正则表达式"))
        self.label_2.setText(_translate("Form", "关键词"))
        self.label_3.setText(_translate("Form", "新形式"))
        self.pushButton_6.setText(_translate("Form", "预览"))
        self.groupBox_2.setTitle(_translate("Form", "删除"))
        self.label_4.setText(_translate("Form", "关键词"))
        self.pushButton_8.setText(_translate("Form", "预览"))
        self.groupBox_3.setTitle(_translate("Form", "替换"))
        self.label_5.setText(_translate("Form", "关键词"))
        self.label_6.setText(_translate("Form", "替换为"))
        self.pushButton_7.setText(_translate("Form", "预览"))
        self.groupBox_4.setTitle(_translate("Form", "按序命名"))
        self.label_7.setText(_translate("Form", "序列"))
        self.label_8.setText(_translate("Form", "方式"))
        self.pushButton_9.setText(_translate("Form", "预览"))
        self.label_9.setText(_translate("Form", "名称"))
        self.pushButton_2.setText(_translate("Form", "恢复"))
        self.pushButton_4.setText(_translate("Form", "撤销"))
        self.pushButton_5.setText(_translate("Form", "确认"))
