import sys
from code.view import main_window
from code.view import add_new_member
from code.model.club import *
from code.model.student import *
from PyQt4 import QtGui, QtCore

class App(QtGui.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        
        # TODO - fix later - for proof of concept right now
        self.club = Club("WIC")

        self.dialog = AddNewMember()
        self.add_member_btn.clicked.connect(self.add_member_clicked)
        self.member_list_model = QtGui.QStandardItemModel(self.member_list_view)
        self.member_list_view.setModel(self.member_list_model)
        self.member_list_view.show()

    def add_member_clicked(self):
        self.dialog.show()
        if self.dialog.exec_():
            new_member = self.dialog.getMember()
            self.club.addMember(new_member)
            self.member_list_model.appendRow(QtGui.QStandardItem(new_member.getName()))

class AddNewMember(QtGui.QDialog, add_new_member.Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.member = None
        # set up buttons
        self.add_member_btn.clicked.connect(self.add_member_fxn)

        # Add stuff to combo box
        school_years = ["Freshman", "Sophomore", "Junior", "Senior", "Other"]
        for item in school_years:
            self.year_combo_box.addItem(item)

    def add_member_fxn(self):
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

        if self.officer_checkbox.isChecked():
            self.member = Officer(self.name_input.text(), self.year_combo_box.currentText());
            self.member.setPosition(self.position_entry.text())
            self.member.setNumEventsHelped(int(self.num_events_input.text()))
        else:
            self.member = Member(self.name_input.text(), self.year_combo_box.currentText());
            self.member.setNumEventsAttended(int(self.num_events_input.text()))

        self.accept()
        
        # TODO - only for proof of concept purpose - remove later
        #self.club.addMember(new_member)
        #text = self.name_input.text() + " has been added!"
        #numMembers = self.club.getNumMembers();
        #clubName = self.club.getName();
        #text += "\n" + clubName + " has " + str(numMembers) + " members:\n"
        #members = self.club.getListOfMembers()
        #for member in members:
        #    text += " " + member.getName() + ""
        #self.showMessage(text)
    def getMember(self):
        return self.member

    def showMessage(self, text):
        msgBox = QtGui.QMessageBox();
        msgBox.setText(text);
        msgBox.exec_();


def main():
    app = QtGui.QApplication(sys.argv)  
    form = App()                
    form.show()                         
    app.exec_()                         

if __name__ == '__main__':
    main() 
