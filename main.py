import pygame
import random
from sys import exit
from game_settings import GameSettings
from letters import Alphabet


class Score:
    """ Class responsible for score. """
    def __init__(self, settings, screen):
        self.score = 0
        self.settings = settings
        self.screen = screen
        self.level = 1

    def draw(self):
        # Draw score on screen.
        score_font = self.settings.game_font
        score_text = score_font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topright=(self.settings.screen_width - 100, 10))
        self.screen.blit(score_text, score_rect)
        # Draw level on screen.
        level_font = self.settings.game_font
        level_text = level_font.render(f"Level: {self.level}", True, (255, 255, 255))
        level_rect = level_text.get_rect(midtop=(self.settings.screen_width / 2, 10))
        self.screen.blit(level_text, level_rect)

    def update_level(self):
        # Update level every 200 points and increase letters falling speed.
        if self.score % 200 == 0 and self.score != 0:
            self.level += 1
            self.settings.falling_speed += 1


class Lives:
    """ Class responsible for player lives. """
    def __init__(self, settings, screen):
        self.lives = 3
        self.settings = settings
        self.screen = screen

    def draw(self):
        # Draw lives on screen.
        life_font = self.settings.game_font
        life_text = life_font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        life_rect = life_text.get_rect(topleft=(100, 10))
        self.screen.blit(life_text, life_rect)

    def decrease(self):
        # Decrease live when letter touch bottom of the screen.
        self.lives -= 1


class FallingLetter(pygame.sprite.Sprite):
    """ Class responsible for falling letters. """
    def __init__(self, letter, settings, alphabet):
        super().__init__()
        self.alphabet = alphabet
        self.settings = settings
        self.image = self.alphabet.get_letter_image(letter)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, GameSettings().screen_width - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        # Initial speed of falling letters.
        self.rect.y += self.settings.falling_speed

    def hit(self, key, score):
        if key.lower() == self.alphabet.get_letter(self.image).lower():
            # Add points to score when hit
            score.score += self.settings.points
            score.update_level()
            return True
        else:
            return False


class Game:
    """ Class responsible for game logic. """
    def __init__(self):
        pygame.init()
        self.settings = GameSettings()
        self.alphabet = Alphabet()
        # Creates a screen with a specific resolution and options.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.screen_title)
        self.clock = pygame.time.Clock()
        # Creates surface with background.
        self.background = self.settings.background
        self.background = pygame.transform.scale(self.background, self.screen.get_size())
        self.screen.blit(self.background, (0, 0))
        # Create sprite group for falling letters.
        self.falling_letters = pygame.sprite.Group()
        # Create score.
        self.score = Score(self.settings, self.screen)
        self.lives = Lives(self.settings, self.screen)

    def start_game(self):
        # Display logo and "Press space to start" message.
        font = self.settings.start_font
        logo = font.render("LETTER SHOOTER", True, (0, 190, 190))
        logo_rect = logo.get_rect(center=(400, 150))
        text = font.render("Press SPACE to START", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(text, text_rect)
        self.screen.blit(logo, logo_rect)
        pygame.display.update()

        # Wait for space key to be pressed
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                break
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def run_game(self):
        # Main loop of the game.
        self.start_game()  # Wait for space key to start game
        # Start main loop of the game.
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    # Check if pressed key matches any falling letter.
                    for letter in self.falling_letters:
                        if letter.hit(event.unicode, self.score):
                            letter.kill()

            for letter in self.falling_letters:
                # Checks if the letter has touched the bottom edge of the screen.
                if letter.rect.bottom >= self.settings.screen_height:
                    letter.kill()
                    self.lives.decrease()
                # If no lives left, game over.
                if self.lives.lives == 0:
                    self.game_over()

            # Add new letter to the screen at random intervals.
            if random.randint(0, 100) < 3:
                letter = FallingLetter(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), self.settings,
                                       self.alphabet)
                self.falling_letters.add(letter)

            # Draw our elements and update everything.
            self.screen.blit(self.background, (0, 0))
            self.falling_letters.update()
            self.falling_letters.draw(self.screen)
            self.score.draw()
            self.lives.draw()
            pygame.display.update()

            # While True loop run max times per second.
            self.clock.tick(self.settings.max_frame)

    def game_over(self):
        # Game over screen.
        font = self.settings.start_font
        game_over = font.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(game_over, game_over_rect)
        pygame.display.update()

        # Wait for space key to be pressed for restart game.
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.__init__()  # Restart the game
                self.run_game()
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()


if __name__ == '__main__':
    game = Game()
    game.run_game()
