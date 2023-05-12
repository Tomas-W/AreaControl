from sprites.player_sprites import PLAYER_SPRITE, PLAYER_SHOOT_SPRITE

PLAYER_SIZE = 0.4
PLAYER = {
    "start_position": (1750, 1450),
    "size": PLAYER_SIZE,

    # attributes
    "hitbox_size": 0.8,
    "speed": 5,
    "health": 1000,
    "skull_level": 34,
    "energy_level": 66,
    "coin_level": 25,

    # states
    "shoot": False,
    "bomb": False,
    "is_invincible": False,

    # state durations
    "shoot_cooldown": 15,
    "muzzle_flash_cooldown": 8,
    "bomb_cooldown": 12,

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
