import sys 
from PyQt4 import QtGui as gui

def main():
	# Create an PyQT4 application object.
	app = gui.QApplication(sys.argv)       
	 
	# The QWidget widget is the base class of all user interface objects in PyQt4.
	w = gui.QWidget()
	 
	# Set window size. 
	w.resize(320, 240)
	 
	# Set window title  
	w.setWindowTitle("PokeDb") 
	 
	# Show window
	w.show() 
	 
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()

