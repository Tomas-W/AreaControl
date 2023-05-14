import os
import sys

import pygame

from settings.general_settings import PLAYER_SIZE

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

PLAYER_SPRITE = pygame.transform.rotozoom(
            pygame.image.load(
                os.path.join(base_dir, "./images/player/player_pistol.png")).convert_alpha(),
            False,
            PLAYER_SIZE)

PLAYER_SHOOT_SPRITE = pygame.transform.rotozoom(
            pygame.image.load(
                os.path.join(base_dir, "./images/player/player_pistol_fire.png")).convert_alpha(),
            False,
            PLAYER_SIZE)
