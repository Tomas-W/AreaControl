# #################################################################### #
# ############################ FIRE SKULL ############################ #
from settings.general_settings import FLAMING_SKULL_SIZE, BULLET_SIZE
from settings.player_settings import PLAYER_SIZE
from sprites.projectile_sprites import FLAMING_SKULL_SPRITE, BULLET_SPRITE

FLAMING_SKULL = {
    "name": "flaming_skull",
    "size": FLAMING_SKULL_SIZE,
    "speed": 4,
    "damage": 50,

    # sprites
    "sprite": FLAMING_SKULL_SPRITE,

    "hitbox": (0, (10 * FLAMING_SKULL_SIZE),
               (15 * FLAMING_SKULL_SIZE), (15 * FLAMING_SKULL_SIZE)),
    "hitbox_x_offset": (0 * FLAMING_SKULL_SIZE),
    "hitbox_y_offset": (10 * FLAMING_SKULL_SIZE),
}

# ################################################################ #
# ############################ BULLET ############################ #
BULLET = {
    "name": "bullet",
    "size": BULLET_SIZE,
    "speed": 4,
    "damage": 60,

    # sprites
    "sprite": BULLET_SPRITE,

    "hitbox": (0, 0,
               (16 * BULLET_SIZE), (16 * BULLET_SIZE)),
    "hitbox_x_offset": (0 * BULLET_SIZE),
    "hitbox_y_offset": (0 * BULLET_SIZE),
}
