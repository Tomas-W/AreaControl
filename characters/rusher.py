from random import choice

from characters.base_enemy import Enemy
from interactives.base_pickup import PickUp

from settings.interactives_settings import ENERGY

from utilities import get_distance

from settings.enemy_settings import RUSHER


class Rusher(Enemy):
    def __init__(self, player, position, character):
        super().__init__(player=player,
                         position=position,
                         character=character)

        # Private attributes
        self.image_opacity = 10

    def manage_spawn_state(self):
        """"
        Controls spawn behaviour of the Rusher.
        Places Rusher in random location,
            plays appear in cage animation and
            increases its alpha value.

        """
        self.frame_ticks += 1

        self.image = self.spawn_sprites[self.frame]
        self.image.set_alpha(self.image_opacity)

        # Set correct spawn frame and alpha value
        if self.frame_ticks == self.spawn_ticks:
            self.frame_ticks = 0
            self.frame += 1
            self.image_opacity += 10

        # Disable spawn state when animation is done
        if self.frame == len(self.spawn_sprites):
            self.frame = 0
            self.frame_ticks = 0
            self.spawn = False

    def set_state(self):
        """
        Sets Rusher state depending on distance to Player.
        """
        distance_to_player = get_distance(location_a=self.player.hitbox.center,
                                          location_b=self.rect.center)

        # Death
        if self.health <= 0:
            self.death = True
            self.idle = False
            self.run = False
            self.strike = False
            self.frame_ticks = 0
            self.frame = 0

        # Strike
        elif distance_to_player < RUSHER["strike_distance"]:
            self.strike = True
            self.idle = False
            self.run = False
            self.current_state = "strike"
        # Move
        elif distance_to_player < RUSHER["run_distance"]:
            self.run = True
            self.idle = False
            self.strike = False
            self.current_state = "run"
        # Idle
        elif distance_to_player > RUSHER["run_distance"]:
            self.idle = True
            self.run = False
            self.strike = False
            self.current_state = "idle"

    def manage_idle_state(self):
        """
        Applies Rusher idle state and image properties.
        """
        self.set_idle_image()

    def manage_move_state(self):
        """
        Applies Rusher move state and image properties.
        """
        self.move_to_player()
        self.set_run_image()

    def manage_strike_state(self):
        """
        Applies Rusher strike state and image properties.
        """
        if self.is_allowed_to_strike():
            self.strike_player()

        self.set_strike_image()

    def is_allowed_to_strike(self):
        """
        Checks if Rusher is allowed to strike Player.

        :return: Returns True if conditions are met (bool).
        """
        return self.frame == self.strike_frame and self.frame_ticks == (
                    self.strike_ticks // 2) and not self.player.is_invincible

    def strike_player(self):
        """
        Deal strike damage to Player.
        """
        self.player.health -= self.damage

    def manage_death_state(self):
        """
        Applies Rusher death state and image properties.
        """
        self.frame_ticks += 1

        self.set_death_image()

        if self.frame_ticks == self.death_ticks:
            self.frame += 1
            self.frame_ticks = 0

        # Kill Rusher and place Energy
        if self.frame == self.death_frame:
            PickUp(position=self.rect.center,
                   pickup_name=ENERGY)
            Rusher(player=self.player,
                   position=choice(RUSHER["start_position"]),
                   character=RUSHER)
            self.kill()

    def update(self):

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

                if self.idle:
                    self.manage_idle_state()

                elif self.run:
                    self.manage_move_state()

                elif self.strike:
                    self.manage_strike_state()
