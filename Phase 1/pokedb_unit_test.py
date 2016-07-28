import unittest 
from pokedb import PokeDB

class PokeDBTests(unittest.TestCase):
	"""Tests the workability of the PokeDb class"""

	def poke_db_bson(self):
		"""Checks if the database can take 
		a collection name"""
		self.PokeDb.load_json_file("blank.json")
		self.assertRaises(self.PokeDb.insert_to_db())

if __name__ == "__main__":
	unittest.main()
