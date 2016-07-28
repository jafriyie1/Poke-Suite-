import sys
from PyQt4 import QtGui as gui
from PyQt4 import QtCore
from pokedb import PokeDB


class PokeDbGui(gui.QWidget):
    
	def __init__(self):
		super(PokeDbGui, self).__init__()
	    
		self.initUI()
        
        
	def initUI(self):
        
		lbll = gui.QLabel("   Welcome to Joel's Pokemon Database! Which Feature would you like to use?", self)

		r0 = gui.QRadioButton("Create Collection", self)
		r1 = gui.QRadioButton("Insert file into collection", self)
		r2 = gui.QRadioButton("Print document in collection", self)
		r0.move(50,50)
		r1.move(50,100)
		r2.move(50,150)

		r0.toggled.connect(lambda:self.buttonstate(r0))
		r0.clicked.connect(self.radioButtonOne)

		r1.toggled.connect(lambda:self.buttonstate(r1))
		r1.clicked.connect(self.radioButtonTwo)

		r2.toggled.connect(lambda:self.buttonstate(r2))
		r2.clicked.connect(self.radioButtonThree)

		push = gui.QPushButton("About",self)
		push.move(205,200)
		push.toggled.connect(lambda:self.push_button(push))
		push.clicked.connect(self.push_button)

		self.backend = PokeDB()
		self.list_widget = gui.QListWidget()
		self.about = gui.QTextEdit()

		self.setGeometry(300, 300, 500, 250)
		self.center()
		self.setWindowTitle("Joel's PokeDb")
		self.setWindowIcon(gui.QIcon('flygon.png'))        
		self.show()

	def closeEvent(self, event):

		reply = gui.QMessageBox.question(self, 'Quit Message',
			"Are you sure you want to quit?", gui.QMessageBox.Yes | 
			gui.QMessageBox.No, gui.QMessageBox.No)

		if reply == gui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	def center(self):
		frame_geometry = self.frameGeometry()
		screen = gui.QApplication.desktop().screenNumber(gui.QApplication.desktop().cursor().pos())
		centerPoint = gui.QApplication.desktop().screenGeometry(screen).center()
		frame_geometry.moveCenter(centerPoint)
		self.move(frame_geometry.topLeft())

	def buttonstate(self, b):
		if b.isChecked() == True:
			a_string = b.text()+" has been selected"
			gui.QMessageBox.information(self, 'Notification', a_string)

	def radioButtonOne(self):
		user_input, ok = gui.QInputDialog.getText(self, "Create Collection", "Please enter a name for the collection:")
			
		if ok:
			collection_name = (str(user_input))
			# print(type(collection_name))
			self.backend.__init__(collection_name)
			self.backend.collection_creation()
			gui.QMessageBox.information(self, 'Notification', "The collection " + user_input + " has been created") 
			

	def radioButtonTwo(self):
		
		user_input, ok = gui.QInputDialog.getText(self, "Collection Input", "Please type the collection")
		
		if ok:
			collection_name = (str(user_input))
			gui.QMessageBox.information(self, 'Collection Box', "The collection " + user_input + " has been chosen") 
		
			filename = gui.QFileDialog.getOpenFileName(self, "Open file to insert", "/home")
			self.backend.__init__(collection_name)
			self.backend.load_json_file(filename)
			self.backend.insert_to_db()



	def radioButtonThree(self):
		user_input, ok = gui.QInputDialog.getText(self, "Collection Input", "Please type the collection")
		if ok:
			collection_name = (str(user_input))
			gui.QMessageBox.information(self, 'Print documents', "The collection " + user_input + " has been chosen") 	

		self.backend.__init__(collection_name)
		print_list = self.backend.print_content()
		
		for item in print_list:
			item_x = gui.QListWidgetItem(self.list_widget)
			item_x.setText(str(item))
			item_x.setIcon(gui.QIcon('Pokeball.png'))
		
		self.list_widget.setFixedSize(self.list_widget.sizeHintForColumn(0) +\
		 2 * self.list_widget.frameWidth(), self.list_widget.sizeHintForRow(0) * \
		 self.list_widget.count() + 2 * self.list_widget.frameWidth())	
		
		"""self.scrollArea = gui.QScrollArea(self)
		self.scrollArea.setWidgetResizable(True)
		self.scrollAreaWidgetContents = gui.QWidget(self.scrollArea)
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 400))
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)

		self.vertical_layout = gui.QVBoxLayout()


		self.vertical_layout.addWidget(self.scrollArea)
		self.vertical_layout.addWidget(self.list_widget)"""
		self.list_widget.setWindowTitle(collection_name +" contets")
		sb = self.list_widget.verticalScrollBar()
		sb.setValue(sb.maximum())
		self.list_widget.show()

	def push_button(self):
		text = ("Gotta catch em'.... This is a simple applet that" 
				"\ncan be used to add data from the web scrappers" 
				"\n(only scrapping pokemon related websites, duh) and" 
				"\nplace it within the PokeDB (which is a MongoDB database)."
				"\nThis applet can only grow, as more features will be" 
				"\nimplemented in the future.")
		
		self.about.setReadOnly(True)
		self.about.setLineWrapMode(gui.QTextEdit.NoWrap)

		font = self.about.font()
		font.setFamily("Courier")
		font.setPointSize(14)

		self.about.moveCursor(gui.QTextCursor.End)
		self.about.setCurrentFont(font)
		self.about.insertPlainText(text)
		#self.about.insertPlainText(text_two)
		#self.about.insertPlainText(text_three)

		self.about.setWindowTitle("About PokeDB")
		self.about.setGeometry(300, 300, 495, 120)
		sb = self.about.verticalScrollBar()
		sb.setValue(sb.maximum())
		self.about.show()

               
def main():
    
    app = gui.QApplication(sys.argv)
    ex = PokeDbGui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    