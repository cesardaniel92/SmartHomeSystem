import sys
from PyQt4 import QtGui, QtCore
import json
import datetime
import matplotlib.pyplot as plt
import pandas as pd
from dataAnalysis import*
# Module to get the canvas to draw the polt on
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas


class Window(QtGui.QWidget):
    
    #super return the parent object. in this case it's QMainWindow
    def __init__(self):
	super(Window, self).__init__()
	#set the postion and the size of the window
        self.setGeometry(300, 300, 800, 500)
	#set the title
        self.setWindowTitle("Data Analysis")
	
	grid = QtGui.QGridLayout()
	self.setLayout(grid)

	#buttons
	button1 = QtGui.QPushButton("Show last 24 hour data", self)
	button1.resize(button1.sizeHint())
        button1.clicked.connect(plot1)
	grid.addWidget(button1, 2,0)
	
	button2 = QtGui.QPushButton("Show last month data", self)
	button2.resize(button2.sizeHint())
        button2.clicked.connect(plot2)
	grid.addWidget(button2, 2,1)

	button3 = QtGui.QPushButton("Show last 3 month data", self)
	button3.resize(button3.sizeHint())
        button3.clicked.connect(plot3)
	grid.addWidget(button3, 3,0)
	
        button4 = QtGui.QPushButton("Show last year", self)
	button4.resize(button4.sizeHint())
        button4.clicked.connect(plot4)
	grid.addWidget(button4, 3,1)

	self.figure = plt.figure(figsize=(15,10))
	self.canvas = FigureCanvas(self.figure)
	grid.addWidget(self.canvas, 1, 0, 1, 2)
	
	self.show()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
   

