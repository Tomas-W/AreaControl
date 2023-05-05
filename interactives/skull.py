import pygame

from settings.interactives_settings import ENERGY
from sprites.interactives_sprites import SKULL_SPRITES
from utilities import all_sprites, skull_sprites


class Skull(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__(all_sprites, skull_sprites)
        # Load sprites
        self.skull_sprites = SKULL_SPRITES

        # Image
        self.image = self.skull_sprites[0]
        # Rect
        self.rect = self.image.get_rect()
        # Spawn location
        self.rect.center = position
        # Hitbox
        self.hitbox = pygame.Rect(ENERGY["hitbox"])

        # Attributes
        self.name = "skull"
        self.image.set_alpha(155)

        # Trackers
        self.skull_ticks = 0

    def update(self):
        self.skull_ticks += 1

        self.set_skull_image()

    def set_skull_image(self):
        """
        Checks player.skull_ticks value and loads corresponding Portal image.
        """
        match self.skull_ticks:
            case 4:
                self.image = self.skull_sprites[1]
                self.image.set_alpha(230)
            case 8:
                self.image = self.skull_sprites[2]
                self.image.set_alpha(200)
            case 12:
                self.image = self.skull_sprites[3]
                self.image.set_alpha(170)
            case 16:
                self.image = self.skull_sprites[4]
                self.image.set_alpha(140)
            case 20:
                self.image = self.skull_sprites[5]
                self.image.set_alpha(110)
            case 24:
                self.image = self.skull_sprites[6]
                self.image.set_alpha(80)
            case 28:
                self.image = self.skull_sprites[5]
                self.image.set_alpha(110)
            case 32:
                self.image = self.skull_sprites[4]
                self.image.set_alpha(140)
            case 36:
                self.image = self.skull_sprites[3]
                self.image.set_alpha(170)
            case 40:
                self.image = self.skull_sprites[2]
                self.image.set_alpha(200)
            case 44:
                self.image = self.skull_sprites[1]
                self.image.set_alpha(230)
            case 48:
                self.image = self.skull_sprites[0]
                self.image.set_alpha(255)
            case 52:
                self.skull_ticks = 0
