import pygame
from population import Population
from evolution_graph import EvolutionGraph

WIDTH, HEIGHT = 500, 500
POPULATION_SIZE = 2000


def init_game():
    pygame.init()
    return pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    screen = init_game()
    population = Population(POPULATION_SIZE)
    evolution_graph = EvolutionGraph()

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        population.update()
        population.draw(screen)
        evolution_graph.update(population.get_best_score())

        pygame.display.flip()
        pygame.time.delay(100)

    pygame.quit()


if __name__ == "__main__":
    main()
