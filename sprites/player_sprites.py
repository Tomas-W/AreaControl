import pygame

from settings.general_settings import PLAYER_SIZE


PLAYER_SPRITE = pygame.transform.rotozoom(
            pygame.image.load("images/player/player_pistol2.png").convert_alpha(),
            False,
            PLAYER_SIZE)

PLAYER_SHOOT_SPRITE = pygame.transform.rotozoom(
            pygame.image.load("images/player/player_pistol_fire2.png").convert_alpha(),
            False,
            PLAYER_SIZE)
