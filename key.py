import pygame

KEY_WIDTH = 34
KEY_HEIGHT = 18

KEY_X = 50 - (KEY_WIDTH / 2)
KEY_Y = 70 - (KEY_HEIGHT / 2)

class Key(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((KEY_WIDTH, KEY_HEIGHT))
        self.image = image
        self.rect = pygame.Rect(x + KEY_X, y + KEY_Y, KEY_WIDTH, KEY_HEIGHT)
