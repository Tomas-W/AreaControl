from characters.base_enemy import BaseEnemy
from interactives.base_pickup import PickUp

from settings.general_settings import GENERAL
from settings.interactives_settings import SKULL

from utilities.game_physics import get_distance

from settings.enemy_settings import SKULL_COLLECTOR


class SkullCollector(BaseEnemy):
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
        if self.rect.centery < GENERAL["y_min"] + 10:  # Offset for shooting
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

    def manage_death_state(self):
        """
        Applies SkullCollector death state and image properties.
        """
        self.play_death_sound()

        self.frame_ticks += 1

        self.set_death_image()

        if self.frame_ticks == self.death_ticks:
            self.frame += 1
            self.frame_ticks = 0

        # Place Skull and kill SkullCollector
        if self.frame == self.death_frame:
            # Spawn PickUp
            PickUp(position=self.rect.center,
                   pickup_name=SKULL,
                   player=self.player)

            # Update Player kills
            self.player.kills[self.name] += 1

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
