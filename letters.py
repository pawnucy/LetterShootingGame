import pygame


class Alphabet:
    """ Class responsible for letters images. """
    def __init__(self):
        self.alphabet_images = {}
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            filename = f"graphics/letters/{letter}.png"
            image = pygame.image.load(filename)
            # Change size of letters images.
            image = pygame.transform.scale(image, (image.get_width() // 4, image.get_height() // 4))
            self.alphabet_images[letter] = image

    def get_letter_image(self, letter):
        # Get image of letter.
        return self.alphabet_images.get(letter.upper())

    def get_letter(self, image):
        # Get the letter associated with a given image.
        for letter, img in self.alphabet_images.items():
            if img == image:
                return letter
        return None
