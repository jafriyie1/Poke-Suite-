"""Backend of Joel's PokeDB application"""
import pymongo
import json
import tempfile
import subprocess
from bson.json_util import dumps
import bson
import re
import ast

class PokeDB(object):
	"""The class for the "back-end" of the
	application. This class interacts with the MongoDB database
	directly and json. More will be added to it over time."""

	def __init__(self, collection_name=""):
		"""Constructor method"""

		# Bash script
		bash_command_script = '''\
		echo "Running mongod"
		mongod
		echo "mongod is now running"
		echo "DBQuery.prototype._prettyShell = true >> ~/.mongorc.py"
		echo "Program will now execute"

		'''

		self.run_command(bash_command_script)
		self.collection_name = collection_name
		client = pymongo.MongoClient()
		self.db = client["pokemon_database"]
		self.collection = self.collection_name


	def collections_in_db(self):
		"""Method that returns a list of all collections in the database"""
		return list(self.db.collection_names(include_system_collections=False))


	def collection_creation(self):
		"""Method that creates a new collection"""
		try:
			# Tries to create a new collection if it does not
			# already exist
			db = self.db
			collection = self.collection
			db.create_collection(collection)
		except pymongo.errors.CollectionInvalid:
			print("The collection already exists")

	def load_json_file(self, path):
		"""Method that loads json file. Has a parameter path
		for loading of JSON file"""
		self.path = path
		try:
			# Tries to open the json file
			# Converts json to bson
			with open(self.path) as json_data:
				bson_data = (json.load(json_data))
			return bson_data
		except json.decoder.JSONDecodeError:
			print("File is not a JSON file. Try again")


	def insert_to_db(self):
		"""Method that inserts loaded json file into database"""
		db = self.db
		t_collection = self.collection
		data = self.load_json_file(self.path)

		for item in range(len(data)):
			result = db[t_collection].insert_one(data[item])

	def print_content(self):
		"""Method that appends content of collection
		to a list and returns it"""
		coll_list = []
		coll_prompt = self.collection
		collection_cursor = self.db[coll_prompt].find()

		for document in collection_cursor:
			coll_list.append(document)

		return coll_list

	def remove_collection(self):
		"""Removes collection from database"""
		db = self.db
		dropped_collection = self.collection
		db[dropped_collection].drop()

	def run_command(self, command):
		"""Method for creating a temporary file for the terminal
		commands"""
		with tempfile.NamedTemporaryFile(mode="w+", encoding="utf-8") as scriptfile:
			scriptfile.write(command)
			scriptfile.flush()
			subprocess.call(['/bin/bash', scriptfile.name])

	def query(self, option, query):
		"""Method that takes in user input of a query
		and finds that specific query"""
		query_list = []
		db = self.db
		coll = self.collection
		# Converts string to a json object
		json_string = query


		if option.lower() == "find":
			# Does a find query
			query_obj = json.loads(json_string)
			query_cursor = db[coll].find(query_obj)

			# Finds the documents with the condition
			# and appends to the query list
			for query in query_cursor:
				query_list.append(query)

		if option.lower() == "key":
			query_cursor = db[coll].find({}, {query: 1})

			for query in query_cursor:
				query_list.append(query)


		elif option.lower() == "aggregate":
			# Does an aggregate query
			#raw_query = "'''"+query"'''"
			#print(raw_query)
			agg_obj = ast.literal_eval(raw_query)
			print(agg_obj)
			print(type(agg_obj))
			query_cursor = db[coll].aggregate(agg_obj)

			# Finds the documents with the condition
			# and appends to the query list
			for query in query_cursor:
				query_list.append(query)


		return query_list

	def queryOutput(self, option, query, filename):
		"""Outputs query into a json file"""
		query_list = []
		db = self.db
		coll = self.collection
		json_string = query

		if option.lower() == "find":
			# Does a find query
			query_obj = json.loads(json_string)
			query_cursor = db[coll].find(query_obj)

			# Finds the documents with the condition
			# and appends to the query list
			for query in query_cursor:
				query_list.append(query)

		with open(filename, "wb") as json_data:
				bson_data = (json.load(json_data))

	def insertValues(self, key, value):
		db =self.db
		coll = self.collection
		insert_dict = {key: value}
		db[coll].insert(insert_dict)
