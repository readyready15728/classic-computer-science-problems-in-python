from random import random
from neuron import Neuron
from util import dot_product

class Layer:
    def __init__(self, previous_layer, num_neurons, learning_rate, activation_function, derivative_activation_function):
        self.previous_layer = previous_layer
        self.neurons = []

        for i in range(num_neurons):
            if previous_layer is None:
                random_weights = []
            else:
                random_weights = [random() for _ in range(len(previous_layer.neurons))]

            neuron = Neuron(random_weights, learning_rate, activation_function, derivative_activation_function)
            self.neurons.append(neuron)

        self.output_cache = [0 for _ in range(num_neurons)]

    def outputs(self, inputs):
        if self.previous_layer is None:
            self.output_cache = inputs
        else:
            self.output_cache = [neuron.output(inputs) for neuron in self.neurons]

        return self.output_cache

    def calculate_deltas_for_output_layer(self, expected):
        for i in range(len(self.neurons)):
            self.neurons[i].delta = self.neurons[i].derivative_activation_function(self.neurons[i].output_cache) * (expected[i] - self.output_cache[i])

    def calculate_deltas_for_hidden_layer(self, next_layer):
        for i, neuron in enumerate(self.neurons):
            next_weights = [n.weights[i] for n in next_layer.neurons]
            next_deltas = [n.delta for n in next_layer.neurons]
            sum_weights_and_deltas = dot_product(next_weights, next_deltas)
            neuron.delta = neuron.derivative_activation_function(neuron.output_cache) * sum_weights_and_deltas
