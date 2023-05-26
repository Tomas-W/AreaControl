import os
import sys

from settings.general_settings import FLAMING_SKULL_SIZE, BULLET_SIZE, BOMB_SIZE
from sprites.projectile_sprites import FLAMING_SKULL_SPRITE, BULLET_SPRITE, BOMB_SPRITES

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# #################################################################### #
# ############################ FLAMING SKULL ############################ #
FLAMING_SKULL = {
    "name": "flaming_skull",
    "size": FLAMING_SKULL_SIZE,
    "speed": 6,
    "damage": 50,

    # frame attributes
    "frame": None,
    "frame_ticks": None,
    # ticks per frame
    "image_ticks": None,

    # sprites
    "sprite_sheet": None,
    "sprite": FLAMING_SKULL_SPRITE,

    # sounds
    "spawn_sound_path": None,
    "death_sound_path": None,

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
    "speed": 14,
    "damage": 40,

    # frame attributes
    "frame": None,
    "frame_ticks": None,
    # ticks per frame
    "image_ticks": None,

    # sprites
    "sprite_sheet": None,
    "sprite": BULLET_SPRITE,

    # sounds
    "spawn_sound_path": os.path.join(base_dir, "sounds/pistol_shoot_sound.mp3"),
    "death_sound_path": None,

    "hitbox": ((0 * BULLET_SIZE), (0 * BULLET_SIZE),
               (16 * BULLET_SIZE), (16 * BULLET_SIZE)),
    "hitbox_x_offset": ((0 * BULLET_SIZE) * BULLET_SIZE),
    "hitbox_y_offset": ((0 * BULLET_SIZE) * BULLET_SIZE),
}

# ############################################################## #
# ############################ BOMB ############################ #
BOMB = {
    "name": "bomb",
    "size": BOMB_SIZE,
    "speed": 3,
    "damage": 500,

    # frame attributes
    "frame": 0,
    "frame_ticks": 0,
    # ticks per frame
    "image_ticks": 5,

    # sprites
    "sprite_sheet": BOMB_SPRITES,
    "sprite": BOMB_SPRITES[0],

    # sounds
    "spawn_sound_path": None,
    "death_sound_path": os.path.join(base_dir, "sounds/bomb_explosion_sound.mp3"),


    "hitbox": ((10 * BOMB_SIZE), (10 * BOMB_SIZE),
               (20 * BOMB_SIZE), (20 * BOMB_SIZE)),
    "hitbox_x_offset": (0 * BOMB_SIZE),
    "hitbox_y_offset": (0 * BOMB_SIZE),
}
