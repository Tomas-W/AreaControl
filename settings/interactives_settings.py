# ####################################################### #
# ####################### PORTAL ####################### #
from settings.general_settings import ENERGY_SIZE, SKULL_SIZE, PORTAL_SIZE, COIN_SIZE
from sprites.interactives_sprites import ENERGY_SPRITES, SKULL_SPRITES, COIN_SPRITES

PORTAL = {
    "size": PORTAL_SIZE,

    "min_distance_player": 250,
    "visible_tick": 180,
    "transparency": 130,
    "active_transparency": 100,

    "hitbox": ((23 * PORTAL_SIZE), (20 * PORTAL_SIZE),
               (30 * PORTAL_SIZE), (40 * PORTAL_SIZE)),
    "hitbox_left_offset": (23 * PORTAL_SIZE),
    "hitbox_right_offset": (20 * PORTAL_SIZE),
}

# ######################################################## #
# ####################### PICK UPS ####################### #
SKULL = {
    "name": "skull",
    "size": SKULL_SIZE,

    # attributes
    "transparency": 155,
    "boost": 1,

    # frame attributes
    "frame": 0,
    "frame_ticks": 0,
    "ticks_per_frame": 6,

    # sprites
    "sprites": SKULL_SPRITES,
    # initial image
    "image": SKULL_SPRITES[0],

    # hitbox
    "hitbox": ((20 * SKULL_SIZE), (25 * SKULL_SIZE),
               (35 * SKULL_SIZE), (50 * SKULL_SIZE)),
    "hitbox_offset_x": 20 * SKULL_SIZE,
    "hitbox_offset_y": 25 * SKULL_SIZE,
}

ENERGY = {
    "name": "energy",
    "size": ENERGY_SIZE,

    # attributes
    "transparency": 155,
    "boost": 1,

    # frame attributes
    "frame": 0,
    "frame_ticks": 0,
    "ticks_per_frame": 4,

    # sprites
    "sprites": ENERGY_SPRITES,
    # initial image
    "image": ENERGY_SPRITES[0],

    "hitbox": ((25 * ENERGY_SIZE), (25 * ENERGY_SIZE),
               (50 * ENERGY_SIZE), (50 * ENERGY_SIZE)),
    "hitbox_offset_x": 25 * ENERGY_SIZE,
    "hitbox_offset_y": 25 * ENERGY_SIZE,
}

COIN = {
    "name": "coin",
    "size": COIN_SIZE,
    "transparency": 155,
    "boost": 1,

    # frame attributes
    "frame": 0,
    "frame_ticks": 0,
    "ticks_per_frame": 5,

    # sprites
    "sprites": COIN_SPRITES,
    # initial image
    "image": COIN_SPRITES[0],

    "hitbox": ((50 * ENERGY_SIZE), (50 * ENERGY_SIZE),
               (100 * ENERGY_SIZE), (75 * ENERGY_SIZE)),
    "hitbox_offset_x": 50 * ENERGY_SIZE,
    "hitbox_offset_y": 50 * ENERGY_SIZE,
}
