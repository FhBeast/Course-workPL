import pygame

DECAY_SPEED = 10

class Effect(pygame.sprite.Sprite):

    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(0)
        self.image.set_alpha(0)
        self.rect = pygame.Rect(0, 0, width, height)
        self.isBlackout = False
        self.isDecay = True
        self.frame = 0

    def blackout(self):
        self.isBlackout = True

    def update(self):
        if self.isBlackout:
            if self.isDecay:
                self.frame += DECAY_SPEED
                if self.frame > 255:
                    self.frame = 255
                    self.isDecay = False
                    self.image.set_alpha(self.frame)
                    return True
            else:
                self.frame -= DECAY_SPEED
                if self.frame < 0:
                    self.frame = 0
                    self.isDecay = True
                    self.isBlackout = False
            self.image.set_alpha(self.frame)
            return False
