from creepers.base_creeper import Creeper


class Fish(Creeper):
    def __init__(self, player, position, creeper_name):
        super().__init__(player=player,
                         position=position,
                         creeper_name=creeper_name)

    def update(self):

        self.set_hitbox()

        self.set_state()

        self.manage_frames()

        self.should_image_flip()

        if self.idle:
            self.manage_idle_state()

        elif self.chase:
            self.manage_chase_state()
