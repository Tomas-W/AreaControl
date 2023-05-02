import math

from interactives.skull import Skull

from characters.base_enemy import Enemy
from projectiles.fire_skull import FireSkull
from settings.enemy_settings import SKULL_COLLECTOR

from utilities import get_distance
from settings.enemy_projectile_settings import FIRE_SKULL


class SkullCollector(Enemy):
    def __init__(self, player, position, character):
        super().__init__(player=player,
                         position=position,
                         character=character)

        self.fire_skull_x_offset = FIRE_SKULL["hitbox_x_offset"]
        self.fire_skull_y_offset = FIRE_SKULL["hitbox_y_offset"]

    def set_state(self):
        """
        Sets SkullCollector state depending on distance to Player.
        """
        distance_to_player = get_distance(location_a=self.player.hitbox.center,
                                          location_b=self.hitbox.center)

        if self.health <= 0:
            self.death = True
            self.walk = False
            self.shoot = False

        elif distance_to_player < SKULL_COLLECTOR["shoot_distance"]:
            self.shoot = True
            self.walk = False

        elif distance_to_player > SKULL_COLLECTOR["shoot_distance"]:
            self.walk = True
            self.shoot = False

    def manage_move_state(self):
        """
        Applies SkullCollector move state properties.
        """
        self.move_to_player()
        self.set_move_image()
        self.move_ticks += 1
        self.shoot_ticks = 0

    def manage_shoot_state(self):
        """
        Applies SkullCollector shoot state properties.
        """
        self.set_shoot_image()
        self.shoot_player()
        self.shoot_ticks += 1

    def shoot_player(self):
        """
        Deal shoot towards Player if Player in range.
        """
        if self.shoot_ticks == SKULL_COLLECTOR["shoot_tick"]:
            # Set projectile in right spot on the SkullCollector image
            if self.flip_image:
                projectile_x = self.rect.centerx - (2 * self.fire_skull_x_offset)
            else:
                projectile_x = self.rect.centerx + self.fire_skull_x_offset
            projectile_y = self.rect.centery + self.fire_skull_y_offset
            # Calculate angle to Player
            dx = self.player.rect.centerx - projectile_x
            dy = self.player.rect.centery - projectile_y
            angle = math.degrees(math.atan2(dy, dx))
            # Create projectile
            FireSkull(x=projectile_x,
                      y=projectile_y,
                      angle=angle)

    def manage_death_state(self):
        self.set_death_image()
        self.death_ticks += 1

        if self.death_ticks == SKULL_COLLECTOR["death_tick"]:
            Skull(position=self.hitbox.center)
            self.kill()

    def update(self):
        # Adjust hitbox position
        self.set_hitbox()

        self.set_state()

        self.should_image_flip()

        if self.move:
            self.manage_move_state()

        elif self.shoot:
            self.manage_shoot_state()

        elif self.death:
            self.manage_death_state()

    def set_move_image(self):
        """
        Checks self.move_ticks value and loads corresponding image.
        """
        match self.move_ticks:
            case 0:
                self.image = self.move_sprites[0]
                if self.flip_image:
                    self.image = self.flipped_move_sprites[0]
            case 5:
                self.image = self.move_sprites[1]
                if self.flip_image:
                    self.image = self.flipped_move_sprites[1]
            case 10:
                self.image = self.move_sprites[2]
                if self.flip_image:
                    self.image = self.flipped_move_sprites[2]
            case 15:
                self.image = self.move_sprites[3]
                if self.flip_image:
                    self.image = self.flipped_move_sprites[3]
            case 20:
                self.image = self.move_sprites[4]
                if self.flip_image:
                    self.image = self.flipped_move_sprites[4]
            case 25:
                self.image = self.move_sprites[5]
                if self.flip_image:
                    self.image = self.flipped_move_sprites[5]
            case 30:
                self.image = self.move_sprites[6]
                if self.flip_image:
                    self.image = self.flipped_move_sprites[6]
            case 35:
                self.image = self.move_sprites[7]
                if self.flip_image:
                    self.image = self.flipped_move_sprites[7]
            case 40:
                self.move_ticks = 0

    def set_shoot_image(self):
        """
        Checks self.shoot_ticks value and loads corresponding image.
        """
        match self.shoot_ticks:
            case 0:
                self.image = self.shoot_sprites[0]
                if self.flip_image:
                    self.image = self.flipped_shoot_sprites[0]
            case 5:
                self.image = self.shoot_sprites[1]
                if self.flip_image:
                    self.image = self.flipped_shoot_sprites[1]
            case 10:
                self.image = self.shoot_sprites[2]
                if self.flip_image:
                    self.image = self.flipped_shoot_sprites[2]
            case 15:
                self.image = self.shoot_sprites[3]
                if self.flip_image:
                    self.image = self.flipped_shoot_sprites[3]
            case 20:
                self.image = self.shoot_sprites[4]
                if self.flip_image:
                    self.image = self.flipped_shoot_sprites[4]
            case 25:
                self.image = self.shoot_sprites[5]
                if self.flip_image:
                    self.image = self.flipped_shoot_sprites[5]
            case 30:
                self.image = self.shoot_sprites[6]
                if self.flip_image:
                    self.image = self.flipped_shoot_sprites[6]
            case 35:
                self.image = self.shoot_sprites[7]
                if self.flip_image:
                    self.image = self.flipped_shoot_sprites[7]
            case 40:
                self.image = self.shoot_sprites[8]
                if self.flip_image:
                    self.image = self.flipped_shoot_sprites[8]
            case 45:
                self.image = self.shoot_sprites[9]
                if self.flip_image:
                    self.image = self.flipped_shoot_sprites[9]
            case 50:
                self.image = self.shoot_sprites[10]
                if self.flip_image:
                    self.image = self.flipped_shoot_sprites[10]
            case 55:
                self.image = self.shoot_sprites[11]
                if self.flip_image:
                    self.image = self.flipped_shoot_sprites[11]
            case 60:
                self.image = self.shoot_sprites[12]
                if self.flip_image:
                    self.image = self.flipped_shoot_sprites[12]
            case 75:
                self.shoot_ticks = 0

    def set_death_image(self):
        """
        Checks self.death_ticks value and loads corresponding image.
        """
        match self.death_ticks:
            case 5:
                self.image = self.death_sprites[0]
            case 10:
                self.image = self.death_sprites[1]
            case 15:
                self.image = self.death_sprites[2]
            case 20:
                self.image = self.death_sprites[3]
            case 25:
                self.image = self.death_sprites[4]
            case 30:
                self.image = self.death_sprites[5]
            case 35:
                self.image = self.death_sprites[6]
            case 40:
                self.image = self.death_sprites[7]
            case 45:
                self.image = self.death_sprites[8]


