import sys
import main_window
from PyQt4 import QtGui, QtCore

class App(QtGui.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)  
    form = App()                
    form.show()                         
    app.exec_()                         


if __name__ == '__main__':              # if we're running file directly and not importing it
    main() 