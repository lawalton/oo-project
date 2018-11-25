# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'event_details.ui'
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
        Dialog.resize(597, 587)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(219, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.event_details_label = QtGui.QLabel(self.widget_2)
        self.event_details_label.setObjectName(_fromUtf8("event_details_label"))
        self.horizontalLayout.addWidget(self.event_details_label)
        spacerItem1 = QtGui.QSpacerItem(219, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.event_name_label = QtGui.QLabel(self.widget)
        self.event_name_label.setObjectName(_fromUtf8("event_name_label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.event_name_label)
        self.event_name_edit = QtGui.QLineEdit(self.widget)
        self.event_name_edit.setObjectName(_fromUtf8("event_name_edit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.event_name_edit)
        self.event_time_label = QtGui.QLabel(self.widget)
        self.event_time_label.setObjectName(_fromUtf8("event_time_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.event_time_label)
        self.event_time_edit = QtGui.QLineEdit(self.widget)
        self.event_time_edit.setObjectName(_fromUtf8("event_time_edit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.event_time_edit)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.task_list_label = QtGui.QLabel(self.widget)
        self.task_list_label.setObjectName(_fromUtf8("task_list_label"))
        self.horizontalLayout_3.addWidget(self.task_list_label)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.task_list_view = QtGui.QListWidget(self.widget)
        self.task_list_view.setObjectName(_fromUtf8("task_list_view"))
        self.verticalLayout.addWidget(self.task_list_view)
        self.complete_task_btn = QtGui.QPushButton(self.widget)
        self.complete_task_btn.setObjectName(_fromUtf8("complete_task_btn"))
        self.verticalLayout.addWidget(self.complete_task_btn)
        self.assign_task_btn = QtGui.QPushButton(self.widget)
        self.assign_task_btn.setObjectName(_fromUtf8("assign_task_btn"))
        self.verticalLayout.addWidget(self.assign_task_btn)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.member_list_label = QtGui.QLabel(self.widget)
        self.member_list_label.setObjectName(_fromUtf8("member_list_label"))
        self.horizontalLayout_4.addWidget(self.member_list_label)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.member_list_view = QtGui.QListWidget(self.widget)
        self.member_list_view.setObjectName(_fromUtf8("member_list_view"))
        self.verticalLayout_2.addWidget(self.member_list_view)
        self.member_attended_btn = QtGui.QPushButton(self.widget)
        self.member_attended_btn.setObjectName(_fromUtf8("member_attended_btn"))
        self.verticalLayout_2.addWidget(self.member_attended_btn)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem6 = QtGui.QSpacerItem(209, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.save_btn = QtGui.QPushButton(self.widget_3)
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        self.horizontalLayout_6.addWidget(self.save_btn)
        spacerItem7 = QtGui.QSpacerItem(209, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.event_details_label.setText(_translate("Dialog", "Event Details", None))
        self.event_name_label.setText(_translate("Dialog", "Event Name:", None))
        self.event_time_label.setText(_translate("Dialog", "Event Time and Date:", None))
        self.task_list_label.setText(_translate("Dialog", "Task List", None))
        self.complete_task_btn.setText(_translate("Dialog", "Mark Task Completed", None))
        self.assign_task_btn.setText(_translate("Dialog", "Assign Task to Member", None))
        self.member_list_label.setText(_translate("Dialog", "Member List", None))
        self.member_attended_btn.setText(_translate("Dialog", "Mark Member as Attended", None))
        self.save_btn.setText(_translate("Dialog", "Save Details", None))

