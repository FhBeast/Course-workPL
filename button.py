import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, image_default, image_select, number):
        pygame.sprite.Sprite.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image = image_default
        self.image_default = image_default
        self.image_select = image_select
        self.rect = pygame.Rect(x, y, width, height)
        self.selected = False
        self.number = number

    def select(self):
        self.selected = True

    def remove_select(self):
        self.selected = False

    def update(self):
        if self.selected:
            self.image = self.image_select
        else:
            self.image = self.image_default

    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, value):
        self.__selected = value
