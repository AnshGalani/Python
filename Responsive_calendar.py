from PyQt5.QtWidgets import*
from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import*
from PyQt5.QtCore import*
import sys

class window(QMainWindow):
    def __init__(self):
        super( ).__init__()
        #setting title
        self.setWindowTitle("CREATING BY ANSH")
        #setting geometry
        self .setGeometry(100,100,600,400)
        #calling method
        self.UiComponents()
        #showing all the widgets
        self.show()
    
#method for componets
    def UiComponents(self):
        #creating a QCalendarWidget object
        calender=QCalendarWidget(self)
        #setting geometry to the calender
        calender.setGeometry(10,10,400,250)
        #creating push button
        push=QPushButton("Next Year",self)
        #setting geometry to the push
        push.setGeometry(120,280,100,40)
        #adding action to the push
        push.clicked.connect(lambda: do_action())
        def do_action():
            #showing next year
            calender.showNextYear()

# creating pyqt5 app

App=QApplication(sys.argv)

#creating the instance od our windown
window = window()

#start the app
sys.exit(App.exec())