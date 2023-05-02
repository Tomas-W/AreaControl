# ####################################################### #
# ####################### PORTAL ####################### #
PORTAL_SIZE = 1
PORTAL = {
    "size": PORTAL_SIZE,
    "left_x_min": 800,
    "left_x_max": 1600,
    "right_x_min": 1800,
    "right_x_max": 2700,
    "y_min": 900,
    "y_max": 2000,

    "min_distance_player": 250,
    "visible_tick": 180,
    "transparency": 130,
    "active_transparency": 100,

    "hitbox": ((23 * PORTAL_SIZE), (20 * PORTAL_SIZE),
               (30 * PORTAL_SIZE), (40 * PORTAL_SIZE)),
    "hitbox_left_offset": (23 * PORTAL_SIZE),
    "hitbox_right_offset": (20 * PORTAL_SIZE),

    "sprite_width": 75,
    "sprite_height": 85,
}

# ##################################################### #
# ####################### SKULL ####################### #
SKULL_SIZE = 1
SKULL = {
    "size": SKULL_SIZE,
    "transparency": None,

    "sprite_width": 75,
    "sprite_height": 100,
}

# ###################################################### #
# ####################### ENERGY ####################### #
ENERGY_SIZE = 0.5
ENERGY = {
    "size": ENERGY_SIZE,
    "transparency": None,

    "hitbox": ((25 * ENERGY_SIZE), (25 * ENERGY_SIZE),
               (50 * ENERGY_SIZE), (50 * ENERGY_SIZE)),
    "hitbox_offset_x": 25,
    "hitbox_offset_y": 25,

    "sprite_width": 100,
    "sprite_height": 100,
}


