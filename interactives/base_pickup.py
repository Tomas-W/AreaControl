from random import choice

import pygame

from utilities.sprite_groups import all_sprites, energy_sprites, skull_sprites, coin_sprites, \
    health_potion_sprites


class PickUp(pygame.sprite.Sprite):
    """
    Base class for PickUps.

    PickUps are spawned in on an Enemy's location after they die.
    Collecting them rewards bonuses.

    A new PickUp can be created by passing in a dictionary.
    """
    def __init__(self, player, position, pickup_name):
        super().__init__(all_sprites)
        # Reference Player
        self.player = player

        # Determine spawn location
        if pickup_name["name"] == "health_potion":
            position = choice(pickup_name["spawn_location"])

        # Sprites
        self.sprites = pickup_name["sprites"]

        # Image
        self.image = pickup_name["image"].copy()
        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = position
        # Hitbox
        self.hitbox = pygame.Rect(pickup_name["hitbox"])
        self.hitbox.center = position

        # Sounds
        self.pick_up_sound = pygame.mixer.Sound(pickup_name["pick_up_sound_path"])
        self.pick_up_sound.set_volume(0.2)
        self.played_death_sound = False

        # Attributes
        self.name = pickup_name["name"]
        self.boost = pickup_name["boost"]
        self.transparency = pickup_name["transparency"]

        # Trackers
        self.frame = pickup_name["frame"]
        self.ticks_per_frame = pickup_name["ticks_per_frame"]
        self.frame_ticks = pickup_name["frame_ticks"]

        # add to correct sprite list
        if pickup_name["name"] == "skull":
            skull_sprites.add(self)
        elif pickup_name["name"] == "energy":
            energy_sprites.add(self)
        elif pickup_name["name"] == "coin":
            coin_sprites.add(self)
        elif self.name == "health_potion":
            health_potion_sprites.add(self)

    def kill_self(self):
        if self.player.sound_is_on:
            self.pick_up_sound.play()

        self.kill()

    def update(self):
        self.frame_ticks += 1
        self.set_interactive_image()
        self.image.set_alpha(self.transparency)

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
