import pygame

from settings.general_settings import FLAMING_SKULL_SIZE, BULLET_SIZE

flaming_skull_image = pygame.image.load(
    "./images/projectiles/flaming_skull.png").convert_alpha()
FLAMING_SKULL_SPRITE = pygame.transform.rotozoom(flaming_skull_image,
                                                 False,
                                                 FLAMING_SKULL_SIZE)

bullet_image = pygame.image.load(
    "./images/projectiles/bullet_blue.png").convert_alpha()
BULLET_SPRITE = pygame.transform.rotozoom(bullet_image,
                                          False,
                                          BULLET_SIZE)
