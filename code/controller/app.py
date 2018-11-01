import sys
sys.path.append("..")
from ..view import add_member
from PyQt4 import QtGui, QtCore

#class App(QtGui.QMainWindow, main_window.Ui_MainWindow):
class App(QtGui.QMainWindow, add_member.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)  
    form = App()                
    form.show()                         
    app.exec_()                         

if __name__ == '__main__':
    main() 