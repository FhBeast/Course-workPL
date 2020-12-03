import pygame

class Door(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image = image
        self.rect = pygame.Rect(x, y, width, height)
        self.__isLocked = False

    @property
    def isLocked(self):
        return self.__isLocked

    @isLocked.setter
    def isLocked(self, value):
        self.__isLocked = value
