import pygame

from settings import WIDTH, HEIGHT, BLACK

class Ninja:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()

        # Move left
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed

        # Move right
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed

        # Move up
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= self.speed

        # Move down
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.speed

        # Keep ninja inside the training area
        if self.x < 30:
            self.x = 30

        if self.x > WIDTH - 30:
            self.x = WIDTH - 30

        if self.y < 470:
            self.y = 470

        if self.y > HEIGHT - 35:
            self.y = HEIGHT - 35

    def draw(self, screen):

        x = int(self.x)
        y = int(self.y)

        # Shadow
        pygame.draw.ellipse(
            screen, (65, 45, 35),
            (x - 23, y + 21, 46, 12)
        )

        # Legs
        pygame.draw.rect(
            screen, BLACK,
            (x - 17, y + 7, 14, 22)
        )

        pygame.draw.rect(
            screen, BLACK,
            (x + 3, y + 7, 14, 22)
        )

        # Body
        pygame.draw.rect(
            screen, (25, 28, 35),
            (x - 20, y - 20, 40, 34)
        )

        # Arms
        pygame.draw.rect(
            screen, BLACK,
            (x - 29, y - 17, 10, 29)
        )

        pygame.draw.rect(
            screen, BLACK,
            (x + 19, y - 17, 10, 29)
        )

        # Red belt
        pygame.draw.rect(
            screen, (180, 40, 50),
            (x - 20, y + 3, 40, 7)
        )

        # Head
        pygame.draw.rect(
            screen, BLACK,
            (x - 18, y - 52, 36, 33)
        )

        # Face opening
        pygame.draw.rect(
            screen, (215, 165, 120),
            (x - 15, y - 39, 30, 12)
        )

        # Eyes
        pygame.draw.rect(
            screen, BLACK,
            (x - 11, y - 35, 8, 3)
        )

        pygame.draw.rect(
            screen, BLACK,
            (x + 3, y - 35, 8, 3)
        )

        # Red headband
        pygame.draw.rect(
            screen, (190, 35, 45),
            (x - 20, y - 48, 40, 7)
        )