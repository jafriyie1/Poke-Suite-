"""Web Scrapper for pokemondb stat combinations"""
from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup 
import json

"""Global variables"""
key_list = []
data_list = []
new_values = []

def get_title(url):
	"""Gets the h1 header of the webpage"""
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None 
	try:
		bs_boj = BeautifulSoup(html, 'lxml')
		title = bs_boj.h1
	except AttributeError as e:
		return None 
	return title


def gen_list_of_keys(keys):
	"""generate keys for future dictionary"""
	key_list = []
	i = 0
	while i < len(keys):		
		key_list.append(keys[i].get_text())
		i+=1
	key_list.remove("#")
	key_list.remove("Type")	
	key_list.remove("Total")
	# A For loop to remove periods.
	# I will have to find a more pythonic
	# way of doing this
	for x in range(len(key_list)):
		if key_list[x] == "Ph. Sweeper":
			key_list[x] = "Ph Sweeper"	
		elif key_list[x] == "Sp. Sweeper":
			key_list[x] = "Sp Sweeper"	
		elif key_list[x] == "Ph. Tank":
			key_list[x] = "Ph Tank"		
		elif key_list[x] == "Sp. Tank":
			key_list[x] = "Sp Tank"					
	return key_list

def gen_values_list(values):
	"""Generates a list of values with stripped html"""
	new_values = []
	i = 0
	while i < len(values):
		new_values.append(values[i].get_text()) 
		i+=1	
	return new_values		
			

def poke_strip(pokemon):
	"""Strips the html tags from the Pokemon list"""
	poke_name = []
	for x in range(len(pokemon)):
		poke_name.append(pokemon[x].get_text())
	return poke_name	


def pairing(keys, pokemon, values, data_list):
	"""Creates a dictionary from two lists 
	and then appends the list to another list.
	This is done through recursion"""
	mutate_values = values
	temp_keys = keys
	# Sets a variable to popped value of list
	temp_pokemon = pokemon.pop(0)
	temp_values = []
	temp_values.append(temp_pokemon)

	# This for loop takes a popped value from
	# One list and converts it to an integer
	# And appends it to a new list
	for int_val in range(1,6):
		temp = mutate_values.pop(int_val)
		temp_values.append(int(temp))

	# Creates new dictionary by zipping together
	# The keys list and the temp_values list	
	new_dict = dict(zip(keys,temp_values))
	del temp_values
	data_list.append(new_dict)
	
	if len(mutate_values) == 0 or len(pokemon) == 0:
		return "finished"
	else: 
		# Calls function recursively 
		pairing(keys, pokemon, values, data_list)

	
	
if __name__ == "__main__":
	# Opens the webpage
	html = urlopen("http://pokemondb.net/pokedex/stats/combo")

	# Checks if webpage can be found
	title = get_title("http://pokemondb.net/pokedex/stats/combo")
	if title == None:
		print("webage cannot be found")
	else:
		# Creates a new BeautifulSoup object and generates 
		# Poke list and values list
		bs_obj = BeautifulSoup(html, 'lxml')
		pokemon = bs_obj.findAll("a", {"class":"ent-name"})
		values = bs_obj.findAll("td", {"class":"num"})

		list_of_keys = bs_obj.findAll("div", {"class":"sortwrap"})
		keys = gen_list_of_keys(list_of_keys)

		gen_values = gen_values_list(values)
		poke_list = (poke_strip(pokemon))

		pairing(keys, poke_list, gen_values,data_list)

		# Writes the list of dictionaries to a JSON
		# file to be used for further analysis
		with open("pokemon_stat.json",'w') as outfile:
			json.dump(data_list, outfile,indent=1)



		




