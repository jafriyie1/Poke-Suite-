"""Joel's PokeDB Application"""
"""I will later need to optimize the code
and make the methods a lot shorter"""
import sys
from PyQt4 import QtGui as gui
from PyQt4 import QtCore
from pokedb import PokeDB


class PokeDbGui(gui.QWidget):
	"""Class for the execution of the
	gui application. Inherits from QWidget"""
	def __init__(self):
		super(PokeDbGui, self).__init__()

		self.initUI()


	def initUI(self):
		"""Constructor of subclass"""
		# Label
		blank = gui.QLabel(" ", self)
		lbll = gui.QLabel("    Welcome to Joel's Pokemon Database! Which Feature would you like to use?", self)

		# Creation of radio buttons and events associated with them
		r0 = gui.QRadioButton("Create Collection", self)
		r1 = gui.QRadioButton("Insert File Into Collection", self)
		r2 = gui.QRadioButton("Print Document In Collection", self)
		r3 = gui.QRadioButton("Delete Collection From Database", self)
		r4 = gui.QRadioButton("Print Collection Names", self)
		r5 = gui.QRadioButton("Query From Collection", self)
		r6 = gui.QRadioButton("Insert Query Into a file", self)
		r7 = gui.QRadioButton("Insert Values Into Collection", self)

		r0.move(50,50)
		r4.move(50,100)
		r1.move(50,150)
		r2.move(50,200)
		r3.move(50,250)
		r5.move(50,300)
		r6.move(50,350)
		r7.move(50,400)

		r0.toggled.connect(lambda:self.buttonstate(r0))
		r0.clicked.connect(self.radioButtonOne)

		r1.toggled.connect(lambda:self.buttonstate(r1))
		r1.clicked.connect(self.radioButtonTwo)

		r2.toggled.connect(lambda:self.buttonstate(r2))
		r2.clicked.connect(self.radioButtonThree)

		r3.toggled.connect(lambda:self.buttonstate(r3))
		r3.clicked.connect(self.radioButtonFour)

		r4.toggled.connect(lambda:self.buttonstate(r4))
		r4.clicked.connect(self.radioButtonFive)

		r5.toggled.connect(lambda:self.buttonstate(r5))
		r5.clicked.connect(self.radioButtonSix)

		r6.toggled.connect(lambda:self.buttonstate(r6))
		r6.clicked.connect(self.radioButtonSeven)

		r7.toggled.connect(lambda:self.buttonstate(r7))
		r7.clicked.connect(self.radioButtonEight)

		# Creation of About button and event associated with it
		push = gui.QPushButton("About",self)
		push.move(205,430)
		push.toggled.connect(lambda:self.push_button(push))
		push.clicked.connect(self.push_button)

		# Declarations and assignments from the PokeDB, QListWidget, QTextEdit, QCloseEvent
		# Class. PokeDB deals with the backend of the application
		self.backend = PokeDB()
		self.list_widget = gui.QListWidget()
		self.temp_widget = gui.QListWidget()
		self.about = gui.QTextEdit()

		# Creation of the main window
		self.setGeometry(225, 320, 479, 480)
		self.center()
		self.setWindowTitle("Joel's PokeDb")
		self.setWindowIcon(gui.QIcon('flygon.png'))
		self.show()

	def closeEvent(self, event):
		"""Override Method that deals with the closing of the application"""
		# Displays message box
		reply = gui.QMessageBox.question(self, 'Quit Message',
			"Are you sure you want to quit?", gui.QMessageBox.Yes |
			gui.QMessageBox.No, gui.QMessageBox.No)

		# Closes application if yes
		if reply == gui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	"""def closeEvent(self):
		print("the window will close")"""

	def center(self):
		"""Method that centers the application"""
		frame_geometry = self.frameGeometry()
		screen = gui.QApplication.desktop().screenNumber(gui.QApplication.desktop().cursor().pos())
		centerPoint = gui.QApplication.desktop().screenGeometry(screen).center()
		frame_geometry.moveCenter(centerPoint)
		self.move(frame_geometry.topLeft())

	def buttonstate(self, b):
		"""Method that displays a messagebox on which button was clicked"""
		if b.isChecked() == True:
			a_string = b.text()+" has been selected"
			gui.QMessageBox.information(self, 'Notification', a_string)

	def radioButtonOne(self):
		"""Method for radio button one"""
		# Gets user input from the prompt
		user_input, ok = gui.QInputDialog.getText(self, "Create Collection", "Please enter a name for the collection:")

		# If the user selects ok then create collection
		if ok:
			collection_name = (str(user_input))
			# Takes the user_input and puts into the constructor
			# Of the backend class
			self.backend.__init__(collection_name)
			self.backend.collection_creation()
			# Notifies user that the collection was created
			gui.QMessageBox.information(self, 'Notification', "The collection " + user_input + " has been created")


	def radioButtonTwo(self):
		"""Method for radio button two"""
		# Gets user input from the prompt
		user_input, ok = gui.QInputDialog.getText(self, "Collection Input", "Please type the collection")

		if ok:
			collection_name = (str(user_input))
			# Notifies user that the collection was created
			gui.QMessageBox.information(self, 'Collection Box', "The collection " + user_input + " has been chosen")

			# Opens a file dialog to select the file
			filename = gui.QFileDialog.getOpenFileName(self, "Open JSON file to insert", "/Users")
			self.backend.__init__(collection_name)
			# filename is now the absolute path of the selected file
			# And is loaded and inserted into the backend of the program
			self.backend.load_json_file(filename)
			self.backend.insert_to_db()



	def radioButtonThree(self):
		"""Method for radio button three"""
		# Asks for user input
		user_input, ok = gui.QInputDialog.getText(self, "Collection Input", "Please type the collection")
		if ok:
			collection_name = (str(user_input))
			# Displays message box that the collection has been selected
			gui.QMessageBox.information(self, 'Print documents', "The collection " + user_input + " has been chosen")

		# The users input is then passed as an argument into
		# the backend constructor
		self.backend.__init__(collection_name)
		# Print list is then declared and assigned to
		# the returned list from the backend method print_content()
		print_list = self.backend.print_content()

		# This for loop creates a new QListWidgetItem for every
		# document (in this case item) in the list
		for item in print_list:
			item_x = gui.QListWidgetItem(self.list_widget)
			item_x.setText(str(item))
			item_x.setIcon(gui.QIcon('Pokeball.png'))

		# Sets size of window
		self.list_widget.setGeometry(300,300,1200,75)
		# Sets the title of the window and displays the window
		self.list_widget.setWindowTitle(collection_name +" contents")
		sb = self.list_widget.verticalScrollBar()
		sb.setValue(sb.maximum())
		self.list_widget.show()
		"""Slight bug. Will be fixed later"""
		user_input, ok = gui.QInputDialog.getText(self, "Collection Input", \
										"Move window to look at contents. Click OK to clear when finished, or click on cancel to interact with the window")
		if ok:
			self.list_widget.clear()

	def radioButtonFour(self):
		"""Method for radio button four"""
		# Asks for user input
		user_input, ok = gui.QInputDialog.getText(self, "Collection Input", "Please type the collection")
		if ok:
			reply = gui.QMessageBox.question(self, 'Collection Removal',
			"Are you sure you want to remove the collection?", gui.QMessageBox.Yes |
			gui.QMessageBox.No, gui.QMessageBox.No)

			# Removes collection if yes
			if reply == gui.QMessageBox.Yes:
				collection_name = (str(user_input))
				self.backend.__init__(collection_name)
				self.backend.remove_collection()
				gui.QMessageBox.information(self, 'Notification', "The collection " + user_input + " has been removed")

			else:
				pass

	def radioButtonFive(self):
		"""Method for radio button five"""
		# Declares and assigns coll list
		# to the return list from collections_in_db()
		# from the backend class
		self.backend.__init__()
		coll_list = self.backend.collections_in_db()
		# A for loop to run through every item
		# in the list to append to the listWidget
		temp_widget = self.temp_widget
		for item in coll_list:
			item_x = gui.QListWidgetItem(temp_widget)
			item_x.setText(item)
			item_x.setIcon(gui.QIcon("Pokeball.png"))

		temp_widget.setWindowTitle("Collections in Database")
		temp_widget.show()

		"""There is still a slight bug here that I will
		need to fix in the future. For now it works, but not
		optimally"""
		user_input, ok = gui.QInputDialog.getText(self, "Collection Input", \
										"Move window to look at contents. Click OK to clear when finished, or click on cancel to interact with the window")



	def radioButtonSix(self):
		"""Method for queries of a collection"""
		# Asks for user input
		user_input, ok = gui.QInputDialog.getText(self, "Collection Input", "Please input collection to be queried")

		if ok:
			collection_name = str(user_input)
			# Displays that the collection has been selected
			gui.QMessageBox.information(self, "Collection Query", "The collection " + collection_name +\
				" has been chosen")

		option_input, ok = gui.QInputDialog.getText(self, "Option", "Please type FIND or AGGREGATE or KEY(i.e major) for query option")
		if ok:
			value_input, ok = gui.QInputDialog.getText(self, "Query", "Please type query below")

			if ok:
				self.backend.__init__(collection_name)
				query_list = self.backend.query(str(option_input), value_input)

		for item in query_list:
			item_x = gui.QListWidgetItem(self.list_widget)
			item_x.setText(str(item))
			item_x.setIcon(gui.QIcon("Pokeball.png"))


		self.list_widget.setGeometry(300,300,1200,75)
		self.list_widget.setWindowTitle(collection_name + " query contents")
		sb = self.list_widget.verticalScrollBar()
		sb.setValue(sb.maximum())
		self.list_widget.show()

		"""Slight bug. Will be fixed later"""
		"""user_input, ok = gui.QInputDialog.getText(self, "Collection Input", \

										"Move window to look at contents. Click OK to clear when finished, or click on cancel to interact with the window")"""
		if self.list_widget.closeEvent():
			self.list_widget.clear()

	def radioButtonSeven(self):
		"""Method for queries of a collection"""
		# Asks for user input
		user_input, ok = gui.QInputDialog.getText(self, "Collection Input", "Please input collection to be queried")

		if ok:
			collection_name = str(user_input)
			# Displays that the collection has been selected
			gui.QMessageBox.information(self, "Collection Query", "The collection " + collection_name +\
				" has been chosen")

		option_input, ok = gui.QInputDialog.getText(self, "Option", "Please type FIND or AGGREGATE for query option")
		if ok:
			value_input, ok = gui.QInputDialog.getText(self, "Query", "Please type query below")

			if ok:
				file_input, ok = gui.QInputDialog.getText(self, "Collection Input", "Please input filename for the generated queries")
				if ok:
					self.backend.__init__(collection_name)
					query_list = self.backend.queryOutput(str(option_input), value_input, file_input)
					gui.QMessageBox.information(self, "Query Output", "The file " + filename +\
					" has been created")

	def radioButtonEight(self):
		"""Method for queries of a collection"""
		# Asks for user input
		user_input, ok = gui.QInputDialog.getText(self, "Collection Input", "Please input collection to use")

		if ok:
			collection_name = str(user_input)
			# Displays that the collection has been selected
			gui.QMessageBox.information(self, "Collection Query", "The collection " + collection_name +\
				" has been chosen")

		key_input, ok = gui.QInputDialog.getText(self, "Option", "Please type Major or key area")
		if ok:
			value_input, ok = gui.QInputDialog.getText(self, "Query", "Please type note below")

			if ok:
				self.backend.__init__(collection_name)
				query_list = self.backend.insertValues(str(key_input), str(value_input))
				gui.QMessageBox.information(self, "Message" ,"The key and note have been placed.")

	def push_button(self):
		"""Method for about button"""
		# Text literal
		text = ("Gotta catch em'.... This is a simple application that"
				"\ncan be used to add data from the web scrappers"
				"\n(only scrapping pokemon related websites, duh) and"
				"\nplace it within the PokeDB (which is a MongoDB database)."
				"\nThis application can only grow, as more features will be"
				"\nimplemented in the future.")

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
		self.about.setWindowTitle("About PokeDB")
		self.about.setGeometry(300, 300, 495, 120)
		sb = self.about.verticalScrollBar()
		sb.setValue(sb.maximum())
		self.about.show()


def main():
    """Main function"""
    app = gui.QApplication(sys.argv)
    ex = PokeDbGui()
    p = ex.palette()
    p.setColor(ex.backgroundRole(), gui.QColor.fromRgb(255,96,27))
    ex.setPalette(p)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
