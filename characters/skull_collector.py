import math

from characters.base_enemy import Enemy
from projectiles.fire_skull import FireSkull
from interactives.skull import Skull

from utilities import get_distance

from settings.enemy_settings import SKULL_COLLECTOR


class SkullCollector(Enemy):
    def __init__(self, player, position, character):
        super().__init__(player=player,
                         position=position,
                         character=character)

    def set_state(self):
        """
        Sets SkullCollector state depending on distance to Player.
        """
        distance_to_player = get_distance(location_a=self.player.hitbox.center,
                                          location_b=self.hitbox.center)

        if self.health <= 0:
            self.death = True
            self.walk = False
            self.shoot = False
            self.frame_ticks = 0
            self.frame = 0

        elif distance_to_player < SKULL_COLLECTOR["shoot_distance"]:
            self.shoot = True
            self.walk = False
            self.current_state = "shoot"

        elif distance_to_player > SKULL_COLLECTOR["shoot_distance"]:
            self.walk = True
            self.shoot = False
            self.current_state = "walk"

    def manage_move_state(self):
        """
        Applies SkullCollector move state and image properties.
        """
        self.move_to_player()
        self.set_move_image()

    def manage_shoot_state(self):
        """
        Applies SkullCollector shoot state and image properties.
        """
        if self.is_allowed_to_shoot():
            self.shoot_player()

        self.set_shoot_image()

    def is_allowed_to_shoot(self):
        """
        Checks if SkullCollector is allowed to shoot Player.

        :return: Returns True if conditions are met (bool).
        """
        return self.frame == self.shoot_frame and self.frame_ticks == (self.shoot_ticks // 2)

    def shoot_player(self):
        """
        Shoot FireSkull towards Player.
        """
        # Set projectile in right spot on the SkullCollector image
        if self.flip_image:
            projectile_x = self.rect.centerx - self.shoot_offset_x
        else:
            projectile_x = self.rect.centerx + self.shoot_offset_x
        projectile_y = self.rect.centery + self.shoot_offset_y

        # Calculate angle to Player
        dx = self.player.rect.centerx - projectile_x
        dy = self.player.rect.centery - projectile_y
        angle = math.degrees(math.atan2(dy, dx))
        # Create projectile
        FireSkull(x=projectile_x,
                  y=projectile_y,
                  angle=angle)

    def manage_death_state(self):
        """
        Applies SkullCollector death state and image properties.
        """
        self.set_death_image()

        self.frame_ticks += 1

        if self.frame_ticks == self.death_ticks:
            self.frame += 1
            self.frame_ticks = 0

        # Kill SkullCollector and place Skull
        if self.frame == self.death_frame:
            Skull(position=self.hitbox.center)
            self.kill()

    def manage_frames(self):
        self.frame_ticks += 1

        # Animation switch
        if self.current_state != self.last_state:
            self.frame_ticks = 0

        self.last_state = self.current_state

    def update(self):
        if self.death:
            self.manage_death_state()

        else:
            self.set_hitbox()

            self.set_state()

            self.manage_frames()

            self.should_image_flip()

            if self.walk:
                self.manage_move_state()

            elif self.shoot:
                self.manage_shoot_state()

    def set_move_image(self):
        if self.frame_ticks == self.walk_ticks:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.walk_sprites) - 1:
            self.frame = 0

        if self.flip_image:
            self.image = self.walk_sprites_flipped[self.frame]
        else:
            self.image = self.walk_sprites[self.frame]

    def set_shoot_image(self):
        if self.frame_ticks == self.shoot_ticks:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.shoot_sprites) - 1:
            self.frame = 0

        if self.flip_image:
            self.image = self.shoot_sprites_flipped[self.frame]
        else:
            self.image = self.shoot_sprites[self.frame]

    def set_death_image(self):
        if self.flip_image:
            self.image = self.death_sprites_flipped[self.frame]
        else:
            self.image = self.death_sprites[self.frame]
