import pygame

class Particle(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, images):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.images = images
        self.imagesReverse = [pygame.transform.flip(image, True, False) for image in images]
        self.image = images[0]
        self.frame = 0
        self.rect = pygame.Rect(x, y, width, height)

    def update(self):
        if self.frame + 1 != len(self.images):  # Меняем кадр анимации частицы
            self.frame += 1
        else:
            self.kill()

        self.image = self.images[self.frame]

    def reverse(self):
        self.images = self.imagesReverse
        self.image = self.imagesReverse[0]
