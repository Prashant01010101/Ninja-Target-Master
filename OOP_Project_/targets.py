import pygame
import math

from abc import ABC, abstractmethod
from settings import WIDTH

class BaseTarget(ABC):

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def get_points(self):
        pass



class Target(BaseTarget):

    def __init__(self, x, y, speed):

        self.x = x
        self.y = y
        self.speed = speed
        self.radius = 28

    def move(self):

        self.x += self.speed

        # Bounce at the right edge
        if self.x + self.radius >= WIDTH:
            self.x = WIDTH - self.radius
            self.speed = -self.speed

        # Bounce at the left edge
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.speed = -self.speed

    def draw(self, screen):

        x = int(self.x)
        y = int(self.y)

        # Outer wooden circle
        pygame.draw.circle(
            screen,
            (155, 105, 60),
            (x, y),
            self.radius
        )

        # Red circle
        pygame.draw.circle(
            screen,
            (185, 55, 55),
            (x, y),
            20
        )

        # White circle
        pygame.draw.circle(
            screen,
            (235, 220, 180),
            (x, y),
            12
        )

        # Center bullseye
        pygame.draw.circle(
            screen,
            (80, 35, 30),
            (x, y),
            5
        )

    def get_points(self):
        return 10

    def is_hit(self, shuriken):

        dx = self.x - shuriken.x
        dy = self.y - shuriken.y

        distance = math.sqrt(dx * dx + dy * dy)

        if distance <= self.radius + shuriken.radius:
            return True

        return False


class FastTarget(BaseTarget):

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = 20

    def get_points(self):
        return 20

    def draw(self, screen):

        x = int(self.x)
        y = int(self.y)

        pygame.draw.circle(
            screen, (45, 100, 180),
            (x, y), self.radius
        )

        pygame.draw.circle(
            screen, (230, 220, 180),
            (x, y), 13
        )

        pygame.draw.circle(
            screen, (45, 100, 180),
            (x, y), 6
        )

    def move(self):

        self.x += self.speed

        if self.x + self.radius >= WIDTH:
            self.x = WIDTH - self.radius
            self.speed = -self.speed

        if self.x - self.radius <= 0:
            self.x = self.radius
            self.speed = -self.speed

    def is_hit(self, shuriken):

        dx = self.x - shuriken.x
        dy = self.y - shuriken.y

        distance = math.sqrt(dx * dx + dy * dy)

        if distance <= self.radius + shuriken.radius:
            return True

        return False


class GoldenTarget(Target):

    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        self.radius = 24

    def get_points(self):
        return 50

    def draw(self, screen):

        x = int(self.x)
        y = int(self.y)

        pygame.draw.circle(
            screen,
            (190, 135, 30),
            (x, y),
            self.radius
        )

        pygame.draw.circle(
            screen,
            (245, 195, 65),
            (x, y),
            17
        )

        pygame.draw.circle(
            screen,
            (255, 235, 150),
            (x, y),
            9
        )


class DangerTarget(Target):

    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        self.radius = 26

    def get_points(self):
        return -20

    def draw(self, screen):

        x = int(self.x)
        y = int(self.y)

        pygame.draw.circle(
            screen,
            (130, 30, 40),
            (x, y),
            self.radius
        )

        pygame.draw.circle(
            screen,
            (35, 30, 35),
            (x, y),
            18
        )

        # Warning symbol
        points = [
            (x, y - 13),
            (x - 12, y + 10),
            (x + 12, y + 10)
        ]

        pygame.draw.polygon(
            screen,
            (230, 65, 65),
            points
        )

        pygame.draw.line(
            screen,
            (255, 255, 255),
            (x, y - 5),
            (x, y + 3),
            3
        )

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (x, y + 7),
            2
        )
