import pygame


class GameSettings:
    """ class responsible for game settings. """
    def __init__(self):
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.screen_title = 'Letter Shooter'

        # Game settings
        self.max_frame = 60

        # Graphics
        self.background = pygame.image.load('graphics/dark_background.png')
