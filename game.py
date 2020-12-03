import pygame
import os
from PIL import Image, ImageFilter
from list_of_level import get_list
from levelLoader import LevelLoader
from player import Player, IMG_FOLDER
from levelController import LevelController
from effect import Effect
from menu import Menu

CONSOLE_NAME = "Game controller"

class Game:

    def __init__(self, width, height):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_icon(pygame.image.load(os.path.join(IMG_FOLDER, 'icon.bmp')))
        pygame.display.set_caption("My Game")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.level_list = get_list()
        self.fps = 60
        self.effect = Effect(width, height)
        self.effects = pygame.sprite.Group()
        self.effects.add(self.effect)
        self.running_game = True
        self.running_level = True

    def runGame(self):
        pygame.mouse.set_visible(False)

        number_level = 0
        
        try:
            f = open('save.bin', 'rb')
            number_level = int(f.read())
            f.close()
            print(f"{CONSOLE_NAME}: Game loaded")
        except Exception:
            print(f"{CONSOLE_NAME}: Failed to open save")

        # Цикл игры
        while self.running_game:

            player = Player()  # Создаем игрока

            level = LevelLoader.load_level(self.level_list[number_level])  # Загружаем уровень
            level.platforms.append(player)
            level.entities_upper.add(player)  # Добавляем игрока в список объектов
            player.rect.midbottom = level.playerStartPosition  # Получаем стартовое местоположение игрока

            # Цикл уровня
            flag_is_complete = False
            self.running_level = True
            while self.running_level:
                # Держим цикл на правильной скорости
                self.clock.tick(self.fps)

                # По умолчанию - стоим и не прыгаем
                left = right = False
                jump = False
                use = False
                attack = False

                # Проверяем одиночные нажатия клавиш
                # События
                for event in pygame.event.get():
                    # Проверяем закрыли ли мы окно
                    if event.type == pygame.QUIT:
                        self.closeGame()

                    # Управление
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_e:
                            use = True
                        if event.key == pygame.K_SPACE:
                            attack = True
                        if event.key == pygame.K_ESCAPE:
                            sub = self.screen.subsurface(pygame.Rect(0, 0, self.width, self.height))
                            bg = pygame.Surface((1200, 800))
                            bg.blit(sub, (0, 0))

                            if Menu.mainMenu(self.screen, self.fps, bg) == "Quit":
                                self.closeGame()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    left = True
                if keys[pygame.K_d]:
                    right = True
                if keys[pygame.K_w]:
                    jump = True

                # Обновление
                level.particles.update()
                player.update(left, right, jump, attack, level.platforms)  # Обновляем игрока
                LevelController.updateLevel(player, level, use)  # Обновляем логику уровня
                if level.isComplete and not flag_is_complete:
                    print(f"{CONSOLE_NAME}: Level completed")
                    self.effect.blackout()
                    flag_is_complete = True
                if self.effect.update():
                    self.nextLevel()

                # Рендеринг
                # Фон
                self.screen.blit(level.bgImg, (0, 0))

                # Объекты
                level.entities.draw(self.screen)
                level.entities_upper.draw(self.screen)
                level.particles.draw(self.screen)
                self.effects.draw(self.screen)

                # Обновляем экран
                pygame.display.update()

            if number_level + 1 < len(self.level_list) and self.running_game:
                number_level += 1
            else:
                print(f"{CONSOLE_NAME}: Game completed")
                self.closeGame()

        try:
            f = open('save.bin', 'wb')
            f.write(str(number_level).encode())
            f.close()
            print(f"{CONSOLE_NAME}: Game saved")
        except Exception:
            print(f"{CONSOLE_NAME}: Failed to save game")

    def closeGame(self):
        self.running_level = False
        self.running_game = False

    def nextLevel(self):
        self.running_level = False
