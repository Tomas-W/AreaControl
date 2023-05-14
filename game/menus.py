import time

import pygame


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
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked and time.time() - self.spawn_time > 0.5:
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
