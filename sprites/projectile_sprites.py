import pygame

from settings.general_settings import FIRE_SKULL_SIZE, BULLET_SIZE

fire_skull_image = pygame.image.load(
    "./images/projectiles/fire_skull.png").convert_alpha()
FIRE_SKULL_SPRITE = pygame.transform.rotozoom(fire_skull_image,
                                              False,
                                              FIRE_SKULL_SIZE)

bullet_image = pygame.image.load(
    "./images/projectiles/bullet_blue.png").convert_alpha()
BULLET_SPRITE = pygame.transform.rotozoom(bullet_image,
                                          False,
                                          BULLET_SIZE)
