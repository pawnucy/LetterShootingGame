import pygame


class GameSettings:
    """ class responsible for game settings. """
    def __init__(self):
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.screen_title = 'Letter Shooter'

        # Game settings.
        self.max_frame = 60

        # Font
        self.start_font = pygame.font.Font('graphics/font/PixelFont.ttf', 26)

        # Paths to graphics
        self.background = pygame.image.load('graphics/dark_background.png')
