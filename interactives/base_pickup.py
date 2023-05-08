import pygame

from utilities import all_sprites, energy_sprites, skull_sprites


class PickUp(pygame.sprite.Sprite):
    def __init__(self, position, pickup_name):
        super().__init__(all_sprites)
        # Sprites
        self.sprites = pickup_name["sprites"]

        # Image
        self.image = pickup_name["image"]
        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = position
        # Hitbox
        self.hitbox = pygame.Rect(pickup_name["hitbox"])
        self.hitbox.center = position

        # Attributes
        self.name = pickup_name["name"]
        self.boost = pickup_name["boost"]
        self.image.set_alpha(pickup_name["transparency"])

        # Trackers
        self.frame = pickup_name["frame"]
        self.ticks_per_frame = pickup_name["ticks_per_frame"]
        self.frame_ticks = pickup_name["frame_ticks"]

        # add to correct sprite list
        if pickup_name["name"] == "skull":
            skull_sprites.add(self)
        elif pickup_name["name"] == "energy":
            energy_sprites.add(self)

    def update(self):
        self.frame_ticks += 1
        self.set_interactive_image()

    def set_interactive_image(self):
        """
        Sets correct image depending on animation length and
            frames per animation.
        """
        if self.frame_ticks == self.ticks_per_frame:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.sprites) - 1:
            self.frame = 0

        self.image = self.sprites[self.frame]
