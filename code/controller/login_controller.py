from PyQt4 import QtGui, QtCore
from ..view import login

class Login(QtGui.QDialog, login.Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        
        # don't display password
        self.password_input.setEchoMode(QtGui.QLineEdit.Password)
        
        # set up button
        self.login_btn.clicked.connect(self.login_fxn)

    def login_fxn(self):
        # check that we have all inputs
        if self.username_input.text() == "":
            text = "Please enter a username."
            self.showMessage(text)
            return

        if self.password_input.text() == "":
            text = "Please enter a password."
            self.showMessage(text)
            return

        #TODO add functionality to check info

        self.accept()

    def showMessage(self, text):
        msgBox = QtGui.QMessageBox();
        msgBox.setText(text);
        msgBox.exec_();

