from projectiles.base_projectile import Projectile
from settings.projectile_settings import BULLET


class Bullet(Projectile):
    def __init__(self, player, x, y, angle):
        super().__init__(player=player,
                         x=x,
                         y=y,
                         angle=angle,
                         projectile_name=BULLET,
                         bomb_location=None)

        self.spawn = True
        self.image.set_alpha(0)
        self.alpha_ticks = 0

    def update(self):
        if self.spawn:
            self.alpha_ticks += 1

            if self.alpha_ticks > 1:
                self.image.set_alpha(255)
                self.spawn = False

        self.set_hitbox()
        self.movement()
