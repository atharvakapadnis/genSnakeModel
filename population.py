import pygame
from snake import Snake


class Population:
    def __init__(self, size):
        self.snakes = [Snake() for _ in range(size)]
        self.generation = 0

    def update(self):
        for snake in self.snakes:
            if snake.alive:
                snake.decide_move()
                snake.move()

    def get_best_score(self):
        return max(len(snake.body) for snake in self.snakes)

    def draw(self, screen):
        for snake in self.snakes:
            if snake.alive:
                for segment in snake.body:
                    pygame.draw.rect(
                        screen, (0, 255, 0), (segment[0] * 20, segment[1] * 20, 20, 20)
                    )
