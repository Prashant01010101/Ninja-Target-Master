
import pygame
import random
from pathlib import Path

from settings import WIDTH, HEIGHT, FPS
from settings import DARK, WALL, WOOD, WOOD_LINE
from settings import BEAM, GOLD, BLACK


from ninja import Ninja


from shuriken import Shuriken


from targets import Target, FastTarget
from targets import GoldenTarget, DangerTarget

from scoreboard import ScoreBoard 


from level import Level



class Game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )

        pygame.display.set_caption(
            "Ninja Target Master - Step 1"
        )

        # Optional arcade sound effects (game still runs without audio).
        self.sounds = {}
        sound_folder = Path(__file__).resolve().parent / "sounds"
        if pygame.mixer.get_init():
            for name in ("throw", "hit", "win"):
                try:
                    self.sounds[name] = pygame.mixer.Sound(
                        str(sound_folder / f"{name}.wav")
                    )
                    self.sounds[name].set_volume(0.35)
                except (pygame.error, OSError):
                    pass

        self.clock = pygame.time.Clock()
        self.running = True
        self.ninja = Ninja(WIDTH // 2, 550)
        self.shurikens = []

        self.scoreboard = ScoreBoard()
        self.game_over = False
        self.won = False
        self.targets = []
        self.level = Level(1)
        self.setup_level()
        self.state = "menu"


    def play_sound(self, name):
        sound = self.sounds.get(name)
        if sound:
            sound.play()

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_r:

                    self.level = Level(1)
                    self.setup_level()
                    self.state = "playing"

                if event.key == pygame.K_SPACE:

                    if self.state == "result" and self.won:

                        if self.level.number < 3:

                            self.level = Level(
                                self.level.number + 1
                            )

                            self.setup_level()
                            self.state = "playing"

                if event.key == pygame.K_RETURN:

                    if self.state == "menu":

                        self.state = "playing"

                if event.key == pygame.K_p:

                    if self.state == "playing":
                        self.state = "paused"

                    elif self.state == "paused":
                        self.state = "playing"

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1 and self.state == "playing":

                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    new_shuriken = Shuriken(
                        self.ninja.x,
                        self.ninja.y - 15,
                        mouse_x,
                        mouse_y
                    )

                    self.shurikens.append(new_shuriken)
                    self.play_sound("throw")

    def draw_dojo(self):

        # Background wall
        self.screen.fill(WALL)

        # Vertical wooden beams
        for x in range(0, WIDTH, 160):
            pygame.draw.rect(
                self.screen,
                BEAM,
                (x, 0, 18, 440)
            )

        # Horizontal wooden beams
        pygame.draw.rect(
            self.screen,
            BEAM,
            (0, 90, WIDTH, 18)
        )

        pygame.draw.rect(
            self.screen,
            BEAM,
            (0, 420, WIDTH, 20)
        )

        # Wooden floor
        pygame.draw.rect(
            self.screen,
            WOOD,
            (0, 440, WIDTH, 200)
        )

        # Floor plank lines
        for y in range(440, HEIGHT, 40):
            pygame.draw.line(
                self.screen,
                WOOD_LINE,
                (0, y),
                (WIDTH, y),
                2
            )

        # Training area
        pygame.draw.rect(
            self.screen,
            BLACK,
            (330, 485, 300, 90)
        )

        pygame.draw.rect(
            self.screen,
            GOLD,
            (330, 485, 300, 90),
            3
        )

        # Title
        font = pygame.font.SysFont(
            "arial",
            42,
            bold=True
        )

        title = font.render(
            "NINJA TARGET MASTER",
            True,
            GOLD
        )

        title_rect = title.get_rect(
            center=(WIDTH // 2, 50)
        )

        self.screen.blit(title, title_rect)

    
    
    def update_shurikens(self):

        for shuriken in self.shurikens[:]:

            shuriken.move()

            # Remove shuriken if it leaves the screen
            if shuriken.is_off_screen():
                self.shurikens.remove(shuriken)
                self.scoreboard.add_miss()
                continue
            

            # Check if shuriken hits a target
            for target in self.targets[:]:

                if target.is_hit(shuriken):

                    self.targets.remove(target)
                    self.shurikens.remove(shuriken)

                    self.scoreboard.add_points(
                    target.get_points()
                    )

                    self.scoreboard.add_hit()
                    self.play_sound("hit")

                    self.targets.append(
                        self.create_target()
                    )

                    break

    
    
    def create_target(self):

        x = random.randint(80, WIDTH - 80)
        y = random.choice([150, 260, 370])

        if self.level.number == 1:

            speed = random.choice([-2, 2])
            return Target(x, y, speed)

        elif self.level.number == 2:

            target_type = random.randint(1, 4)
            speed = random.choice([-4, 4])

            if target_type == 1:
                return GoldenTarget(x, y, speed)

            return FastTarget(x, y, speed)

        else:

            target_type = random.randint(1, 5)
            speed = random.choice([-5, -4, 4, 5])

            if target_type == 1:
                return GoldenTarget(x, y, speed)

            elif target_type == 2:
                return DangerTarget(x, y, speed)

            return FastTarget(x, y, speed)



    def setup_level(self):

        self.scoreboard.score = 0
        self.scoreboard.goal = self.level.goal
        self.scoreboard.time_left = self.level.time_limit
        self.scoreboard.hits = 0
        self.scoreboard.misses = 0

        self.game_over = False
        self.won = False

        self.shurikens = []
        self.targets = []

        self.ninja.x = WIDTH // 2
        self.ninja.y = 550

        for i in range(3):
            self.targets.append(self.create_target())



    def update_targets(self):

        for target in self.targets:
            target.move()

    
    def draw_menu(self):

        # Background
        self.screen.fill((55, 42, 38))

        title_font = pygame.font.SysFont(
            "arial", 55, bold=True
        )

        text_font = pygame.font.SysFont(
            "arial", 26
        )

        small_font = pygame.font.SysFont(
            "arial", 22
        )

        # Main title
        title = title_font.render(
            "NINJA TARGET MASTER",
            True,
            GOLD
        )

        title_rect = title.get_rect(
            center=(WIDTH // 2, 130)
        )

        self.screen.blit(title, title_rect)

        # Decorative wooden panel
        pygame.draw.rect(
            self.screen,
            (35, 30, 35),
            (180, 220, 600, 300)
        )

        pygame.draw.rect(
            self.screen,
            GOLD,
            (180, 220, 600, 300),
            4
        )

        # Instructions
        instructions = [
            "WASD / Arrow Keys - Move",
            "Left Mouse Click - Throw Shuriken",
            "Hit targets to earn points",
            "Avoid red danger targets",
            "Complete all 3 levels!"
        ]

        y = 260

        for instruction in instructions:

            text = small_font.render(
                instruction,
                True,
                (255, 255, 255)
            )

            text_rect = text.get_rect(
                center=(WIDTH // 2, y)
            )

            self.screen.blit(text, text_rect)

            y += 42

        # Start message
        start_text = text_font.render(
            "PRESS ENTER TO START",
            True,
            GOLD
        )

        start_rect = start_text.get_rect(
            center=(WIDTH // 2, 570)
        )

        self.screen.blit(start_text, start_rect)

    
    def draw_pause(self):

        pygame.draw.rect(
            self.screen,
            (25, 25, 35),
            (230, 200, 500, 250)
        )

        pygame.draw.rect(
            self.screen,
            GOLD,
            (230, 200, 500, 250),
            4
        )

        title_font = pygame.font.SysFont(
            "arial", 45, bold=True
        )

        text_font = pygame.font.SysFont(
            "arial", 25
        )

        title = title_font.render(
            "GAME PAUSED",
            True,
            GOLD
        )

        hits = text_font.render(
            f"Hits: {self.scoreboard.hits}",
            True,
            (255, 255, 255)
        )

        misses = text_font.render(
            f"Misses: {self.scoreboard.misses}",
            True,
            (255, 255, 255)
        )

        accuracy = text_font.render(
            f"Accuracy: {self.scoreboard.get_accuracy():.1f}%",
            True,
            (255, 255, 255)
        )

        instruction = text_font.render(
            "Press P to Resume",
            True,
            GOLD
        )

        texts = [
            (title, 250),
            (hits, 310),
            (misses, 345),
            (accuracy, 380),
            (instruction, 420)
        ]

        for text, y in texts:

            rect = text.get_rect(
                center=(WIDTH // 2, y)
            )

            self.screen.blit(text, rect)


    
    def draw_result(self):

        pygame.draw.rect(
            self.screen,
            (25, 25, 35),
            (180, 200, 600, 250)
        )

        pygame.draw.rect(
            self.screen,
            GOLD,
            (180, 200, 600, 250),
            4
        )

        font = pygame.font.SysFont(
            "arial", 42, bold=True
        )

        small_font = pygame.font.SysFont(
            "arial", 25
        )

        if self.won:

            if self.level.number == 3:
                message = "NINJA MASTER!"
                instruction = "Press R to play again"

            else:
                message = "LEVEL COMPLETE!"
                instruction = "Press SPACE for next level"

        else:
            message = "TIME'S UP!"
            instruction = "Press R to restart"

        title = font.render(
            message, True, GOLD
        )

        score = small_font.render(
            f"Final Score: {self.scoreboard.score}",
            True, (255, 255, 255)
        )

        accuracy = small_font.render(
            f"Accuracy: {self.scoreboard.get_accuracy():.1f}%",
            True, (255, 255, 255)
        )

        next_text = small_font.render(
            instruction,
            True, (255, 255, 255)
        )

        title_rect = title.get_rect(
            center=(WIDTH // 2, 265)
        )

        score_rect = score.get_rect(
            center=(WIDTH // 2, 325)
        )

        next_rect = next_text.get_rect(
            center=(WIDTH // 2, 415)
        )

        self.screen.blit(title, title_rect)
        self.screen.blit(score, score_rect)
        accuracy_rect = accuracy.get_rect(
            center=(WIDTH // 2, 355)
        )

        self.screen.blit(accuracy, accuracy_rect)
        self.screen.blit(next_text, next_rect)




    
    def run(self):

        while self.running:

            seconds = self.clock.tick(FPS) / 1000

            self.handle_events()

            if self.state == "menu":

                self.draw_menu()

            else:

                if self.state == "playing":

                    self.ninja.move()

                    self.update_targets()

                    self.update_shurikens()

                    self.scoreboard.update_time(seconds)

                    if self.scoreboard.is_winner():
                        self.game_over = True
                        self.won = True
                        self.play_sound("win")
                        self.state = "result"

                    elif self.scoreboard.is_time_up():
                        self.game_over = True
                        self.won = False
                        self.state = "result"

                self.draw_dojo()

                for target in self.targets:
                    target.draw(self.screen)

                self.ninja.draw(self.screen)

                for shuriken in self.shurikens:
                    shuriken.draw(self.screen)

                self.scoreboard.draw(
                    self.screen,
                    self.level.number
                )

                if self.state == "paused":
                    self.draw_pause()

                if self.state == "result":
                    self.draw_result()

            pygame.display.flip()

        pygame.quit()



if __name__ == "__main__":
    game = Game()
    game.run()
