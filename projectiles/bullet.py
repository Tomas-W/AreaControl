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

    def update(self):
        self.set_hitbox()
        self.movement()
