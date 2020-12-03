import pygame

PUSH_SPEED = 20
DECELERATION_RATE = 0.7
GRAVITY = 0.7

WIDTH = 100
HEIGHT = 100

class Box(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.image = image
        self.speed = 0
        self.speedFall = 0
        self.fall = False

    def update(self, platforms):
        if self.speed > 0:
            if self.speed < DECELERATION_RATE:
                self.speed = 0
            else:
                self.speed -= DECELERATION_RATE
        elif self.speed < 0:
            if self.speed > -DECELERATION_RATE:
                self.speed = 0
            else:
                self.speed += DECELERATION_RATE

        if self.fall:
            self.speedFall += GRAVITY

        self.fall = True

        self.rect.y += self.speedFall  # Двигаемся по оси y
        self.collide(0, self.speedFall, platforms)  # Проверяем пересекаемся ли мы с чем-нибудь

        self.rect.x += self.speed  # Двигаемся по оси x
        self.collide(self.speed, 0, platforms)  # Проверяем пересекаемся ли мы с чем-нибудь

    def push(self, right=True):
        if right:
            self.speed = PUSH_SPEED
        else:
            self.speed = -PUSH_SPEED

    def collide(self, speed_x, speed_y, platforms):
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform) and platform != self:  # Если есть пересечение

                if speed_x > 0:  # Если двигались вправо
                    self.rect.right = platform.rect.left  # То возвращаем игрока обратно
                    self.speed = 0

                if speed_x < 0:  # Если двигались влево
                    self.rect.left = platform.rect.right  # То возвращаем игрока обратно тоже
                    self.speed = 0

                if speed_y > 0:  # Если падали вниз
                    self.rect.bottom = platform.rect.top  # То возвращаем игрока на платформу
                    self.fall = False  # Отключаем падение
                    self.speedFall = 0  # Скорость падения обнуляется

                if speed_y < 0:  # Если двигались вверх
                    self.rect.top = platform.rect.bottom  # То не поднимаем игрока дальше
                    self.speedFall = 0  # Скорость падения обнуляется
