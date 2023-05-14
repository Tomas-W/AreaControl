from sprites.player_sprites import PLAYER_SPRITE, PLAYER_SHOOT_SPRITE

PLAYER_SIZE = 0.4
PLAYER = {
    "start_position": (1750, 1450),
    "size": PLAYER_SIZE,
    "name": "player",

    # attributes
    "hitbox_size": 0.8,
    "speed": 8,
    "health": 1000,
    "skull_level": 0,
    "energy_level": 0,
    "coin_level": 0,
    "wave_level": 0,
    "total_bombs": 3,

    # buy menu
    "buy_multiplier": 1.1,
    "buy_multiplier_addition": 1.3,
    "bullet_upgrade_cost": 4,
    "bomb_upgrade_cost": 6,
    "buy_bomb_cost": 1,
    "buy_portal_cost": 3,

    # states
    "shoot": False,
    "bomb": False,
    "is_invincible": False,

    # state durations
    "shoot_cooldown": 15,
    "muzzle_flash_cooldown": 8,
    "bomb_cooldown": 120,

    # portal
    "new_location": None,
    "teleport_location": None,
    "left_portal": None,
    "right_portal": None,
    # portal attributes
    "new_location_tick": 120,

    # invincibility attributes
    "invincibility_ticks": 240,

    # sprites
    "sprite": PLAYER_SPRITE,
    "shoot_sprite": PLAYER_SHOOT_SPRITE,
    "hitbox": ((25 * PLAYER_SIZE), (25 * PLAYER_SIZE),
               (170 * PLAYER_SIZE), (170 * PLAYER_SIZE)),
    "sprite_width": 220,
    "sprite_height": 220,

}
