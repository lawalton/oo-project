import sys
from code.view import main_window
from code.view import add_new_member
from code.controller.add_member_controller import *
from code.model.club import *
from code.model.student import *
from PyQt4 import QtGui, QtCore

class App(QtGui.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        
        # TODO - fix later - for proof of concept right now
        self.club = Club("WIC")

        # functionality for adding members
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

def main():
    app = QtGui.QApplication(sys.argv)  
    form = App()                
    form.show()                         
    app.exec_()                         

if __name__ == '__main__':
    main() 
