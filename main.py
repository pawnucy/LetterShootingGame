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

    def run_game(self):
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