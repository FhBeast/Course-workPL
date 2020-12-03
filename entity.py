import pygame

class Entity(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image = image
        self.rect = pygame.Rect(x, y, width, height)
