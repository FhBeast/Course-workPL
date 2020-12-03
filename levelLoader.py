import pygame
import os
from entity import Entity
from key import Key
from box import Box
from door import Door
from crystal import Crystal
from level import Level

# Настройка местоположения ассетов
GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, 'img')
BG_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'bg2.jpg'))
WALL_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'wall.jpg'))
WALL_GRASS_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'wall_grass.jpg'))
DOOR_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'door.jpg'))
DOOR_LOCKED_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'door_locked.jpg'))
TABLE_IMG = [pygame.image.load(os.path.join(IMG_FOLDER, 'table_0.png')),
             pygame.image.load(os.path.join(IMG_FOLDER, 'table_1.png')),
             pygame.image.load(os.path.join(IMG_FOLDER, 'table_2.png')),
             pygame.image.load(os.path.join(IMG_FOLDER, 'table_3.png'))]
CRYSTAL_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'crystal.png'))
CRYSTAL_DESTROY_IMG = [pygame.image.load(os.path.join(IMG_FOLDER, 'crystal_1.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'crystal_2.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'crystal_3.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'crystal_4.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'crystal_5.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'crystal_6.png')),
                       pygame.image.load(os.path.join(IMG_FOLDER, 'crystal_7.png'))]
BOX_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'box.png'))
STONE_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'stone.png'))
KEY_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'key.png'))
SHRUB_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'shrub.png'))
PLATFORM_IMG = [pygame.image.load(os.path.join(IMG_FOLDER, 'platform_single.png')),
                pygame.image.load(os.path.join(IMG_FOLDER, 'platform_right.png')),
                pygame.image.load(os.path.join(IMG_FOLDER, 'platform_left.png')),
                pygame.image.load(os.path.join(IMG_FOLDER, 'platform_center.png'))]

WALL_WIDTH = 100
WALL_HEIGHT = 100

PLATFORM_WIDTH = WALL_WIDTH
PLATFORM_HEIGHT = 30

WALL = "="
PLATFORM = "-"
PLAYER = "P"
DOOR = "D"
DOOR_LOCKED = "L"
KEY = "K"
SHRUB = "*"
BOX = "B"
STONE = "#"
CRYSTAL = "+"

TABLE_0 = 0  # Табличка с изображением кнопок вправо и влево
TABLE_1 = 1  # Табличка с изображением кнопки E
TABLE_2 = 2  # Табличка с изображением кнопки вверх
TABLE_3 = 3  # Табличка с изображением кнопки пробел


class LevelLoader:
    @staticmethod
    def load_level(level_map):
        level = Level()

        level.bgImg = BG_IMG

        # Подготавливаем локацию
        x = y = 0  # Координаты
        for row in range(len(level_map)):  # Вся строка
            for col in range(len(level_map[row])):  # Каждый символ
                # Если это стена
                if level_map[row][col] == WALL:
                    # Создаем блок
                    wall_img_temp = WALL_IMG
                    if row:  # Если над ним нет других блоков, накладываем на него текстуру с травой
                        if level_map[row - 1][col] != WALL:
                            wall_img_temp = WALL_GRASS_IMG
                    wall = Entity(x, y, WALL_WIDTH, WALL_HEIGHT, wall_img_temp)
                    level.entities.add(wall)
                    level.platforms.append(wall)

                # Если это платформа
                elif level_map[row][col] == PLATFORM:
                    variant = 0
                    if col:  # Если есть платформа слева
                        if level_map[row][col - 1] == PLATFORM or level_map[row][col - 1] == WALL:
                            variant += 1
                    if col + 1 != len(level_map[row]):  # Если есть платформа справа
                        if level_map[row][col + 1] == PLATFORM or level_map[row][col + 1] == WALL:
                            variant += 2

                    platform = Entity(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM_IMG[variant])

                    level.entities.add(platform)
                    level.platforms.append(platform)

                # Если это куст
                elif level_map[row][col] == SHRUB:
                    shrub = Entity(x, y, 0, 0, SHRUB_IMG)
                    level.entities.add(shrub)

                # Если это табличка №0
                elif level_map[row][col] == str(TABLE_0):
                    table = Entity(x, y, 0, 0, TABLE_IMG[TABLE_0])
                    level.entities.add(table)

                # Если это табличка №1
                elif level_map[row][col] == str(TABLE_1):
                    table = Entity(x, y, 0, 0, TABLE_IMG[TABLE_1])
                    level.entities.add(table)

                # Если это табличка №2
                elif level_map[row][col] == str(TABLE_2):
                    table = Entity(x, y, 0, 0, TABLE_IMG[TABLE_2])
                    level.entities.add(table)

                # Если это табличка №2
                elif level_map[row][col] == str(TABLE_3):
                    table = Entity(x, y, 0, 0, TABLE_IMG[TABLE_3])
                    level.entities.add(table)

                # Если это ящик
                elif level_map[row][col] == BOX:
                    box = Box(x, y, BOX_IMG)
                    level.dynamicEntity.append(box)
                    level.entities_upper.add(box)
                    level.platforms.append(box)

                # Если это камень
                elif level_map[row][col] == STONE:
                    stone = Entity(x, y, WALL_WIDTH, WALL_HEIGHT, STONE_IMG)
                    level.entities.add(stone)
                    level.platforms.append(stone)

                # Если это кристалл
                elif level_map[row][col] == CRYSTAL:
                    crystal = Crystal(x, y, WALL_WIDTH, WALL_HEIGHT, CRYSTAL_IMG, CRYSTAL_DESTROY_IMG)
                    level.dynamicEntity.append(crystal)
                    level.entities.add(crystal)
                    level.platforms.append(crystal)

                # Если это дверь
                elif level_map[row][col] == DOOR:
                    door = Door(x, y, WALL_WIDTH, WALL_HEIGHT, DOOR_IMG)
                    level.dynamicEntity.append(door)
                    level.entities.add(door)
                    if col == len(level_map[row]) - 1:
                        wall = Entity(x + WALL_WIDTH, y, WALL_WIDTH, WALL_HEIGHT, WALL_IMG)
                        level.entities.add(wall)
                        level.platforms.append(wall)
                    elif col == 0:
                        wall = Entity(x - WALL_WIDTH, y, WALL_WIDTH, WALL_HEIGHT, WALL_IMG)
                        level.entities.add(wall)
                        level.platforms.append(wall)

                # Если это запертая дверь
                elif level_map[row][col] == DOOR_LOCKED:
                    door = Door(x, y, WALL_WIDTH, WALL_HEIGHT, DOOR_LOCKED_IMG)
                    door.isLocked = True
                    level.dynamicEntity.append(door)
                    level.entities.add(door)
                    if col == len(level_map[row]) - 1:
                        wall = Entity(x + WALL_WIDTH, y, WALL_WIDTH, WALL_HEIGHT, WALL_IMG)
                        level.entities.add(wall)
                        level.platforms.append(wall)
                    elif col == 0:
                        wall = Entity(x - WALL_WIDTH, y, WALL_WIDTH, WALL_HEIGHT, WALL_IMG)
                        level.entities.add(wall)
                        level.platforms.append(wall)

                # Если это ключ
                elif level_map[row][col] == KEY:
                    key = Key(x, y, KEY_IMG)
                    level.dynamicEntity.append(key)
                    level.entities.add(key)

                # Если это персонаж
                elif level_map[row][col] == PLAYER:
                    level.playerStartPosition = (x + (WALL_WIDTH / 2), y + WALL_HEIGHT)

                x += WALL_WIDTH  # блоки платформы ставятся на ширине блоков
            y += WALL_HEIGHT  # то же самое и с высотой
            x = 0

        return level
