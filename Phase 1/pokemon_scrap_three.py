"""Web Scrapper for Bulbapedia poxedex"""
from bs4 import BeautifulSoup 
from urllib.request import urlopen, HTTPError 
import re 
import json 

data_list = []


def check_open(url):
	"""Checks if the webpage can be opened"""
	try:
		urlopen(url)
		print("The webpage has opened")
		return "Execute"
	except HTTPError as e:
		return None 


def gen_pokedex_list(url):
	"""Generates list of pokemon in pokedex"""
	html = urlopen(url)
	bs_obj = BeautifulSoup(html, 'lxml')
	regex =  re.compile("/pokedex/.+[a-z]")
	
	pokedex = bs_obj.findAll("a", {"class": "ent-name"} , {"href":regex})
	poke_gen_list = [x.get_text() for x in pokedex]

	return poke_gen_list


def get_Text(base_url, pokedex, data):
	"""Gets the paragraph text from various webpages"""
	try:
		if len(pokedex) == 0:
			print("Finished")
		else:	
			pokemon = pokedex.pop()
			if pokemon == "Mime Jr.":
				pokemon = "Mime Jr"
			elif pokemon == "Mr. Mime":
				pokemon = "Mr Mime"
			elif pokemon == "Nidoran♀":
				pokemon = "Nidoran F"
			elif pokemon == "Nidoran♂":
				pokemon = "Nidoran M"

			print(pokemon)
			html = urlopen(base_url)
			bs_obj = BeautifulSoup(html, 'lxml')
			para = bs_obj.findAll("p")

			for item in range(len(para)):
				current_item = para[item].get_text()
				temp_dict = {pokemon: current_item}
				data.append(temp_dict)

			base_page = "http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
			next_page = "http://bulbapedia.bulbagarden.net/wiki/"+pokemon+"_(Pokemon)"
			urlopen(base_page)

	except UnicodeEncodeError:
		
		base_page = "http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
		next_page = "http://bulbapedia.bulbagarden.net/wiki/"+pokemon+"_(Pokemon)"
		urlopen(base_page)

		

	except HTTPError as e:
		
		base_page = "http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
		next_page = "http://bulbapedia.bulbagarden.net/wiki/"+pokemon+"_(Pokemon)"
		urlopen(base_page)

		
	if len(pokedex) != 0:
		get_Text(next_page, pokedex, data)
	else:
		print("Finished")



if __name__ == "__main__":
	check_open("http://pokemondb.net/pokedex/national")
	pokedex_list = gen_pokedex_list("http://pokemondb.net/pokedex/national")

	uni = "http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
	get_Text(uni, pokedex_list, data_list)

	with open("bulbapedia_info.json", "w") as jsonfile:
		json.dump(data_list,jsonfile, indent=1)

