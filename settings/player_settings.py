# ################################################################ #
# ############################ PLAYER ############################ #
PLAYER_SIZE = 0.4
PLAYER = {
    "start_position": (1750, 1450),
    "size": PLAYER_SIZE,
    "hitbox_size": 0.8,
    "speed": 10,
    "health": 1000,

    "shoot_cooldown": 60,
    "muzzle_flash_cooldown": 8,

    "left_portal": None,
    "right_portal": None,

    "new_location_tick": 120,
    "invincibility_ticks": 240,

    "hitbox": (0, 0,
               (214 * PLAYER_SIZE), (174 * PLAYER_SIZE)),
}
