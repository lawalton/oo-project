# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(83, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.title_label = QtGui.QLabel(self.widget_2)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.horizontalLayout.addWidget(self.title_label)
        spacerItem1 = QtGui.QSpacerItem(82, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.username_label = QtGui.QLabel(self.widget)
        self.username_label.setObjectName(_fromUtf8("username_label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.username_label)
        self.username_input = QtGui.QLineEdit(self.widget)
        self.username_input.setObjectName(_fromUtf8("username_input"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.username_input)
        self.password_label = QtGui.QLabel(self.widget)
        self.password_label.setObjectName(_fromUtf8("password_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.password_label)
        self.password_input = QtGui.QLineEdit(self.widget)
        self.password_input.setObjectName(_fromUtf8("password_input"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.password_input)
        self.verticalLayout.addLayout(self.formLayout)
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(90, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.login_btn = QtGui.QPushButton(self.widget_3)
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.horizontalLayout_2.addWidget(self.login_btn)
        spacerItem3 = QtGui.QSpacerItem(90, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.widget_3)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.title_label.setText(_translate("Dialog", "Club Management System", None))
        self.username_label.setText(_translate("Dialog", "Username:", None))
        self.password_label.setText(_translate("Dialog", "Password:", None))
        self.login_btn.setText(_translate("Dialog", "Login", None))

