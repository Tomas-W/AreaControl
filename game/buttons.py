import time

import pygame

from settings.general_settings import GENERAL

clicked_time = time.time()


class Button:
    def __init__(self, x, y, image, scale, name, player):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

        # Sounds
        self.button_hover_sound = pygame.mixer.Sound(GENERAL["button_hover_sound_path"])
        self.button_hover_sound.set_volume(0.1)
        self.button_click_sound = pygame.mixer.Sound(GENERAL["button_click_sound_path"])
        self.button_click_sound.set_volume(0.3)
        self.play_game_sound = pygame.mixer.Sound(GENERAL["play_game_sound_path"])
        self.play_game_sound.set_volume(0.3)

        self.name = name
        self.player = player

    def draw(self, surface):
        global clicked_time

        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            # Hover sound
            if self.image.get_alpha() < 255 and self.player.sound_is_on:
                self.button_hover_sound.play()
            self.image.set_alpha(255)

            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                if time.time() - clicked_time > 0.5:
                    clicked_time = time.time()
                    self.clicked = True
                    action = True

                    # Play correct sound
                    if self.name == "play" or self.name == "restart":
                        if self.player.sound_is_on:
                            self.play_game_sound.play()
                        time.sleep(0.5)

                    else:
                        if self.player.sound_is_on:
                            self.button_click_sound.play()

        else:
            self.image.set_alpha(175)

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
