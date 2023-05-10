from projectiles.base_projectile import Projectile
from settings.projectile_settings import FLAMING_SKULL


class FlamingSkull(Projectile):
    def __init__(self, player, x, y, angle, bomb_location):
        super().__init__(player=player,
                         x=x,
                         y=y,
                         angle=angle,
                         projectile_name=FLAMING_SKULL,
                         bomb_location=bomb_location)

    def update(self):
        self.set_hitbox()
        self.movement()
