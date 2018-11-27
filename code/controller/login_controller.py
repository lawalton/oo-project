from PyQt4 import QtGui, QtCore
import sys, os
dirname = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dirname)
from ..view import login

class LoginController(QtGui.QDialog, login.Ui_Dialog):
    """
    Controller to allow a user to login.
    """
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.privs = False
        
        # don't display password
        self.password_input.setEchoMode(QtGui.QLineEdit.Password)
        
        # set up button
        self.login_btn.clicked.connect(self.login_fxn)

    def login_fxn(self):
        """
        Check the validity of the username and password.
        """
        # check that we have all inputs
        if self.username_input.text() == "":
            text = "Please enter a username."
            self.showMessage(text)
            return

        if self.password_input.text() == "":
            text = "Please enter a password."
            self.showMessage(text)
            return

        file_name = dirname + "\passwords.txt"
        file = open(file_name, "r")
        found = False
        for line in file.readlines():
            line = line.replace(" ", "")
            args = line.split(",")
            if args[0] == self.username_input.text():
                # acceptable username, check password
                if args[1] == self.password_input.text():
                    found = True
                    privs = args[2].strip()
                    if privs == "t":
                        # user is an officer, has elevated privileges
                        self.privs = True
                else:
                    text = "Incorrect password"
                    self.showMessage(text)
                    return

        # username not found
        if found == False:
            text = "Username not found."
            self.showMessage(text)
            return

        self.accept()

    def getPrivs(self):
        """
        Return the status of the privileges of the user logging in. Officers have elevated privileges.

        :return: Boolean representing if the user has elevated privileges
        :rtype: bool
        """
        return self.privs

    def showMessage(self, text):
        """
        Displays a pop-up message

        :param str text: the text to be displayed in the pop-up message box
        """
        msgBox = QtGui.QMessageBox();
        msgBox.setText(text);
        msgBox.exec_();

