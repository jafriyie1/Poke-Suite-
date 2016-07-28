from OpenFiles import OpenImageFiles 
from ANN import NeuronLayer, NeuralNetwork
from numpy import array
from sklearn import neural_network
import numpy as np
import random
import pickle

def implementation():
	"""Implementation function for ANN"""

	layer1 = NeuronLayer(96, 96)
	layer2 = NeuronLayer(10, 96)

	neural_network = NeuralNetwork(layer1, layer2)

	print("Stage 1) Random starting synaptic weights: ")
	neural_network.print_weights()

	rand_int = random.randint(1,721)
	two_int = random.randint(1,30)
	#path = input("Please enter absolute path: ")
	temp_path = "/Users/Joel/Desktop/Joel's Poke Suite/Phase 2/Poke Pictures Train"
	obj = OpenImageFiles(temp_path)
	data = obj.getOpenFiles()
	test_picture = data[rand_int]
	np_training_outputs = array([[1] for x in range(728)]).T


	temp_path_non = "/Users/Joel/Desktop/Joel's Poke Suite/Phase 2/Not Poke Pictures"
	obj = OpenImageFiles(temp_path_non)
	data_not = obj.getOpenFiles()
	test_p = data_not[two_int]
	np_training_outputs_non = array([[0] for x in range(56)]).T

	#print(np_training_outputs)

	counter = 0 
	print("Training...")
	total_size = len(data) + len(data_not)
	for train in range(total_size):
		training_set_inputs = data[train]
		neural_network.train(training_set_inputs, np_training_outputs[train], 20000)
		print(("Number of iterations: %d") % counter)
		counter += 1
		if counter


	print("Training once again...")
	for train in range(len(data_not)):
		training_set_inputs = data_not[train]
		neural_network.train(training_set_inputs, np_training_outputs_non[train], 20000)
		print(("Number of iterations: %d") % counter)
		counter+=1


	print("Stage 2) New synaptic weights after training: ")
	neural_network.print_weights()

	print("Stage 3) Considering a new situation -> ?: ")
	hidden_state, output = neural_network.think(test_p)
	out = np.mean(output)
	out = round(out, 10)
	real_out = 100.0000*out
	print(real_out) 
	print()
	hidden_state, output = neural_network.think(test_picture)
	out = np.mean(output)
	out = round(out, 10)
	real_out = 100.0000*out
	#print(real_out) 

	current_pickled = neural_network
	f = open("neural_network.obj", "wb+")
	pickle.dump(current_pickled, f)
	f.close()


if __name__ == "__main__":
	implementation()