import pygame

class Alphabet:
    """ Class responsible for letters images. """
    def __init__(self):
        self.alphabet_images = {}
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            filename = f"graphics/letters/{letter}.png"
            self.alphabet_images[letter] = pygame.image.load(filename)

    def get_letter_image(self, letter):
        # Get image of letter.
        return self.alphabet_images.get(letter.upper())
