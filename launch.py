import sys
from code.view import main_window
from code.view import add_new_member
from code.controller.add_member_controller import *
from code.controller.add_event_controller import *
from code.model.club import *
from code.model.student import *
from code.model.event import *
from PyQt4 import QtGui, QtCore

class App(QtGui.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        
        # TODO - fix later - for proof of concept right now
        self.club = Club("WIC")

        # functionality for adding members
        self.m_dialog = AddNewMember()
        self.add_member_btn.clicked.connect(self.add_member_clicked)
        self.member_list_model = QtGui.QStandardItemModel(self.member_list_view)
        self.member_list_view.setModel(self.member_list_model)
        self.member_list_view.show()

         # functionality for adding events
        self.e_dialog = AddNewEvent()
        self.add_event_btn.clicked.connect(self.add_event_clicked)
        self.event_list_model = QtGui.QStandardItemModel(self.event_list_view)
        self.event_list_view.setModel(self.event_list_model)
        self.event_list_view.show()

    def add_member_clicked(self):
        self.m_dialog.show()
        if self.m_dialog.exec_():
            new_member = self.m_dialog.getMember()
            self.club.addMember(new_member)
            self.member_list_model.appendRow(QtGui.QStandardItem(new_member.getName()))

    def add_event_clicked(self):
        self.e_dialog.show()
        if self.e_dialog.exec_():
            new_event = self.e_dialog.getEvent()
            self.club.addEvent(new_event)
            self.event_list_model.appendRow(QtGui.QStandardItem(new_event.getName()))

def main():
    app = QtGui.QApplication(sys.argv)  
    form = App()                
    form.show()                         
    app.exec_()                         

if __name__ == '__main__':
    main() 
