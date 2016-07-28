"""Testing and learning script"""
from pymongo import MongoClient
import json
client = MongoClient()
db = client["pokemon_database"]
collection = db["stat_combinations"]
print(collection)

# Opens created .json file from the web scrapper
with open("pokemon_stat.json") as json_data:
	data = json.load(json_data)

# Inserts the contents of the json file into the database
def insert_to_db(data):
	"""A simple function that inserts the entire json
	file into the database"""
	for item in range(len(data)):
		result = db.collection.insert_one(data[item])

# insert_to_db(data) This was only used as a one
# time thing to insert the collection into the database
strings = " "
"""
db.strings.drop()
db.h_test.drop()
db.j_test.drop()
"""

# Asks for user input
user_input = input("Would you like to view the contents of the collection? (y or n) ")
if user_input == "y" or user_input == "Y":
	cursor = db["stat_combinations"].find()
	
	def print_cursor(cursor_pointer):
		"""A simple function that prints each 
		document in the collection"""
		for document in cursor_pointer:
			print(document)

	print_cursor(cursor)

else:
	print("Exiting the program")