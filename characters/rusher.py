from characters.base_enemy import Enemy

from interactives.energy import Energy

from utilities import get_distance

from settings.enemy_settings import RUSHER


class Rusher(Enemy):
    def __init__(self, player, position, character):
        super().__init__(player=player,
                         position=position,
                         character=character)

    def set_state(self):
        """
        Sets Rusher state depending on distance to Player.
        """
        distance_to_player = get_distance(location_a=self.player.hitbox.center,
                                          location_b=self.rect.center)

        if self.health <= 0:
            self.death = True
            self.idle = False
            self.run = False
            self.strike = False
            self.frame_ticks = 0
            self.frame = 0

        # Set strike
        elif distance_to_player < RUSHER["strike_distance"]:
            self.strike = True
            self.idle = False
            self.run = False
            self.current_state = "strike"
        # Set move
        elif distance_to_player < RUSHER["run_distance"]:
            self.run = True
            self.idle = False
            self.strike = False
            self.current_state = "run"
        # Set idle
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
        self.set_move_image()

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
        self.set_death_image()

        self.frame_ticks += 1

        if self.frame_ticks == self.death_ticks:
            self.frame += 1
            self.frame_ticks = 0

        # Kill Rusher and place Energy
        if self.frame == self.death_frame:
            Energy(position=self.rect.center)
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

            if self.idle:
                self.manage_idle_state()

            elif self.run:
                self.manage_move_state()

            elif self.strike:
                self.manage_strike_state()

    def set_idle_image(self):
        if self.frame_ticks == self.idle_ticks:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.idle_sprites) - 1:
            self.frame = 0

        if self.flip_image:
            self.image = self.idle_sprites_flipped[self.frame]
        else:
            self.image = self.idle_sprites[self.frame]

    def set_move_image(self):
        if self.frame_ticks == self.run_ticks:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.run_sprites) - 1:
            self.frame = 0

        if self.flip_image:
            self.image = self.run_sprites_flipped[self.frame]
        else:
            self.image = self.run_sprites[self.frame]

    def set_strike_image(self):
        if self.frame_ticks == self.strike_ticks:
            self.frame += 1
            self.frame_ticks = 0

        if self.frame > len(self.strike_sprites) - 1:
            self.frame = 0

        if self.flip_image:
            self.image = self.strike_sprites_flipped[self.frame]
        else:
            self.image = self.strike_sprites[self.frame]

    def set_death_image(self):
        if self.flip_image:
            self.image = self.death_sprites_flipped[self.frame]
        else:
            self.image = self.death_sprites[self.frame]
