import pygame
import os
from key import Key
from door import Door
from box import Box
from crystal import Crystal
from levelLoader import DOOR_IMG
from particle import Particle

GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, 'img')
ATTACK_IMG = [pygame.image.load(os.path.join(IMG_FOLDER, 'attack_1.png')),
              pygame.image.load(os.path.join(IMG_FOLDER, 'attack_2.png')),
              pygame.image.load(os.path.join(IMG_FOLDER, 'attack_3.png'))]

CONSOLE_NAME = "Level controller"

class LevelController:
    @staticmethod
    def updateLevel(player, level, use):
        attack_zone = None

        if player.attack:  # Если игрок толкает что-либо
            attack_zone = Particle(0, 0, 50, 90, ATTACK_IMG)
            level.particles.add(attack_zone)
            if player.lookRight:
                attack_zone.rect.topleft = player.rect.topright
            elif not player.lookRight:
                attack_zone.rect.topright = player.rect.topleft
                attack_zone.reverse()

        for entity in level.dynamicEntity:
            if pygame.sprite.collide_rect(player, entity):  # Если есть пересечение с игроком
                if isinstance(entity, Key):  # С ключом
                    player.key = True
                    entity.remove(level.entities)
                    level.dynamicEntity.remove(entity)
                    print(f"{CONSOLE_NAME}: Key has been picked")

                if isinstance(entity, Door):  # С дверью
                    if entity.isLocked:
                        if player.key:
                            player.key = False
                            entity.isLocked = False
                            entity.image = DOOR_IMG
                            print(f"{CONSOLE_NAME}: Door has been unlocked")
                    else:
                        if use:
                            level.complete()

            if isinstance(entity, Box):
                if player.attack and pygame.sprite.collide_rect(attack_zone, entity):
                    entity.push(player.lookRight)

                entity.update(level.platforms)

            if isinstance(entity, Crystal):
                if player.attack and pygame.sprite.collide_rect(attack_zone, entity):
                    if not entity.isDestroy:
                        level.platforms.remove(entity)
                    entity.destroy()

                entity.update()
