from settings.general_settings import GENERAL

from utilities.sprite_groups import player_sprite, player_projectile_sprites, bomb_sprites, enemy_sprites, \
    enemy_projectile_sprites, \
    all_creeper_sprites

from utilities.game_physics import get_distance


def handle_outgoing_projectiles():
    """
    Checks all Player projectiles and Enemies and applies damage if collision.
    """
    # Collision with Enemies
    for projectile in player_projectile_sprites:
        for enemy in enemy_sprites:
            if projectile.rect.colliderect(enemy.hitbox) and not enemy.death:
                enemy.health -= projectile.damage
                projectile.kill_self()

    # Collision with Creepers
    for projectile in player_projectile_sprites:
        for creeper in all_creeper_sprites:
            if projectile.rect.colliderect(creeper.hitbox):
                creeper.health -= projectile.damage
                projectile.kill_self()

            # Check collision with walls
            if projectile.rect.left < GENERAL["level_left_x"] or projectile.rect.right > \
                    GENERAL[
                        "level_right_x"] or \
                    projectile.rect.top < GENERAL["level_top_y"] or projectile.rect.bottom > \
                    GENERAL["level_bottom_y"]:
                projectile.kill_self()


def handle_outgoing_bombs():
    """
    Checks for damage caused by Player Bomb.
    """
    for bomb in bomb_sprites:
        if bomb.explode and not bomb.dealt_damage:
            # Because of small offset trigger detonation by distance

            # Enemies
            for enemy in enemy_sprites:
                distance = get_distance(enemy.rect.center,
                                        bomb.rect.center)
                # Only deal damage if Bomb has damage left
                if distance < bomb.damage_radius and bomb.damage > 0:
                    old_enemy_health = enemy.health
                    enemy.health -= bomb.damage - (bomb.damage / bomb.damage_radius * distance)
                    bomb.damage -= old_enemy_health

            # Creepers
            for creeper in all_creeper_sprites:
                distance = get_distance(creeper.rect.center,
                                        bomb.rect.center)
                # Only deal damage if Bomb has damage left
                if distance < bomb.damage_radius and bomb.damage > 0:
                    old_creeper_health = creeper.health
                    creeper.health -= bomb.damage - (bomb.damage / bomb.damage_radius * distance)
                    bomb.damage -= old_creeper_health

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