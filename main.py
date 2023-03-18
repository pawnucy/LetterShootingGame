import pygame
import random
from sys import exit
from game_settings import GameSettings
from letters import Alphabet


class Score:
    def __init__(self, settings, screen):
        self.score = 0
        self.settings = settings
        self.screen = screen

    def update(self):
        score_font = self.settings.game_font
        score_text = score_font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topright=(self.settings.screen_width - 100, 10))
        self.screen.blit(score_text, score_rect)

class FallingLetter(pygame.sprite.Sprite):
    """ Function responsible for falling letters. """
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
           score.score  += self.settings.points  # Add 10 points to score
           return True
        else:
            return False


class Game:
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

            # Add new letter to the screen at random intervals.
            if random.randint(0, 100) < 3:
                letter = FallingLetter(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), self.settings,
                                       self.alphabet)
                self.falling_letters.add(letter)

            # Draw our elements and update everything.
            self.screen.blit(self.background, (0, 0))
            self.falling_letters.update()
            self.falling_letters.draw(self.screen)
            self.score.update()
            pygame.display.update()
            # While True loop run max times per second.
            self.clock.tick(self.settings.max_frame)


if __name__ == '__main__':
    game = Game()
    game.run_game()
