import pygame

from creepers.base_creeper import Creeper


class Bat(Creeper):
    def __init__(self, player, creeper_name):
        super().__init__(player=player,
                         creeper_name=creeper_name)

    def update(self):

        self.frame_ticks += 1

        self.set_hitbox()

        self.set_state()

        self.should_image_flip()

        if self.idle:
            self.manage_idle_state()

        elif self.chase:
            self.manage_chase_state()
