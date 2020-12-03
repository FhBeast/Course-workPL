import pygame
import os
from entity import Entity
from button import Button

FORM_WIDTH = 500
FORM_HEIGHT = 538
BUTTON_WIDTH = 354
BUTTON_HEIGHT = 89

GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, 'img')
BG_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'bg.jpg'))
FORM_MENU_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'form_menu.png'))
BUTTON_CONTINUE_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'button_continue.png'))
BUTTON_CONTINUE_S_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'button_continue_s.png'))
BUTTON_NEW_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'button_new.png'))
BUTTON_NEW_S_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'button_new_s.png'))
BUTTON_RESTART_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'button_restart.png'))
BUTTON_RESTART_S_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'button_restart_s.png'))
BUTTON_EXIT_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'button_exit.png'))
BUTTON_EXIT_S_IMG = pygame.image.load(os.path.join(IMG_FOLDER, 'button_exit_s.png'))

class Menu:
    @staticmethod
    def pauseMenu(screen, fps, bg):
        clock = pygame.time.Clock()
        result = "Continue"

        pygame.mouse.set_visible(True)
        menu_elements = pygame.sprite.Group()
        buttons = []
        form_menu = Entity(350, 130, FORM_WIDTH, FORM_HEIGHT, FORM_MENU_IMG)
        menu_elements.add(form_menu)
        button = Button(423, 250, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_CONTINUE_IMG, BUTTON_CONTINUE_S_IMG, 0)
        menu_elements.add(button)
        buttons.append(button)
        button = Button(423, 370, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_RESTART_IMG, BUTTON_RESTART_S_IMG, 1)
        menu_elements.add(button)
        buttons.append(button)
        button = Button(423, 490, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_EXIT_IMG, BUTTON_EXIT_S_IMG, 2)
        menu_elements.add(button)
        buttons.append(button)

        menu_is_open = True
        while menu_is_open:
            # Держим цикл на правильной скорости
            clock.tick(fps)

            # События
            for event in pygame.event.get():
                # Проверяем закрыли ли мы окно
                if event.type == pygame.QUIT:
                    menu_is_open = False
                    result = "Quit"

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu_is_open = False
                        result = "Continue"

                elif event.type == pygame.MOUSEMOTION:
                    for button in buttons:
                        mouse_col = pygame.sprite.Sprite()
                        mouse_col.rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                        if pygame.sprite.collide_rect(mouse_col, button):
                            button.select()
                        else:
                            button.remove_select()
                elif event.type == pygame.MOUSEBUTTONUP:
                    for button in buttons:
                        mouse_col = pygame.sprite.Sprite()
                        mouse_col.rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                        if pygame.sprite.collide_rect(mouse_col, button):
                            if button.number == 0:
                                menu_is_open = False
                                result = "Continue"
                            elif button.number == 1:
                                menu_is_open = False
                                result = "Restart"
                            elif button.number == 2:
                                menu_is_open = False
                                result = "Quit"

            # Обновление
            menu_elements.update()

            # Рендеринг
            screen.blit(bg, (0, 0))
            menu_elements.draw(screen)

            # Обновляем экран
            pygame.display.update()

        return result

    @staticmethod
    def mainMenu(screen, fps):
        clock = pygame.time.Clock()
        result = "Continue"

        pygame.mouse.set_visible(True)
        menu_elements = pygame.sprite.Group()
        buttons = []
        button = Button(423, 250, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_CONTINUE_IMG, BUTTON_CONTINUE_S_IMG, 0)
        menu_elements.add(button)
        buttons.append(button)
        button = Button(423, 370, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_NEW_IMG, BUTTON_NEW_S_IMG, 1)
        menu_elements.add(button)
        buttons.append(button)
        button = Button(423, 490, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_EXIT_IMG, BUTTON_EXIT_S_IMG, 2)
        menu_elements.add(button)
        buttons.append(button)

        menu_is_open = True
        while menu_is_open:
            # Держим цикл на правильной скорости
            clock.tick(fps)

            # События
            for event in pygame.event.get():
                # Проверяем закрыли ли мы окно
                if event.type == pygame.QUIT:
                    menu_is_open = False
                    result = "Quit"

                elif event.type == pygame.MOUSEMOTION:
                    for button in buttons:
                        mouse_col = pygame.sprite.Sprite()
                        mouse_col.rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                        if pygame.sprite.collide_rect(mouse_col, button):
                            button.select()
                        else:
                            button.remove_select()
                elif event.type == pygame.MOUSEBUTTONUP:
                    for button in buttons:
                        mouse_col = pygame.sprite.Sprite()
                        mouse_col.rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                        if pygame.sprite.collide_rect(mouse_col, button):
                            if button.number == 0:
                                menu_is_open = False
                                result = "Continue"
                            elif button.number == 1:
                                menu_is_open = False
                                result = "New game"
                            elif button.number == 2:
                                menu_is_open = False
                                result = "Quit"

            # Обновление
            menu_elements.update()

            # Рендеринг
            screen.blit(BG_IMG, (0, 0))
            menu_elements.draw(screen)

            # Обновляем экран
            pygame.display.update()

        return result
