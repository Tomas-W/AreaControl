import pygame

from settings.general_settings import GENERAL

pygame.init()

screen = pygame.display.set_mode((GENERAL["width"],
                                  GENERAL["height"]),
                                 16)
pygame.display.set_caption(GENERAL["title"])

from settings.enemy_settings import SKULL_COLLECTOR

from characters.skull_collector import SkullCollector
from player import Player

player = Player()

enemy = SkullCollector(player=player,
                       position=(1750, 1100),
                       character=SKULL_COLLECTOR)

print(enemy.health)
print(enemy.run_speed)
