import pygame
from sys import exit
from game_settings import GameSettings


class Game:
    def __init__(self):
        pygame.init()
        self.settings = GameSettings()

        # Creates a screen with a specific resolution and options.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.screen_title)
        self.clock = pygame.time.Clock()

        # Creates surface with background.
        self.background = self.settings.background
        self.background = pygame.transform.scale(self.background, self.screen.get_size())
        self.screen.blit(self.background, (0, 0))

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
            # Draw our elements and update everything.
            pygame.display.update()
            # While True loop run max times per second.
            self.clock.tick(self.settings.max_frame)


if __name__ == '__main__':
    game = Game()
    game.run_game()
