import random
import numpy as np
from neural_net import NeuralNet

WIDTH, HEIGHT, GRID_SIZE = 500, 500, 20


class Snake:
    def __init__(self):
        self.body = [[5, 5]]
        self.direction = [0, 1]
        self.brain = NeuralNet()
        self.alive = True
        self.food = [
            random.randint(0, WIDTH // GRID_SIZE - 1),
            random.randint(0, HEIGHT // GRID_SIZE - 1),
        ]

    def move(self):
        head = self.body[-1]
        new_head = [head[0] + self.direction[0], head[1] + self.direction[1]]
        if new_head in self.body or not (
            0 <= new_head[0] < WIDTH // GRID_SIZE
            and 0 <= new_head[1] < HEIGHT // GRID_SIZE
        ):
            self.alive = False
        else:
            self.body.append(new_head)
            if new_head == self.food:
                self.food = [
                    random.randint(0, WIDTH // GRID_SIZE - 1),
                    random.randint(0, HEIGHT // GRID_SIZE - 1),
                ]
            else:
                self.body.pop(0)

    def decide_move(self):
        inputs = np.random.rand(24)  # Replace with actual vision inputs
        output = self.brain.forward(inputs)
        moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        self.direction = moves[np.argmax(output)]
