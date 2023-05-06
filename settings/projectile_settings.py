# #################################################################### #
# ############################ FIRE SKULL ############################ #
from settings.general_settings import FIRE_SKULL_SIZE, BULLET_SIZE
from settings.player_settings import PLAYER_SIZE
from sprites.projectile_sprites import FIRE_SKULL_SPRITE, BULLET_SPRITE

FIRE_SKULL = {
    "name": "fire_skull",
    "size": FIRE_SKULL_SIZE,
    "speed": 4,
    "damage": 50,

    # sprites
    "sprite": FIRE_SKULL_SPRITE,

    "hitbox": (0, (10 * FIRE_SKULL_SIZE),
               (15 * FIRE_SKULL_SIZE), (15 * FIRE_SKULL_SIZE)),
    "hitbox_x_offset": (0 * FIRE_SKULL_SIZE),
    "hitbox_y_offset": (10 * FIRE_SKULL_SIZE),
}

# ################################################################ #
# ############################ BULLET ############################ #
BULLET = {
    "name": "bullet",
    "size": BULLET_SIZE,
    "speed": 4,
    "damage": 25,

    # sprites
    "sprite": BULLET_SPRITE,

    "hitbox": (0, 0,
               (16 * BULLET_SIZE), (16 * BULLET_SIZE)),
    "hitbox_x_offset": (0 * BULLET_SIZE),
    "hitbox_y_offset": (0 * BULLET_SIZE),
}
