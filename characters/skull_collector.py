import math

from characters.base_enemy import Enemy
from interactives.base_pickup import PickUp
from projectiles.flaming_skull import FlamingSkull

from settings.general_settings import GENERAL
from settings.interactives_settings import SKULL

from utilities import get_distance

from settings.enemy_settings import SKULL_COLLECTOR


class SkullCollector(Enemy):
    def __init__(self, player, position, character):
        super().__init__(player=player,
                         position=position,
                         character=character)

        # Private attributes

    def manage_spawn_state(self):
        """"
        Controls spawn behaviour of the SkullCollector.
        Places SkullCollector outside boarders and
            moves it towards the play area,
            increasing its alpha value.

        When SkullCollector is in play area and 255 alpha,
            spawn state is disabled.
        """
        self.frame_ticks += 1

        # Move towards play area
        if self.rect.centery < GENERAL["y_min"]:
            self.rect.y += 1
        if self.rect.centery > GENERAL["y_max"]:
            self.rect.y -= 1

        # Update position and alpha value
        self.position = self.rect.center
        self.image.set_alpha(self.frame_ticks)

        if self.frame_ticks == 255:
            self.spawn = False
            self.frame_ticks = 0

    def set_state(self):
        """
        Sets SkullCollector state depending on distance to Player.
        """
        distance_to_player = get_distance(location_a=self.player.hitbox.center,
                                          location_b=self.hitbox.center)

        # Death
        if self.health <= 0:
            self.death = True
            self.walk = False
            self.shoot = False
            self.frame_ticks = 0
            self.frame = 0

        # Move
        if distance_to_player > SKULL_COLLECTOR["shoot_distance"]:
            self.walk = True
            self.shoot = False
            self.current_state = "walk"

        # Shoot
        elif distance_to_player < SKULL_COLLECTOR["shoot_distance"]:
            self.shoot = True
            self.walk = False
            self.current_state = "shoot"

    def manage_move_state(self):
        """
        Applies SkullCollector move state and image properties.
        """
        self.move_to_player()
        self.set_walk_image()

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
        Shoot FlamingSkull towards Player.
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
        FlamingSkull(player=self.player,
                     x=projectile_x,
                     y=projectile_y,
                     angle=angle,
                     bomb_location=None)

    def manage_death_state(self):
        """
        Applies SkullCollector death state and image properties.
        """
        self.frame_ticks += 1

        self.set_death_image()

        if self.frame_ticks == self.death_ticks:
            self.frame += 1
            self.frame_ticks = 0

        # Place Skull and kill SkullCollector
        if self.frame == self.death_frame:
            PickUp(position=self.rect.center,
                   pickup_name=SKULL)
            # SkullCollector(player=self.player,
            #                position=(choice(SKULL_COLLECTOR["start_position"])),
            #                character=SKULL_COLLECTOR)
            self.kill()

    def update(self):
        # Spawn image is currently static
        if self.spawn:
            self.manage_spawn_state()

        else:
            # Death state has its own frame manager
            if self.death:
                self.manage_death_state()

            # If not dead and not in spawn mode
            else:
                self.set_hitbox()

                self.set_state()

                self.manage_frames()

                self.should_image_flip()

                if self.walk:
                    self.manage_move_state()

                elif self.shoot:
                    self.manage_shoot_state()
