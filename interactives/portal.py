import pygame

from settings.interactives_settings import PORTAL
from settings.player_settings import PLAYER
from sprites.interactives_sprites import PORTAL_SPRITES
from utilities import all_sprites, get_new_portal_center, portal_sprites


class Portal(pygame.sprite.Sprite):
    def __init__(self, player, side):
        super().__init__(all_sprites, portal_sprites)
        # Reference Player sprite
        self.player = player
        # Load Portal side
        self.side = side  # Left or right side of level

        # Load sprites
        self.portal_sprites = PORTAL_SPRITES

        # Image
        self.image = self.portal_sprites[0]
        # Rect
        self.rect = self.image.get_rect()
        # Hitbox
        self.hitbox = pygame.Rect(PORTAL["hitbox"])

        # Spawn location
        self.rect.center = get_new_portal_center(side)

        # Attributes
        self.this_portal_was_used = False
        self.is_visible = False
        self.image.set_alpha(0)
        self.name = "portal"

        # Trackers
        self.spawn_ticks = 0
        self.portal_ticks = 0
        self.portal_animation_ticks = 0

    def set_portal_hitbox(self):
        """
        Aligns hitbox with Portal rect.
        """
        self.hitbox.left = self.rect.left + PORTAL["hitbox_left_offset"]
        self.hitbox.top = self.rect.top + PORTAL["hitbox_right_offset"]

    def set_visibility(self):
        """
        Makes the Portal visible after certain time.
        """
        if self.spawn_ticks == PORTAL["visible_tick"]:
            self.is_visible = True
            self.image.set_alpha(PORTAL["transparency"])

    def check_portal_collision(self):
        """
        Detects collision between Player and Portal,
            loads other Portal's coordinates in the Player instance and
            configures used Portal.
        """
        if self.player_used_portal():
            self.this_portal_was_used = True
            self.player.new_location = self.other_portal_center()
            for portal in portal_sprites:
                portal.portal_ticks += 1

    def player_used_portal(self):
        """
        Returns whether player collides with Portal and teleport requirements are met.

        :return: If player is allowed to use Portal (bool).
        """
        return self.player.hitbox.colliderect(
            self.hitbox) and self.is_visible and self.portal_ticks == 0

    @staticmethod
    def other_portal_center():
        """
        Returns coordinates of the Portal that was not used.

        :return: Coordinates (bool).
        """
        for portal in portal_sprites:
            if not portal.this_portal_was_used:
                return portal.rect.center

    def reset_portal(self):
        """
        Creates a new Portal and self-destructs.

        :return: New Portal instance.
        """
        if self.portal_ticks == PLAYER["new_location_tick"] - 1:
            Portal(player=self.player,
                   side=self.side)
            self.kill()

    def follow_player(self):
        """
        Aligns Portal center with Player hitbox center if Portal was used.
        """
        if self.this_portal_was_used:
            self.rect.center = self.player.hitbox.center
            self.image.set_alpha(PORTAL["active_transparency"])
        self.spawn_ticks += 1

    def update(self):
        # Align hitbox
        self.set_portal_hitbox()

        # Display correct frame
        self.set_portal_image()

        # Initially invisible after spawn
        self.set_visibility()

        self.check_portal_collision()

        self.reset_portal()

        # Track Player hitbox after Portal use
        self.follow_player()

        # Update trackers
        if self.portal_ticks > 0:
            self.portal_ticks += 1
        self.spawn_ticks += 1
        self.portal_animation_ticks += 1

    def set_portal_image(self):
        """
        Checks player.new_location_ticks value and loads corresponding Portal image.
        """
        match self.portal_animation_ticks:
            case 2:
                self.image = self.portal_sprites[0]
            case 4:
                self.image = self.portal_sprites[2]
            case 6:
                self.image = self.portal_sprites[4]
            case 8:
                self.image = self.portal_sprites[6]
            case 10:
                self.image = self.portal_sprites[8]
            case 12:
                self.image = self.portal_sprites[10]
            case 14:
                self.image = self.portal_sprites[12]
            case 16:
                self.image = self.portal_sprites[14]
            case 18:
                self.image = self.portal_sprites[16]
            case 20:
                self.image = self.portal_sprites[14]
            case 22:
                self.image = self.portal_sprites[12]
            case 24:
                self.image = self.portal_sprites[10]
            case 26:
                self.image = self.portal_sprites[8]
            case 28:
                self.image = self.portal_sprites[6]
            case 30:
                self.image = self.portal_sprites[4]
            case 32:
                self.image = self.portal_sprites[2]
            case 34:
                self.portal_animation_ticks = 0
