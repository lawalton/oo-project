# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_new_event.ui'
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
        Dialog.resize(809, 632)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.widget_2 = QtGui.QWidget(Dialog)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout = QtGui.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(129, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.add_member_title_label = QtGui.QLabel(self.widget_3)
        self.add_member_title_label.setObjectName(_fromUtf8("add_member_title_label"))
        self.horizontalLayout_2.addWidget(self.add_member_title_label)
        spacerItem1 = QtGui.QSpacerItem(295, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.event_name_label = QtGui.QLabel(self.widget_2)
        self.event_name_label.setObjectName(_fromUtf8("event_name_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.event_name_label)
        self.event_name_in = QtGui.QLineEdit(self.widget_2)
        self.event_name_in.setObjectName(_fromUtf8("event_name_in"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.event_name_in)
        self.date_time_label = QtGui.QLabel(self.widget_2)
        self.date_time_label.setObjectName(_fromUtf8("date_time_label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.date_time_label)
        self.event_datetime_in = QtGui.QDateTimeEdit(self.widget_2)
        self.event_datetime_in.setObjectName(_fromUtf8("event_datetime_in"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.event_datetime_in)
        self.tasks_label = QtGui.QLabel(self.widget_2)
        self.tasks_label.setObjectName(_fromUtf8("tasks_label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.tasks_label)
        self.task_line_edit_in = QtGui.QPlainTextEdit(self.widget_2)
        self.task_line_edit_in.setObjectName(_fromUtf8("task_line_edit_in"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.task_line_edit_in)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.add_event_btn = QtGui.QPushButton(self.widget_2)
        self.add_event_btn.setObjectName(_fromUtf8("add_event_btn"))
        self.gridLayout.addWidget(self.add_event_btn, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.add_member_title_label.setText(_translate("Dialog", "Add New Event", None))
        self.event_name_label.setText(_translate("Dialog", "Name:", None))
        self.date_time_label.setText(_translate("Dialog", "Date and Time:", None))
        self.tasks_label.setText(_translate("Dialog", "Tasks:", None))
        self.add_event_btn.setText(_translate("Dialog", "Add Event", None))

