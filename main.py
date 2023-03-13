import pygame
from sys import exit
from game_settings import GameSettings

settings = GameSettings()

pygame.init()
# Creates a screen with a specific resolution and options.
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption(settings.screen_title)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Draw our elements and update everything.
    pygame.display.update()
    # While True loop run max times per second.
    clock.tick(settings.frame)