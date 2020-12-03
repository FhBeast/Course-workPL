import pygame

class Level:

    def __init__(self):
        self.__entities = pygame.sprite.Group()
        self.__entities_upper = pygame.sprite.Group()
        self.__particles = pygame.sprite.Group()
        self.__dynamicEntity = []
        self.__platforms = []
        self.__bgImg = None
        self.__playerStartPosition = ()
        self.__isComplete = False

    @property
    def particles(self):
        return self.__particles

    @particles.setter
    def particles(self, value):
        self.__particles = value

    @property
    def entities(self):
        return self.__entities

    @entities.setter
    def entities(self, value):
        self.__entities = value

    @property
    def entities_upper(self):
        return self.__entities_upper

    @entities_upper.setter
    def entities_upper(self, value):
        self.__entities_upper = value

    @property
    def dynamicEntity(self):
        return self.__dynamicEntity

    @dynamicEntity.setter
    def dynamicEntity(self, value):
        self.__dynamicEntity = value

    @property
    def platforms(self):
        return self.__platforms

    @platforms.setter
    def platforms(self, value):
        self.__platforms = value

    @property
    def bgImg(self):
        return self.__bgImg

    @bgImg.setter
    def bgImg(self, value):
        self.__bgImg = value

    @property
    def playerStartPosition(self):
        return self.__playerStartPosition

    @playerStartPosition.setter
    def playerStartPosition(self, value):
        self.__playerStartPosition = value

    @property
    def isComplete(self):
        return self.__isComplete

    def complete(self):
        self.__isComplete = True
