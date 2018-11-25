from PyQt4 import QtGui, QtCore
from ..view import event_details
from ..model.event import *
from ..model.task import *

class EventDetails(QtGui.QDialog, event_details.Ui_Dialog):
    def __init__(self, event, club):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.event = event
        self.club = club
        self.updatedMembers = []

        self.populate_details()

        # set up buttons
        self.complete_task_btn.clicked.connect(self.complete_task_fxn)
        self.assign_task_btn.clicked.connect(self.assign_task_fxn)
        self.member_attended_btn.clicked.connect(self.member_attended_fxn)
        self.save_btn.clicked.connect(self.save_fxn)

    def populate_details(self):
        self.event_name_edit.setText(self.event.getName())
        self.event_time_edit.setText(self.event.getDate())

        self.display_members()
        self.display_tasks()

    def display_members(self):
        # get list of members
        for member in self.club.getListOfMembers():
            text = member.getName()
            if self.event.getName() in member.getEvents():
                text += " - " + member.getEventString()
            self.member_list_view.addItem(text)

    def display_tasks(self):
        # get list of tasks
        for task in self.event.getTasks():
            text = task.getName()
            if task.getAssignee() is not None:
                text += " - assigned to " + str(task.getAssignee().getName())
            if task.getIsComplete():
                text += " - completed"
            
            self.task_list_view.addItem(text)

    def complete_task_fxn(self):
        # get selected task
        sel_tasks = self.task_list_view.selectedItems()
        if len(sel_tasks) == 0:
            text = "Please select a task."
            self.showMessage(text)
            return
        if len(sel_tasks) > 1:
            text = "Please select only one task."
            self.showMessage(text)
            return

        for task in sel_tasks:
            task.setText(task.text() + ' - completed')
            task_object = self.event.findTask(task.text().split("-")[0].strip())
            task_object.setIsComplete(True)

    def member_attended_fxn(self):
        sel_member = self.member_list_view.selectedItems()
        if len(sel_member) == 0:
            text = "Please select a member."
            self.showMessage(text)
            return
        if len(sel_member) > 1:
            text = "Please select only one member."
            self.showMessage(text)
            return

        for member in sel_member:
            member_object = self.club.findMember(member.text().split("-")[0].strip())
            member.setText(member.text() + ' - ' + member_object.getEventString())
            member_object.addEvent(self.event.getName())
            member_object.eventAttended()
            self.updatedMembers.append(member_object)

    def assign_task_fxn(self):
        sel_member = self.member_list_view.selectedItems()
        if len(sel_member) == 0:
            text = "Please select a member."
            self.showMessage(text)
            return
        if len(sel_member) > 1:
            text = "Please select only one member."
            self.showMessage(text)
            return

        sel_tasks = self.task_list_view.selectedItems()
        if len(sel_tasks) == 0:
            text = "Please select a task."
            self.showMessage(text)
            return
        if len(sel_tasks) > 1:
            text = "Please select only one task."
            self.showMessage(text)
            return

        member = sel_member[0]
        task = sel_tasks[0]
        member_object = self.club.findMember(member.text().split("-")[0].strip())
        task_object = self.event.findTask(task.text().split("-")[0].strip())
        task_object.setAssignee(member_object)
        task.setText(task.text() + ' - assigned to ' + member_object.getName())

       
    def getEvent(self):
        return self.event

    def getUpdatedMembers(self):
        return self.updatedMembers

    def save_fxn(self):
        for task in self.event.getTasks():
            text = task.getName() + " - " + str(task.getIsComplete())
        self.accept()

    def showMessage(self, text):
        msgBox = QtGui.QMessageBox();
        msgBox.setText(text);
        msgBox.exec_();







