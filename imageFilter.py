import pygame

class ImageFilter:
    @staticmethod
    def blur(image, power, quality):
        width = image.get_width()
        height = image.get_height()

        for i in range(quality):
            image = pygame.transform.smoothscale(image, (int(width / power), int(height / power)))
            image = pygame.transform.smoothscale(image, (width, height))

        return image