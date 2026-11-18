import pygame
import math

from settings import WIDTH, HEIGHT, BLACK

class Shuriken:

    def __init__(self, x, y, target_x, target_y):

        self.x = float(x)
        self.y = float(y)

        self.speed = 12
        self.radius = 12

        # Calculate direction to mouse
        dx = target_x - self.x
        dy = target_y - self.y

        distance = math.sqrt(dx * dx + dy * dy)

        if distance == 0:
            distance = 1

        self.dx = dx / distance
        self.dy = dy / distance

    def move(self):

        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def draw(self, screen):

        x = int(self.x)
        y = int(self.y)
        r = self.radius

        # Four-pointed throwing star
        points = [
            (x, y - r),
            (x + 4, y - 4),
            (x + r, y),
            (x + 4, y + 4),
            (x, y + r),
            (x - 4, y + 4),
            (x - r, y),
            (x - 4, y - 4)
        ]

        pygame.draw.polygon(
            screen,
            (190, 200, 210),
            points
        )

        # Center hole
        pygame.draw.circle(
            screen,
            BLACK,
            (x, y),
            3
        )

    def is_off_screen(self):

        if self.x < 0 or self.x > WIDTH:
            return True

        if self.y < 0 or self.y > HEIGHT:
            return True

        return False