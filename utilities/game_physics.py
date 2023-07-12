from random import randint

import pygame

from settings.general_settings import GENERAL
from utilities.sprite_groups import player_sprite


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
        x = randint(GENERAL["left_x_min"],
                    GENERAL["left_x_max"])
    else:
        x = randint(GENERAL["right_x_min"],
                    GENERAL["right_x_max"])
    y = randint(GENERAL["y_min"],
                GENERAL["y_max"])

    return x, y


def relocate_player(new_center):
    """
    Relocates Player to the given coordinate.
    """
    player_sprite.sprite.rect.center = new_center
    player_sprite.sprite.hitbox.center = new_center