from random import randint

import pygame

from settings.general_settings import GENERAL

all_sprites = pygame.sprite.Group()
# Characters
player_sprite = pygame.sprite.GroupSingle()
enemy_sprites = pygame.sprite.Group()
# Projectiles
all_projectile_sprites = pygame.sprite.Group()
player_projectile_sprites = pygame.sprite.Group()
enemy_projectile_sprites = pygame.sprite.Group()
bomb_sprites = pygame.sprite.Group()
# Creepers
all_creeper_sprites = pygame.sprite.Group()
bat_sprites = pygame.sprite.Group()
fish_sprites = pygame.sprite.Group()
# Pickups
all_pickup_sprites = pygame.sprite.Group()
skull_sprites = pygame.sprite.Group()
energy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()
# Interactives
all_interactives_sprites = pygame.sprite.Group()
portal_sprites = pygame.sprite.Group()


def buy_bullet_upgrade(game, bullet_stats):
    if game.player.coin_level > int(
            game.player.bullet_upgrade_cost * game.player.buy_multiplier):
        game.player.coin_level -= int(
            game.player.bullet_upgrade_cost * game.player.buy_multiplier)
        game.buy_tick = game.wave_pause_ticks
        game.player.buy_multiplier *= game.player.buy_multiplier_addition
        bullet_stats["damage"] *= 1.05
        bullet_stats["speed"] *= 1.05


def buy_bomb_upgrade(game, bomb_stats):
    if game.player.coin_level > int(
            game.player.bomb_upgrade_cost * game.player.buy_multiplier):
        game.player.coin_level -= int(
            game.player.bomb_upgrade_cost * game.player.buy_multiplier)
        game.buy_tick = game.wave_pause_ticks
        game.player.buy_multiplier *= game.player.buy_multiplier_addition
        bomb_stats["damage"] *= 1.07


def buy_bomb(game, player):
    if game.player.skull_level > int(
            game.player.buy_bomb_cost * game.player.buy_multiplier):
        game.player.skull_level -= int(
            game.player.buy_bomb_cost * game.player.buy_multiplier)
        game.buy_tick = game.wave_pause_ticks
        game.player.buy_multiplier *= game.player.buy_multiplier_addition
        player.total_bombs += 1


def buy_portal(game, player):
    if game.player.energy_level > int(
            game.player.buy_bomb_cost * game.player.buy_multiplier):
        game.player.energy_level -= int(
            game.player.buy_bomb_cost * game.player.buy_multiplier)
        game.buy_tick = game.wave_pause_ticks
        game.player.buy_multiplier *= game.player.buy_multiplier_addition
        # player.total_portals += 1


def handle_pickups():
    """
    Checks all PickUps and Player location and applies PickUp stats if collision.
    """
    for energy in energy_sprites:
        if energy.hitbox.colliderect(player_sprite.sprite.hitbox):
            player_sprite.sprite.energy_level += energy.boost
            energy.kill()

    for skull in skull_sprites:
        if skull.hitbox.colliderect(player_sprite.sprite.hitbox):
            player_sprite.sprite.skull_level += skull.boost
            skull.kill()

    for coin in coin_sprites:
        if coin.hitbox.colliderect(player_sprite.sprite.hitbox):
            player_sprite.sprite.coin_level += coin.boost
            coin.kill()


def handle_outgoing_projectiles():
    """
    Checks all Player projectiles and Enemies and applies damage if collision.
    """
    # Collision with Enemies
    for projectile in player_projectile_sprites:
        for enemy in enemy_sprites:
            if projectile.rect.colliderect(enemy.hitbox) and not enemy.death:
                enemy.health -= projectile.damage
                projectile.kill()

    # Collision with Creepers
    for projectile in player_projectile_sprites:
        for creeper in all_creeper_sprites:
            if projectile.rect.colliderect(creeper.hitbox):
                creeper.health -= projectile.damage
                projectile.kill()

            # Check collision with walls
            if projectile.rect.left < GENERAL["level_left_x"] or projectile.rect.right > \
                    GENERAL[
                        "level_right_x"] or \
                    projectile.rect.top < GENERAL["level_top_y"] or projectile.rect.bottom > \
                    GENERAL["level_bottom_y"]:
                projectile.kill()


def handle_outgoing_bombs():
    """
    Checks for damage caused by Player Bomb.
    """
    for bomb in bomb_sprites:
        if bomb.explode and not bomb.dealt_damage:

            # Because of small offset trigger detonation by distance
            for enemy in enemy_sprites:
                distance = get_distance(enemy.rect.center,
                                        bomb.rect.center)
                # Only deal damage if Bomb has damage left
                if distance < bomb.damage_radius and bomb.damage > 0:
                    old_enemy_health = enemy.health
                    enemy.health -= bomb.damage - (bomb.damage / bomb.damage_radius * distance)
                    bomb.damage -= old_enemy_health
            # Disable bomb damage
            bomb.dealt_damage = True


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
