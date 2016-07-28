import pickle 
from ANN import NeuronLayer, NeuralNetwork
from numpy import array
f = open("neural_network.obj" ,"rb+")

trained_net = pickle.load(f)
f.close()
x= trained_net.think(array([1,0,1,1,0,1]))

print(x)