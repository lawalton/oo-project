# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_member.ui'
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
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
        self.verticalLayout.addWidget(self.widget_3)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.name_label = QtGui.QLabel(self.widget_2)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.name_label)
        self.name_input = QtGui.QLineEdit(self.widget_2)
        self.name_input.setObjectName(_fromUtf8("name_input"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.name_input)
        self.year_label = QtGui.QLabel(self.widget_2)
        self.year_label.setObjectName(_fromUtf8("year_label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.year_label)
        self.year_combo_box = QtGui.QComboBox(self.widget_2)
        self.year_combo_box.setObjectName(_fromUtf8("year_combo_box"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.year_combo_box)
        self.officer_label = QtGui.QLabel(self.widget_2)
        self.officer_label.setObjectName(_fromUtf8("officer_label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.officer_label)
        self.officer_checkbox = QtGui.QCheckBox(self.widget_2)
        self.officer_checkbox.setObjectName(_fromUtf8("officer_checkbox"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.officer_checkbox)
        self.position_label = QtGui.QLabel(self.widget_2)
        self.position_label.setObjectName(_fromUtf8("position_label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.position_label)
        self.position_entry = QtGui.QLineEdit(self.widget_2)
        self.position_entry.setObjectName(_fromUtf8("position_entry"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.position_entry)
        self.num_events_label = QtGui.QLabel(self.widget_2)
        self.num_events_label.setObjectName(_fromUtf8("num_events_label"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.num_events_label)
        self.num_events_input = QtGui.QLineEdit(self.widget_2)
        self.num_events_input.setObjectName(_fromUtf8("num_events_input"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.num_events_input)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.add_member_btn = QtGui.QPushButton(self.widget_2)
        self.add_member_btn.setObjectName(_fromUtf8("add_member_btn"))
        self.verticalLayout.addWidget(self.add_member_btn)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.add_member_title_label.setText(_translate("MainWindow", "Add New Member", None))
        self.name_label.setText(_translate("MainWindow", "Name:", None))
        self.year_label.setText(_translate("MainWindow", "Year in School:", None))
        self.officer_label.setText(_translate("MainWindow", "Officer?", None))
        self.officer_checkbox.setText(_translate("MainWindow", "Yes", None))
        self.position_label.setText(_translate("MainWindow", "Position:", None))
        self.num_events_label.setText(_translate("MainWindow", "Number of events attended:", None))
        self.add_member_btn.setText(_translate("MainWindow", "Add Member", None))

