import pygame
import os

RUN_SPEED = 10
WIDTH = 52
HEIGHT = 90
JUMP_POWER = 17
GRAVITY = 0.7  # Гравитация
ATTACK_COOLDOWN = 15
ADD_SPEED_DECELERATION = 1

GAME_FOLDER = os.path.dirname(__file__)  # Таков путь к каталогу с файлами
IMG_FOLDER = os.path.join(GAME_FOLDER, 'img')

ANIMATION_DECELERATION = 3

ANIMATION_STAY_RIGHT = pygame.image.load(os.path.join(IMG_FOLDER, 'idle.png'))
ANIMATION_STAY_LEFT = pygame.transform.flip(ANIMATION_STAY_RIGHT, True, False)
ANIMATION_JUMP_RIGHT = pygame.image.load(os.path.join(IMG_FOLDER, 'idle_jump.png'))
ANIMATION_JUMP_LEFT = pygame.transform.flip(ANIMATION_JUMP_RIGHT, True, False)
ANIMATION_FALL_RIGHT = pygame.image.load(os.path.join(IMG_FOLDER, 'idle_fall.png'))
ANIMATION_FALL_LEFT = pygame.transform.flip(ANIMATION_FALL_RIGHT, True, False)
ANIMATION_RUN_RIGHT = [pygame.image.load(os.path.join(IMG_FOLDER, 'idle_run.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'idle_run2.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'idle_run3.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'idle_run4.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'idle_run5.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'idle_run6.png'))]
ANIMATION_RUN_LEFT = [pygame.transform.flip(image, True, False) for image in ANIMATION_RUN_RIGHT]

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 0
        self.speedFall = 0
        self.__lookRight = True
        self.fall = True
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
        self.frame = 0  # необходимо для анимации
        self.__attackNow = False
        self.__attackCooldown = 0
        self.__key = False

    def update(self, left, right, jump, attack, platforms):

        if jump:  # Прыжок
            if not self.fall:
                self.speedFall = -JUMP_POWER
            if self.__lookRight:
                self.image = ANIMATION_JUMP_RIGHT
            else:
                self.image = ANIMATION_JUMP_LEFT

        if left:  # идем влево
            self.__lookRight = False
            self.speed = -RUN_SPEED
            self.image = ANIMATION_RUN_LEFT[self.frame // ANIMATION_DECELERATION]

        if right:  # идем вправо
            self.__lookRight = True
            self.speed = RUN_SPEED
            self.image = ANIMATION_RUN_RIGHT[self.frame // ANIMATION_DECELERATION]

        if not (left or right):  # стоим, когда не идем
            self.speed = 0
            if not jump:
                if self.__lookRight:
                    self.image = ANIMATION_STAY_RIGHT
                else:
                    self.image = ANIMATION_STAY_LEFT
        else:
            if self.frame + 1 != len(ANIMATION_RUN_RIGHT) * ANIMATION_DECELERATION:  # Меняем кадр анимации если бежим
                self.frame += 1
            else:
                self.frame = 0

        if self.speedFall > GRAVITY:  # Если падаем, то одна анимация
            if self.__lookRight:
                self.image = ANIMATION_FALL_RIGHT
            else:
                self.image = ANIMATION_FALL_LEFT
        elif self.speedFall < 0:  # Если летим вверх, то другая
            if self.__lookRight:
                self.image = ANIMATION_JUMP_RIGHT
            else:
                self.image = ANIMATION_JUMP_LEFT

        if self.fall:  # Если падаем, то увеличиваем скорость падения
            self.speedFall += GRAVITY

        self.fall = True  # Падаем каждый раз. Если падать не нужно, коллайдеры это исправят

        self.__attackNow = False  # Обработка атаки
        if attack:
            if not self.__attackCooldown:
                self.__attackCooldown = ATTACK_COOLDOWN
                self.__attackNow = True
        if self.__attackCooldown > 0:
            self.__attackCooldown -= 1

        self.rect.y += self.speedFall  # Двигаемся по оси y
        self.collide(0, self.speedFall, platforms)  # Проверяем пересекаемся ли мы с чем-нибудь

        self.rect.x += self.speed  # Двигаемся по оси x
        self.collide(self.speed, 0, platforms)  # Проверяем пересекаемся ли мы с чем-нибудь

    def collide(self, speed_x, speed_y, platforms):
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform) and platform != self:  # Если есть пересечение

                if speed_x > 0:  # Если двигались вправо
                    self.rect.right = platform.rect.left  # То возвращаем игрока обратно

                if speed_x < 0:  # Если двигались влево
                    self.rect.left = platform.rect.right  # То возвращаем игрока обратно тоже

                if speed_y > 0:  # Если падали вниз
                    self.rect.bottom = platform.rect.top  # То возвращаем игрока на платформу
                    self.fall = False  # Отключаем падение
                    self.speedFall = 0  # Скорость падения обнуляется

                if speed_y < 0:  # Если двигались вверх
                    self.rect.top = platform.rect.bottom  # То не поднимаем игрока дальше
                    self.speedFall = 0  # Скорость падения обнуляется

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value):
        self.__key = value

    @property
    def attack(self):
        return self.__attackNow

    @attack.setter
    def attack(self, value):
        self.__attackNow = value

    @property
    def lookRight(self):
        return self.__lookRight

    @lookRight.setter
    def lookRight(self, value):
        self.__lookRight = value
