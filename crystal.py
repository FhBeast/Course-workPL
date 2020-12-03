import pygame

class Crystal(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, image, destroy_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image = image
        self.images = destroy_img
        self.rect = pygame.Rect(x, y, width, height)
        self.__isDestroy = False
        self.frame = 0

    def destroy(self):
        self.__isDestroy = True

    def update(self):
        if self.__isDestroy:
            if not self.frame + 1 >= len(self.images):  # Меняем кадр анимации частицы
                self.frame += 1
            else:
                self.kill()

            self.image = self.images[self.frame]

    @property
    def isDestroy(self):
        return self.__isDestroy
