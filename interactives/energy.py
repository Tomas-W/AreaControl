import pygame

from settings.interactives_settings import ENERGY
from sprites.interactives_sprites import ENERGY_SPRITES
from utilities import all_sprites, energy_sprites


class Energy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__(all_sprites, energy_sprites)
        # Load sprites
        self.energy_sprites = ENERGY_SPRITES

        # Image
        self.image = self.energy_sprites[0]
        # Rect
        self.rect = self.image.get_rect()
        # Hitbox
        self.hitbox = pygame.Rect(0, 0,
                                  ENERGY["hitbox_width"], ENERGY["hitbox_height"])

        # Spawn location
        self.rect.center = position
        self.hitbox.left = self.rect.left + ENERGY["hitbox_offset_x"]
        self.hitbox.top = self.rect.top + ENERGY["hitbox_offset_y"]

        # Attributes
        self.name = "energy"
        self.image.set_alpha(155)

        # Trackers
        self.energy_ticks = 0

    def update(self):
        self.energy_ticks += 1
        self.set_energy_image()

    def set_energy_image(self):
        """
        Checks player.energy_ticks value and loads corresponding Energy image.
        """
        match self.energy_ticks:
            case 4:
                self.image = self.energy_sprites[1]
            case 8:
                self.image = self.energy_sprites[2]
            case 12:
                self.image = self.energy_sprites[3]
            case 16:
                self.image = self.energy_sprites[4]
            case 20:
                self.image = self.energy_sprites[5]
            case 24:
                self.image = self.energy_sprites[6]
            case 28:
                self.image = self.energy_sprites[7]
            case 32:
                self.image = self.energy_sprites[8]
            case 36:
                self.image = self.energy_sprites[9]
            case 40:
                self.image = self.energy_sprites[10]
            case 44:
                self.energy_ticks = 0
