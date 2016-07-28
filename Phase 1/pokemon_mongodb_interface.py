"""Testing script"""
from pymongo import MongoClient
import json 
import sys 


client = MongoClient()
db = client["pokemon_database"]

prompt = input("Welcome to Joel's pokemon database! Which feature would you like to use?\n"\
				" 1) Create collection \n 2) Insert json file into collection \
				 \n 3) Print document in collection \n "\
				"4) exit ")

def program(prompt):
	while True:
		if prompt == "1":
			print("Creating collection")
			break
		elif prompt == "2":
			print("Insertion of file")
			break
		elif prompt == "3":
			print("Print documents")
			break
		else:
			print("exiting program")
			return "4"
			break 

def access(validation):
	if validation == "y":
		return "y"
	elif validation == "n":
		return "n"

if program(prompt) == "4":
	break

user_input = input("Would you like to use another feature? (y or n) ").lower()
access(user_input)

while access(user_input) == "y" or new_prompt!=4:
	new_prompt = input("Which feature would you like to use?\n"\
					" 1) Create collection \n 2) Insert json file into collection \
					 \n 3) Print document in collection \n "\
					"4) exit ")
	program(new_prompt)
	user_input = input("Would you like to use another feature? (y or n) ").lower()
	if access == "n" or program(new_prompt) == "4" :
		break






