import numpy as np
import random


class NeuralNet:
    def __init__(self, input_size=24, hidden_layers=[16, 16], output_size=4):
        self.layers = [input_size] + hidden_layers + [output_size]
        self.weights = [
            np.random.randn(self.layers[i], self.layers[i + 1])
            for i in range(len(self.layers) - 1)
        ]

    def forward(self, inputs):
        activation = np.array(inputs)
        for w in self.weights:
            activation = np.tanh(np.dot(activation, w))
        return activation
