from random import randint

import pygame

from settings.general_settings import GENERAL
from settings.interactives_settings import PORTAL

all_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.GroupSingle()
enemy_sprites = pygame.sprite.Group()

all_projectile_sprites = pygame.sprite.Group()
player_projectile_sprites = pygame.sprite.Group()
enemy_projectile_sprites = pygame.sprite.Group()

skull_sprites = pygame.sprite.Group()
energy_sprites = pygame.sprite.Group()
portal_sprites = pygame.sprite.Group()


def handle_outgoing_projectiles():
    """
    Checks all Player projectiles and Enemies and applies damage if collision.
    """
    for enemy in enemy_sprites:
        for projectile in player_projectile_sprites:
            # Check collision with Enemies
            if projectile.rect.colliderect(enemy.hitbox) and not enemy.death:
                enemy.health -= projectile.damage
                projectile.kill()

            # Check collision with walls
            if projectile.rect.left < GENERAL["level_left_x"] or projectile.rect.right > GENERAL[
                "level_right_x"] or \
                    projectile.rect.top < GENERAL["level_top_y"] or projectile.rect.bottom > \
                    GENERAL["level_bottom_y"]:
                projectile.kill()


def handle_incoming_projectiles():
    """
    Checks all Enemy projectiles and Player and applies damage if collision.
    """
    for projectile in enemy_projectile_sprites:
        # Check collision with Player
        if projectile.hitbox.colliderect(player_sprite.sprite.hitbox):
            # Check Player invincibility
            if not player_sprite.sprite.is_invincible:
                player_sprite.sprite.health -= projectile.damage
            projectile.kill()

        # Check collision with walls
        if projectile.rect.left < GENERAL["level_left_x"] or projectile.rect.right > GENERAL[
            "level_right_x"] or \
                projectile.rect.top < GENERAL["level_top_y"] or projectile.rect.bottom > \
                GENERAL["level_bottom_y"]:
            projectile.kill()


def get_distance_vector(vec1, vec2):
    """
    Returns magnitude of two vectors.
    """
    return (vec1 - vec2).magnitude()


def get_distance(location_a, location_b):
    """
    Returns distance between two coordinates.
    """
    vector_a = pygame.math.Vector2(location_a)
    vector_b = pygame.math.Vector2(location_b)
    distance = get_distance_vector(vector_a,
                                   vector_b)

    return distance


def get_direction(location_a, location_b):
    """
    Returns direction based on two vectors.
    """
    vector_a = pygame.math.Vector2(location_a)
    vector_b = pygame.math.Vector2(location_b)
    direction = (vector_a - vector_b).normalize()

    return direction


def get_new_portal_center(side):
    """
    Generates random coordinates within a range
        depending on the portals side.
    """
    if side == "left":
        x = randint(PORTAL["left_x_min"],
                    PORTAL["left_x_max"])
    else:
        x = randint(PORTAL["right_x_min"],
                    PORTAL["right_x_max"])
    y = randint(PORTAL["y_min"],
                PORTAL["y_max"])

    return x, y


def relocate_player(new_center):
    """
    Relocates Player to the given coordinate.
    """
    player_sprite.sprite.rect.center = new_center
    player_sprite.sprite.hitbox.center = new_center


def get_sprites(sheet, number_sprites, width, height, scale, color):
    """
    Returns a list of individual sprites taken from the given sheet.

    :param sheet: Image file containing the sprites (png).
    :param number_sprites: Number of sprites to obtain (int).
    :param width: Sprite width in pixels (int).
    :param height: Sprite height in pixels (int).
    :param scale: Magnification in comparison with the original (int).
    :param color: Pixel color of background to remove (pygame wants this)(str rgb).

    :return: List of sprite images.
    """
    sprites = []
    for i in range(0, number_sprites):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), ((i * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        sprites.append(image)

    return sprites
