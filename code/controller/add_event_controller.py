from PyQt4 import QtGui, QtCore
from ..view import add_new_event
from ..model.event import *
from ..model.task import *

class AddNewEvent(QtGui.QDialog, add_new_event.Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.event = None
        # set up buttons
        self.add_event_btn.clicked.connect(self.add_event_fxn)

    def add_event_fxn(self):
        # check that we have all inputs
        if self.event_name_in.text() == "":
            text = "Please enter the event's name."
            self.showMessage(text)
            return

        if not self.event_datetime_in.dateTime():
            text = "Please enter the date and time for the event."
            self.showMessage(text)
            return

        date = self.event_datetime_in.dateTime()
        string_date = date.toString("ddd MMMM d yy")
        self.event = Event(self.event_name_in.text(), string_date )

        if self.task_line_edit_in.toPlainText() != "":
            self.createTasks()

        self.accept()
        
    def createTasks(self):
        tasks = self.task_line_edit_in.toPlainText()
        for task in tasks.splitlines():
            new_task = Task(task, "")
            self.event.addTask(new_task)

    def getEvent(self):
        return self.event

    def showMessage(self, text):
        msgBox = QtGui.QMessageBox();
        msgBox.setText(text);
        msgBox.exec_();




