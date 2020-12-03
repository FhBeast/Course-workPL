import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, image_default, image_select):
        pygame.sprite.Sprite.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image = image_default
        self.image_default = image_default
        self.image_select = image_select
        self.rect = pygame.Rect(x, y, width, height)
        self.selected = False

    def select(self):
        self.selected = True

    def update(self):
        if self.selected:
            self.image = self.image_select
        else:
            self.image = self.image_default

        self.selected = False
