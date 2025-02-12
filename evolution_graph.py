import matplotlib.pyplot as plt


class EvolutionGraph:
    def __init__(self):
        self.scores = []

    def update(self, best_score):
        self.scores.append(best_score)
        plt.plot(self.scores)
        plt.pause(0.01)
