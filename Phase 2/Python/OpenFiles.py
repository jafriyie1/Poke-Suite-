import numpy as np 
import matplotlib.pyplot as plt
import os 
import skimage.io as io
from skimage.color import rgb2gray
from skimage.transform import resize
import random

class OpenImageFiles():
	"""a Class that opens files to be viewed"""

	def __init__(self, path_name):
		"""Constructor method"""
		self.__path_name = path_name


	def getPath(self):
		"""Accessor method"""
		return self.__path_name

	def setPath(self, path_name):
		"""Mutator method"""
		self.__path_name = path_name

	def getOpenFiles(self):
		"""Method to find files, open files transform 
		and return a list of numpy arrays"""
		file_list = []
		np_img_list = []
		extension = input("Please specify which extension to be read in: ")
		for files in os.listdir(self.__path_name):
			if files.endswith(extension):
				file_list.append(files)
		
		for item in file_list: 
			tmp_file = self.__path_name+"/"+item
			shown_item = resize(io.imread(tmp_file), (96,96))
			grayed_item = rgb2gray(shown_item)
			np_img_list.append(grayed_item)
		
		return np_img_list

	def getSingleFile(self):
		"""Method to find single files"""
		tmp_file = self.__path_name
		shown_item = resize(io.imread(tmp_file), (96,96))
		grayed_item = rgb2gray(shown_item)
		return grayed_item



def main():
	rand_int = random.randint(1,721)
	path = input("Please enter absolute path: ")
	obj = OpenImageFiles(path)
	alist = obj.getOpenFiles()
	temp_picture = alist[rand_int]
	print(type(temp_picture))
	print(temp_picture.shape)
	#print(temp_picture)
	plt.imshow(temp_picture)
	plt.show()

if __name__ == "__main__":
	main()
