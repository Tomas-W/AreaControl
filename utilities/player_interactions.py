from utilities.sprite_groups import player_sprite, skull_sprites, energy_sprites, coin_sprites, \
    health_potion_sprites


def buy_bullet_upgrade(game, bullet_stats):
    from settings.player_settings import PLAYER
    if game.player.coin_level >= int(
            game.player.bullet_upgrade_cost * game.player.buy_multiplier):
        game.player.coin_level -= int(
            game.player.bullet_upgrade_cost * game.player.buy_multiplier)
        game.buy_tick = game.wave_pause_ticks
        game.player.buy_multiplier += game.player.buy_multiplier_addition
        bullet_stats["damage"] *= 1.05
        bullet_stats["speed"] *= 1.05
        PLAYER["shoot_cooldown"] -= 0.4
        return True


def buy_bomb_upgrade(game, bomb_stats):
    if game.player.coin_level >= int(
            game.player.bomb_upgrade_cost * game.player.buy_multiplier):
        game.player.coin_level -= int(
            game.player.bomb_upgrade_cost * game.player.buy_multiplier)
        game.buy_tick = game.wave_pause_ticks
        game.player.buy_multiplier += game.player.buy_multiplier_addition
        bomb_stats["damage"] *= 1.07
        return True
    return False


def buy_bomb(game, player):
    if game.player.skull_level >= int(
            game.player.buy_bomb_cost * game.player.buy_multiplier):
        game.player.skull_level -= int(
            game.player.buy_bomb_cost * game.player.buy_multiplier)
        game.buy_tick = game.wave_pause_ticks
        game.player.buy_multiplier += game.player.buy_multiplier_addition
        player.total_bombs += 1
        return True
    return False


def buy_portal(game, player):
    if game.player.energy_level >= int(
            game.player.buy_bomb_cost * game.player.buy_multiplier):
        game.player.energy_level -= int(
            game.player.buy_bomb_cost * game.player.buy_multiplier)
        game.buy_tick = game.wave_pause_ticks
        game.player.buy_multiplier += game.player.buy_multiplier_addition
        player.total_portals += 1
        return True
    return False


def handle_pickups():
    """
    Checks all PickUps and Player location and applies PickUp stats if collision.
    """
    for energy in energy_sprites:
        if energy.hitbox.colliderect(player_sprite.sprite.hitbox):
            player_sprite.sprite.energy_level += energy.boost
            energy.kill_self()

    for skull in skull_sprites:
        if skull.hitbox.colliderect(player_sprite.sprite.hitbox):
            player_sprite.sprite.skull_level += skull.boost
            skull.kill_self()

    for coin in coin_sprites:
        if coin.hitbox.colliderect(player_sprite.sprite.hitbox):
            player_sprite.sprite.coin_level += coin.boost
            coin.kill_self()

    for health_potion in health_potion_sprites:
        if health_potion.hitbox.colliderect(player_sprite.sprite.hitbox):
            player_sprite.sprite.total_health_potions += 1
            health_potion.kill_self()