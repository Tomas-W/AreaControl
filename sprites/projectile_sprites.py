import pygame

from settings.enemy_projectile_settings import FIRE_SKULL
from settings.player_settings import BULLET

fire_skull_image = pygame.image.load(
    "./images/projectiles/fire_skull.png").convert_alpha()
FIRE_SKULL_SPRITE = pygame.transform.rotozoom(fire_skull_image,
                                              False,
                                              FIRE_SKULL["size"])

bullet_image = pygame.image.load(
    "./images/projectiles/bullet_blue.png").convert_alpha()
BULLET_SPRITE = pygame.transform.rotozoom(bullet_image,
                                          False,
                                          BULLET["size"])
