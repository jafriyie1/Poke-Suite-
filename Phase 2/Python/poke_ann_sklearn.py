from OpenFiles import OpenImageFiles 
from ANN import NeuronLayer, NeuralNetwork
from numpy import array
from sklearn.neural_network import MLPClassifier 
import numpy as np
import random

def implementation():
	"""Implementation function for ANN"""
	rand_int = random.randint(1,721)
	path = input("Please enter absolute path: ")
	
	obj = OpenImageFiles(path)
	data = obj.getOpenFiles()
	train_input = data[:521]
	train_output = data[521:]
	
	temp_picture_output = alist[rand_int]

	clf = MLPClassifier(activation="logistic", algorithm ="adam", 
		learning_rate_init=0.00001, max_iter=500)

	clf.fit(train_input, train_output)
	clf.predict(temp_picture_output)