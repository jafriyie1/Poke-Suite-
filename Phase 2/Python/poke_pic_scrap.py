"""Web Scraper for Picture Collection
for train data of Pokemon Pictures"""
from urllib.request import urlopen, HTTPError, urlretrieve
from bs4 import BeautifulSoup


def get_poke_name(url):
	""" Function to get pokemon names"""
	poke = []
	html = urlopen(url)
	bs_obj = BeautifulSoup(html, "lxml")
	tmp = bs_obj.findAll("a", {"class":"ent-name"})	

	for x in tmp:
		poke.append(x.get_text())

	return poke

def main():
	"""Main function"""
	# Base urls
	start_url = "http://pokemondb.net/pokedex/national"
	base_url = "http://pokedream.com/pokedex/pokemon/"
	# Pokemon name list
	pokemon_list = get_poke_name(start_url)


	for pokemon in pokemon_list:
		# Runs through each pokemon in pokemon list
		# Prints pokemon to display progress
		print(pokemon)
		if pokemon == "Nidoran♀":
			pokemon = "Nidoran F"
		elif pokemon == "Nidoran♂":
			pokemon = "Nidoran M"
		elif pokemon == "Flabébé":
			pokemon = "Flabebe"
		# cReates new url and passes it to a new BeautifulSoup object
		new_url = base_url+pokemon
		temp = urlopen(new_url)
		soup = BeautifulSoup(temp, "lxml")
		img_base_url = "http://pokedream.com"

		image = soup.findAll("img", {"class": "main-picture"})

		for img in image:
			# Assigns new variable to base of image url
			# and the source of the image. Creates 
			# a new jpg file and writes 
			# the contents of the new webpage into the file
			out_img = img_base_url + img["src"]
			f = open(pokemon+"_train1.jpg", "wb")
			f.write(urlopen(out_img).read())
			f.close()
		
	print("Finished, Pictures have been amassed!")

if __name__ == "__main__":
	main()