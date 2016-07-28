"""Web scrapper for serebii news"""

from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup 
import calendar
import json


base_url = "http://www.serebii.net/"
all_paragraphs = []
month_list = []
month_year_list = []
final_list = []


# Creates month list
for x in range(1,13):
	month_list.append(calendar.month_name[x])


# This is a very very stupid way of doing 
# this! But I could not think of a more immediate
# and elegant way of doing this. If you look at my 
# code and know of any improvements please let me know
# FYI I am a noob when it comes to programming :)
digit_list = ["00","01","02","03","04","05","06","07","08",
			"09","10","11","12","13","14","15","16"]


# I did this so I could get a pairing of the months
# and the year

for x in digit_list:
	for y in range(len(month_list)):
		month_year_list.append(month_list[y]+" 20"+x)


def check(url):
	"""This function checks if the webpage can be 
	opened or not"""
	try:
		urlopen(url)
		print("The Webpage has been opened")
		return "go"
	except HTTPError as e:
		return None

def paragraph_generator(url,all_paragraphs,date_list):
	"""A function that will go through all of the 
	news link on serebii.net and grab each paragraph"""
	html = urlopen(base_url)

	bs_obj = BeautifulSoup(html, 'lxml')

	news = bs_obj.findAll({"p"})

	# Appends each paragraph
	for paragraph in news:
		all_paragraphs.append(paragraph.get_text())

	# After appending the paragraph the scrapper
	# looks for the Archived News link
	tail = bs_obj.find({"a": "Archived News"})

	# Gets the url of the link and opens it
	new_tail = (tail['href'])
	urlopen(new_tail)

	# This part of the function loops through
	# each of the items in the date_list, 
	# pops the item (and doing so decreases the 
	# size of the date_list by 1), finds the link of 
	# the item, calls its url, and then gets plugged
	# back into the recursive function call
	size = len(date_list)
	if size > 0:
		for x in range(len(date_list)):
			if x == 0:
				date = date_list.pop()
				rec_tail = bs_obj.find({"a": date})
				recursive_tail = tail["href"]
				print(date)
				paragraph_generator(recursive_tail,all_paragraphs, \
									date_list)
				break
			break
	elif size == 0:
		print("finished")

def id_gen(all_paragraphs):
	id_list = ["Paragraph " +str() for x in range(len(all_paragraphs))]
	return id_list

	
def dict_to_list(ids, para, final):
	"""Generates dictionaries and appends it to list"""
	for item in range(len(para)):
		temp_dict = {ids[item] : para[item]}
		final.append(temp_dict)

"""The "Main" function of the scrapper"""
if __name__ == "__main__":
	go_ahead = check(base_url)
	if go_ahead == None:
		print("Webpage was not found. Program will terminate.")
	else:
		paragraph_generator(base_url,all_paragraphs,month_year_list)
		# List comp for the keys of the upcoming list
		
		# Creates a list of dictionaries (or documents) to be inserted
		# into the JSON file 
		new_list = id_gen(all_paragraphs)
		dict_to_list(new_list, all_paragraphs, final_list)
		
		# Dumps the final_list into a json file
		with open("serebii_news.json","w") as jsonfile:
			json.dump(final_list, jsonfile ,indent=2)
