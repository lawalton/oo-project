from PyQt4 import QtGui, QtCore
from ..view import add_new_member
from ..model.student import *
from ..model.studentfactory import *

class AddNewMemberController(QtGui.QDialog, add_new_member.Ui_Dialog):
    """
    Controller for creating a new member.
    """
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.member = None

        # create Factory 
        self.studentFactory = StudentFactory()

        # set up buttons
        self.add_member_btn.clicked.connect(self.add_member_fxn)

        # Add stuff to combo box
        school_years = ["Freshman", "Sophomore", "Junior", "Senior", "Other"]
        for item in school_years:
            self.year_combo_box.addItem(item)

    def add_member_fxn(self):
        """
        Slot for the "Add New Member" button. Run when the user clicks the button, creates
        a new member based on user inputs.
        """
        # check that we have all inputs
        if self.name_input.text() == "":
            text = "Please enter the student's name."
            self.showMessage(text)
            return

        if self.year_combo_box.currentIndex() < 0:
            text = "Please enter the student's academic year."
            self.showMessage(text)
            return

        if self.num_events_input.text() == "":
            text = "Please enter how many events the student has attended."
            self.showMessage(text)
            return

        # get inputs
        name = self.name_input.text()
        year = self.year_combo_box.currentText()
        num_events = int(self.num_events_input.text())
        args = [num_events]
        if self.officer_checkbox.isChecked():
            type = "officer"
            args.append(self.position_entry.text())

        else:
            type = "member"

        self.member = self.studentFactory.getStudent(type, name, year, args)
        self.accept()

    def getMember(self):
        """
        Returns the new member created by the user

        :return: the new member
        :rtype: Student
        """
        return self.member

    def showMessage(self, text):
        """
        Displays a pop-up message

        :param str text: the text to be displayed in the pop-up message box
        """
        msgBox = QtGui.QMessageBox();
        msgBox.setText(text);
        msgBox.exec_();
