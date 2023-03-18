import pygame


class GameSettings:
    """ class responsible for game settings. """
    def __init__(self):
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.screen_title = 'Letter Shooter'

        # Game settings.
        self.max_frame = 30
        self.falling_speed = 5
        self.points = 10 # Points awarded per letter.
        self.lives = 3 # Number of initial lives of the player.

        # Font
        self.start_font = pygame.font.Font('graphics/font/PixelFont.ttf', 26)
        self.game_font = pygame.font.Font('graphics/font/PixelFont.ttf', 20)
        self.game_over_font = pygame.font.Font('graphics/font/PixelFont.ttf', 30)

        # Paths to graphics
        self.background = pygame.image.load('graphics/dark_background.png')
