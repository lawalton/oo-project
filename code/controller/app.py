#import sys, os
#sys.path.append("..")
#file_dir = os.path.dirname(__file__)
#sys.path.append(file_dir)
#from ..view import add_member
#from ..view import main_window
#from clubview import *
#from ..model.club import *
#from ..model.student import *
#from ..model.event import *
#from PyQt4 import QtGui, QtCore

#class App(QtGui.QMainWindow, main_window.Ui_MainWindow):
#    def __init__(self):
#        super(self.__class__, self).__init__()
#        self.setupUi(self)
#        self.widget = ClubView()

#class App(QtGui.QMainWindow, add_member.Ui_MainWindow):
#    def __init__(self):
#        super(self.__class__, self).__init__()
#        self.setupUi(self)

#        # set up buttons
#        self.add_member_btn.clicked.connect(self.add_member_fxn)

#        # Add stuff to combo box
#        school_years = ["Freshman", "Sophomore", "Junior", "Senior", "Other"]
#        for item in school_years:
#            self.year_combo_box.addItem(item)

#        # TODO - fix later - for proof of concept right now
#        self.club = Club("WIC");

#    def add_member_fxn(self):
#        # check that we have all inputs
#        if self.name_input.text() == "":
#            text = "Please enter the student's name."
#            self.showMessage(text)
#            return

#        if self.year_combo_box.currentIndex() < 0:
#            text = "Please enter the student's academic year."
#            self.showMessage(text)
#            return

#        if self.num_events_input.text() == "":
#            text = "Please enter how many events the student has attended."
#            self.showMessage(text)
#            return

#        if self.officer_checkbox.isChecked():
#            new_member = Officer(self.name_input.text(), self.year_combo_box.currentText());
#            new_member.setPosition(self.position_entry.text())
#            new_member.setNumEventsHelped(int(self.num_events_input.text()))
#        else:
#            new_member = Member(self.name_input.text(), self.year_combo_box.currentText());
#            new_member.setNumEventsAttended(int(self.num_events_input.text()))
        
#        # TODO - only for proof of concept purpose - remove later
#        self.club.addMember(new_member)
#        text = self.name_input.text() + " has been added!"
#        numMembers = self.club.getNumMembers();
#        clubName = self.club.getName();
#        text += "\n" + clubName + " has " + str(numMembers) + " members:\n"
#        members = self.club.getListOfMembers()
#        for member in members:
#            text += " " + member.getName() + ""
#        self.showMessage(text)

#    def showMessage(self, text):
#        msgBox = QtGui.QMessageBox();
#        msgBox.setText(text);
#        msgBox.exec_();

#def main():
#    app = QtGui.QApplication(sys.argv)  
#    form = App()                
#    form.show()                         
#    app.exec_()                         

#if __name__ == '__main__':
#    main() 