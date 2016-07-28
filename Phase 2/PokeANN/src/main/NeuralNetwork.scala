package main

import breeze.numerics._
import breeze.linalg._
class NeuralNetwork(layer1: NeuronLayer, layer2: NeuronLayer) {
  
  private def sigmoid(x: DenseVector[Double]) = {
    1 / (1 + exp(-x))
  }
  
  private def sigmoid_derivative(x: DenseVector[Double]) = {
    x dot (DenseVector[Double](1) -x)
  }
 
 def think(inputs: DenseVector[Double])
 {
   var new_input = this.layer1.synaptic_weights * inputs
   var output_layer_one = this.sigmoid(new_input)
   var output_layer_two = this.sigmoid(output_layer_one dot this.Layer2.synaptic_weights)
   return output_layer_one
   return output_layer_two
 }
 def train(training_set_inputs: DenseVector[Double], training_set_outputs: DenseVector[Double], num_iterations: Int) = { 
   for(iterations<- 0 to num_iterations) 
   {
     var output_layer1 = this.think(training_set_inputs)
     var output_layer2 = this.think(training_set_inputs)
     
     var negated_train = training_set_outputs * -1.0
     var layer2_error = output_layer2 + negated_train
     var layer2_delta = layer2_error * this.sigmoid_derivative(output_layer2)
     
     var layer1_error = layer2_delta dot this.layer2.synaptic_weights
     var layer1_delta = layer1_error * this.sigmoid_derivative(output_layer1)
     
     var layer1_adjustment = training_set_inputs.t dot layer1_delta
     var layer2_adjustment = output_layer1.t dot layer2_delta
     
     this.layer1.synaptic_weights += layer1_adjustment
     this.layer2.synaptic_weights += layer2_adjustment
   }  
 }
 

  
}