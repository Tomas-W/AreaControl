from random import randint

from creepers.base_creeper import Creeper
from utilities import get_distance


class Fish(Creeper):
    def __init__(self, player, creeper_name):
        super().__init__(player=player,
                         creeper_name=creeper_name)

    def set_state(self):

        if self.health <= 0:
            self.kill()

        if not self.chase:
            distance_to_player = get_distance(location_a=self.player.hitbox.center,
                                              location_b=self.hitbox.center)

            if distance_to_player < self.chase_distance:
                self.chase = True
                self.idle = False
                self.frame_ticks = 0
                self.position = self.rect.center
                self.speed = self.chase_speed

    def manage_idle_state(self):
        self.circle_location()
        self.set_idle_image()

    def manage_chase_state(self):
        self.move_to_player()

        if self.is_allowed_to_strike():
            self.strike_player()

        self.set_chase_image()

    def is_allowed_to_strike(self):
        """
        Checks if Fish is allowed to strike Player.

        :return: Returns True if conditions are met (bool).
        """
        return self.hitbox.colliderect(self.player.hitbox) and not self.player.is_invincible

    def strike_player(self):
        self.player.health -= self.damage
        self.kill()

    def update(self):

        self.set_hitbox()

        self.set_state()

        self.manage_frames()

        self.should_image_flip()

        if self.idle:
            self.manage_idle_state()

        elif self.chase:
            self.manage_chase_state()
