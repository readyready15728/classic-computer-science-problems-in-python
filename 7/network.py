from functools import reduce
from layer import Layer
from util import sigmoid, derivative_sigmoid

class Network:
    def __init__(self, layer_structure, learning_rate, activation_function=sigmoid, derivative_activation_function=derivative_sigmoid):
        if len(layer_structure) < 3:
            raise ValueError('Error: should be at least 3 layers (1, input, 1 hidden, 1 output')

        self.layers = []

        # Input layer
        input_layer = Layer(None, layer_structure[0], learning_rate, activation_function, derivative_activation_function)
        self.layers.append(input_layer)
        # Hidden layer(s) and output layer
        for previous, num_neurons in enumerate(layer_structure[1:]):
            next_layer = Layer(self.layers[previous], num_neurons, learning_rate, activation_function, derivative_activation_function)
            self.layers.append(next_layer)

    def outputs(self, input_):
        return reduce(lambda inputs, layer: layer.outputs(inputs), self.layers, input_)

    def back_propagate(self, expected):
        last_layer = len(self.layers) - 1
        # Calculate delta for outer layer
        self.layers[last_layer].calculate_deltas_for_output_layer(expected)
        # Calculate delta for hidden layers in reverse order
        for l in range(last_layer - 1, 0, -1):
            self.layers[l].calculate_deltas_for_hidden_layer(self.layers[l + 1])

    # Apply changes effected by back_propagate()
    def update_weights(self):
        for layer in self.layers[1:]: # Skip input layer
            for neuron in layer.neurons:
                for w in range(len(neuron.weights)):
                    neuron.weights[w] = neuron.weights[w] + neuron.learning_rate * layer.previous_layer.output_cache[w] * neuron.delta

    def train(self, inputs, expecteds):
        for location, xs in enumerate(inputs):
            ys = expecteds[location]
            outs = self.outputs(xs)
            self.back_propagate(ys)
            self.update_weights()

    def validate(self, inputs, expecteds, interpret_output):
        correct = 0

        for input_, expected in zip(inputs, expecteds):
            result = interpret_output(self.outputs(input_))

            if result == expected:
                correct += 1

        percentage = correct / len(inputs)
        return correct, len(inputs), percentage
