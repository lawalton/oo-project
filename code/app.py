import sys
from code.view import main_window
from code.view import add_new_member
from code.view import login
from code.controller.add_member_controller import *
from code.controller.add_event_controller import *
from code.controller.login_controller import *
from code.controller.event_details_controller import *
from code.model.club import *
from code.model.student import *
from code.model.event import *
from PyQt4 import QtGui, QtCore

class App(QtGui.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
       
        self.club = Club("name")
        self.hide()
        my_login = Login()
        if my_login.exec_() == QtGui.QDialog.Accepted:
            self.show()
            self.privs = my_login.getPrivs()

        #logout button
        self.logout_btn.clicked.connect(self.logout_fxn)

        # Assign privileges to current user

        if not self.privs:
            # user doesn't have privileges to add new members or events
            self.add_member_btn.hide()
            self.add_event_btn.hide()

        # functionality for adding members
        self.m_dialog = AddNewMember()
        self.add_member_btn.clicked.connect(self.add_member_clicked)
        self.member_list_model = QtGui.QStandardItemModel(self.member_list_view)
        self.member_list_view.setModel(self.member_list_model)
        self.member_list_view.show()
        self.view_member_btn.clicked.connect(self.view_member_clicked)

         # functionality for adding events
        self.e_dialog = AddNewEvent()
        self.add_event_btn.clicked.connect(self.add_event_clicked)
        self.event_list_model = QtGui.QStandardItemModel(self.event_list_view)
        self.event_list_view.setModel(self.event_list_model)
        self.event_list_view.show()
        self.view_event_btn.clicked.connect(self.view_event_clicked)

    def add_member_clicked(self):
        self.m_dialog.show()
        if self.m_dialog.exec_():
            new_member = self.m_dialog.getMember()
            self.club.addMember(new_member)
            self.member_list_model.appendRow(QtGui.QStandardItem(new_member.getName()))

    def view_member_clicked(self):
        # get selected member
        members = self.member_list_view.selectedIndexes()
        if len(members) == 0:
            text = "Please select a member."
            self.showMessage(text)
            return
        if len(members) > 1:
            text = "Please select only one member."
            self.showMessage(text)
            return

        member_name = members[0].data()
        member = self.club.findMember(member_name)
        self.showMessage(member.getInfo())

    def showMessage(self, text):
        msgBox = QtGui.QMessageBox();
        msgBox.setText(text);
        msgBox.exec_();

    def add_event_clicked(self):
        self.e_dialog.show()
        if self.e_dialog.exec_():
            new_event = self.e_dialog.getEvent()
            self.club.addEvent(new_event)
            self.event_list_model.appendRow(QtGui.QStandardItem(new_event.getName()))

    def view_event_clicked(self):
        # get selected event
        events = self.event_list_view.selectedIndexes()
        if len(events) == 0:
            text = "Please select an event."
            self.showMessage(text)
            return
        if len(events) > 1:
            text = "Please select only one event."
            self.showMessage(text)
            return

        event_name = events[0].data()
        event = self.club.findEvent(event_name)
        self.details_dialog = EventDetails(event, self.club)
        self.details_dialog.show()
        if self.details_dialog.exec_():
            edited_event = self.details_dialog.getEvent()
            # find original event and update
            updated = self.club.updateEvent(event_name, edited_event)
            if not updated:
                text = "Error: unable to update event"
                self.showMessage(text)
            updated_members = self.details_dialog.getUpdatedMembers()
            if len(updated_members) > 0:
                for updated_member in updated_members:
                    self.club.updateMember(updated_member)

    def logout_fxn(self):
        self.hide()
        my_login = Login()
        if my_login.exec_() == QtGui.QDialog.Accepted:
            self.show()
            self.privs = my_login.getPrivs()

