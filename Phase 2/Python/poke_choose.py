from PyQt4 import QtGui as gui
from PyQt4 import QtCore
from OpenFiles import OpenImageFiles
import sys
from numpy import array
import numpy as np
import pickle
from sklearn import svm


class PokeChoose(gui.QWidget):
	"""Class for the execution of the 
	gui application. Inherits from QWidget"""
	def __init__(self):
		super(PokeChoose, self).__init__()
	    
		self.initUI()
        
        
	def initUI(self):
		"""Constructor of subclass"""
		# Label
		blank = gui.QLabel(" ", self)
		lbll = gui.QLabel("   Welcome to PokeChoose! Please select button below.", self)

		# Creation of radio buttons and events associated with them
		r0 = gui.QRadioButton("Pick file for guess", self)

		r0.move(90,50)

		r0.clicked.connect(self.radioButtonOne)

		push = gui.QPushButton("About",self)
		push.move(125,100)
		
		push.clicked.connect(self.push_button)

		self.setGeometry(225, 320, 335, 150)
		self.about = gui.QTextEdit()
		self.show()
		f = open("poke_svm_trained.pkl" ,"rb+")
		self.f = f
		self.trained_svm = pickle.load(self.f)
		self.f.close()

		self.setWindowTitle("Joel's PokeChoose")
		self.setWindowIcon(gui.QIcon('Mienshao.png'))   

	def radioButtonOne(self):
		"""Method for radio button one"""
		# Gets user input from the prompt
			
		# Opens a file dialog to select the file
		filename = gui.QFileDialog.getOpenFileName(self, "Open .jpg file to insert", "/Users")
		
		# filename is now the absolute path of the selected file
		# And is loaded and inserted into the backend of the program
		
		test_pic = OpenImageFiles(filename)
		test_data = test_pic.getSingleFile()
		nx, ny = test_data.shape
		pred = self.trained_svm.predict(test_data.reshape(nx*ny))[0]
		
		if pred == 1: 
			gui.QMessageBox.information(self, 'Prediction', "The Image is a Pokemon!")

		elif pred == 0:
			gui.QMessageBox.information(self, 'Prediction', "The Image is not a Pokemon! Try again :-)")
		

	

	def push_button(self):
		"""Method for about button"""
		# Text literal 
		text = ("This is a simple application that uses a Support Vector" 
				"\nMachine algorithm to see if the picture is a pokemon or not.")
		
		self.about.setReadOnly(True)
		self.about.setLineWrapMode(gui.QTextEdit.NoWrap)

		# Sets font and family
		font = self.about.font()
		font.setFamily("Courier")
		font.setPointSize(14)

		# Sets font and passes the string text as an
		# argument to the insertPlainText method
		self.about.moveCursor(gui.QTextCursor.End)
		self.about.setCurrentFont(font)
		self.about.insertPlainText(text)
		
		# Sets title, size, and implements a scroll bar 
		# for the window
		self.about.setWindowTitle("About PokeChoose")
		self.about.setGeometry(300, 300, 495, 120)
		sb = self.about.verticalScrollBar()
		sb.setValue(sb.maximum())
		self.about.show()


def main():	
	"""Main function"""
	app = gui.QApplication(sys.argv)
	ex = PokeChoose()
	p = ex.palette()
	p.setColor(ex.backgroundRole(), gui.QColor.fromRgb(196,134,212))
	ex.setPalette(p)
	sys.exit(app.exec_())


if __name__ == '__main__':
    main() 
    
		