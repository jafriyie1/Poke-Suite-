package main
import breeze.linalg._
import breeze.stats.distributions._
class NeuronLayer(number_of_neurons: Int, number_of_inputs_per_neuron: Int) {
  
    var synaptic_weights =  2 * (((DenseVector.rand(number_of_neurons)) dot DenseVector.rand(number_of_inputs_per_neuron)) - 1)
    
  
}