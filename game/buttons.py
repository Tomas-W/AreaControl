import time

import pygame

from settings.general_settings import GENERAL
from settings.menu_settings import DISPLAY


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.spawn_time = time.time()

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            self.image.set_alpha(255)
            if pygame.mouse.get_pressed()[
                0] == 1 and not self.clicked and time.time() - self.spawn_time > 0.5:
                self.spawn_time = time.time()
                self.clicked = True
                action = True
        else:
            self.image.set_alpha(175)

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


# Buttons
first_button_x = 0.62 * GENERAL["width"]
first_button_y = 0.144 * GENERAL["width"]
play_button_image = pygame.image.load(DISPLAY["play_btn_img"]).convert_alpha()
play_button = Button(x=first_button_x,
                     y=first_button_y,
                     image=play_button_image,
                     scale=1)

settings_button_image = pygame.image.load(DISPLAY["settings_btn_img"]).convert_alpha()
settings_button = Button(x=first_button_x,
                         y=first_button_y + 90,
                         image=settings_button_image,
                         scale=1)

leaderboard_button_image = pygame.image.load(
    DISPLAY["leaderboard_btn_img"]).convert_alpha()
leaderboard_button = Button(x=first_button_x,
                            y=first_button_y + 180,
                            image=leaderboard_button_image,
                            scale=1)

credits_button_image = pygame.image.load(
    DISPLAY["credits_btn_img"]).convert_alpha()
credits_button = Button(x=first_button_x,
                        y=first_button_y + 270,
                        image=credits_button_image,
                        scale=1)

sounds_on_button_image = pygame.image.load(
    DISPLAY["sounds_on_btn_img"]).convert_alpha()
sounds_on_button = Button(x=first_button_x,
                          y=first_button_y + 360,
                          image=sounds_on_button_image,
                          scale=1)

sounds_off_button_image = pygame.image.load(
    DISPLAY["sounds_off_btn_img"]).convert_alpha()
sounds_off_button = Button(x=first_button_x,
                           y=first_button_y + 360,
                           image=sounds_off_button_image,
                           scale=1)

main_menu_button_image = pygame.image.load(
    DISPLAY["main_menu_btn_img"]).convert_alpha()
main_menu_button = Button(x=first_button_x,
                          y=first_button_y + 360,
                          image=main_menu_button_image,
                          scale=1)