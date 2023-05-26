from projectiles.base_projectile import Projectile
from settings.projectile_settings import BOMB
from sprites.projectile_sprites import BOMB_EXPLOSION_SPRITES
from utilities import get_distance


class Bomb(Projectile):
    """
    Bomb flies towards coordinates of the mouse upon time of fire.

    Explodes distance to target is within x (because of small offsets, see player model).
    """
    def __init__(self, player, x, y, angle, bomb_location):
        super().__init__(player=player,
                         x=x,
                         y=y,
                         angle=angle,
                         projectile_name=BOMB,
                         bomb_location=bomb_location)

        self.spawn = True
        self.image.set_alpha(0)
        self.alpha_ticks = 0

        self.explosion_sprites = BOMB_EXPLOSION_SPRITES
        self.dealt_damage = False
        self.explode = False
        self.damage_radius = 150

    def manage_bomb(self):
        self.frame_ticks += 1

        # Update frame index
        if self.frame_ticks == self.image_ticks:
            self.frame += 1
            self.frame_ticks = 0

        # Reset animation
        if self.frame == len(self.sprite_sheet):
            self.frame = 0

        self.image = self.sprite_sheet[self.frame]

        # Explode when in range
        if get_distance(self.bomb_location,
                        self.rect.center) < 20:
            self.explode = True
            self.frame = 0
            self.frame_ticks = 0

    def manage_explosion(self):
        # Offset explosion because of scaling
        self.rect.centerx = self.bomb_location[0] - 25
        self.rect.centery = self.bomb_location[1] - 25
        print(self.frame)
        print(self.frame_ticks)
        print("**********")
        print("**********")

        if self.frame == 0 and self.frame_ticks == 1:
            self.death_sound.play()

        self.frame_ticks += 1

        # Update frame index
        if self.frame_ticks == self.image_ticks:
            self.frame += 1
            self.frame_ticks = 0

        # Kill itself after explosion animation
        if self.frame == len(self.explosion_sprites) - 1:
            self.kill()

        self.image = self.explosion_sprites[self.frame]

    def update(self):
        if self.spawn:
            self.alpha_ticks += 1

            if self.alpha_ticks > 1:
                self.image.set_alpha(255)
                self.spawn = False

        if not self.explode:
            self.set_hitbox()
            self.movement()
            self.manage_bomb()

        else:
            self.manage_explosion()

