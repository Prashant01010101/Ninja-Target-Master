import pygame

from settings import WIDTH, GOLD

class ScoreBoard:

    def __init__(self):

        self._score = 0
        self.goal = 150
        self._time_left = 60
        self.hits = 0
        self.misses = 0

        self.font = pygame.font.SysFont(
            "arial", 30, bold=True
        )

    @property
    def score(self):
        return self._score

    @score.setter 
    def score(self, value):

        if value < 0:
            self._score = 0

        else:
            self._score = value

    @property
    def time_left(self):
        return self._time_left

    @time_left.setter
    def time_left(self, value):
        if value < 0:
            self._time_left = 0

        else:
            self._time_left = value


    def add_points(self, points):
        self.score += points

    def update_time(self, seconds):

        self.time_left -= seconds

    def is_winner(self):

        return self.score >= self.goal

    def is_time_up(self):

        return self.time_left <= 0

    
    def add_hit(self):
        self.hits += 1


    def add_miss(self):
        self.misses += 1


    def get_accuracy(self):

        total = self.hits + self.misses

        if total == 0:
            return 0

        return (self.hits / total) * 100


    def draw(self, screen, level_number):

        pygame.draw.rect(
            screen,
            (25, 25, 35),
            (0, 0, WIDTH, 80)
        )

        score_text = self.font.render(
            f"Score: {self.score}",
            True,
            GOLD
        )

        time_text = self.font.render(
            f"Time: {int(self.time_left)}",
            True,
            GOLD
        )

        goal_text = self.font.render(
            f"L{level_number} | Goal: {self.goal}",
            True,
            GOLD
        )

        screen.blit(score_text, (30, 25))
        screen.blit(time_text, (390, 25))
        screen.blit(goal_text, (760, 25))
