import random

WIDTH, HEIGHT, GRID_SIZE = 500, 500, 20


class Food:
    def __init__(self):
        self.position = [
            random.randint(0, WIDTH // GRID_SIZE - 1),
            random.randint(0, HEIGHT // GRID_SIZE - 1),
        ]

    def respawn(self):
        self.position = [
            random.randint(0, WIDTH // GRID_SIZE - 1),
            random.randint(0, HEIGHT // GRID_SIZE - 1),
        ]
