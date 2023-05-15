from settings.general_settings import BAT_SIZE, FISH_SIZE
from sprites.creeper_sprites import BAT_SPRITES, BAT_SPRITES_FLIPPED, FISH_SPRITES, \
    FISH_SPRITES_FLIPPED

# ############################################################ #
# ############################ BAT ########################### #
BAT = {
    # main
    "start_position": [(1100, 1000), (3200, 1000), (1100, 2500), (3200, 2500)],
    "spawn_opacity": 0,
    "size": BAT_SIZE,
    "name": "bat",

    # attributes
    "health": 60,
    "damage": 50,
    "speed": 2,
    "idle_speed": 2,
    "chase_speed": 7,
    "circle_radius": 350,
    "angle": [x for x in range(-180, 180, 10)],
    "angle_adjustment": 0.5,
    "wave_spawns": [3, 4, 12, 0, 5, 8, 15],

    # states
    "spawn": None,
    "idle": True,
    "chase": False,
    "strike": None,
    "shoot": None,
    "death": None,
    # state distance
    "chase_distance": 350,
    "strike_distance": None,
    "shoot_distance": None,

    # frame attributes
    "frame": 0,
    "frame_ticks": 0,
    "spawn_ticks": 0,
    # ticks per frame
    "idle_ticks": 6,
    "chase_ticks": 4,
    "strike_ticks": None,
    "shoot_ticks": None,
    "death_ticks": None,
    # action at what frame (starts at 0)
    "strike_frame": None,
    "shoot_frame": None,
    "death_frame": None,

    # sprites
    "sprites": BAT_SPRITES,
    "sprites_flipped": BAT_SPRITES_FLIPPED,
    # initial image
    "image": BAT_SPRITES[0],
    "flip_image": False,

    # hitbox
    "hitbox": ((8 * BAT_SIZE), (8 * BAT_SIZE),
               (20 * BAT_SIZE), (20 * BAT_SIZE)),
    "hitbox_offset_x": (8 * BAT_SIZE),
    "hitbox_offset_y": (8 * BAT_SIZE),
    # offsets
    "shoot_offset_x": None,
    "shoot_offset_y": None,
}

# ############################################################# #
# ############################ FISH ########################### #
FISH = {
    "start_position": [(x, y) for x in range(1000, 3301, 150) for y in range(900, 2601, 150)],
    "spawn_opacity": 0,
    "size": FISH_SIZE,
    "name": "fish",

    # attributes
    "health": 60,
    "damage": 50,
    "speed": 2,
    "idle_speed": 2,
    "chase_speed": 6,
    "circle_radius": 100,
    "angle": [x for x in range(-180, 180, 10)],
    "angle_adjustment": 1,
    "wave_spawns": [3, 3, 0, 20, 7, 11, 7],

    # states
    "spawn": None,
    "idle": True,
    "chase": False,
    "strike": None,
    "shoot": None,
    "death": None,

    # state distance
    "chase_distance": 225,
    "strike_distance": None,
    "shoot_distance": None,

    # frame attributes
    "frame": 0,
    "frame_ticks": 0,
    "spawn_ticks": 0,
    # ticks per frame
    "idle_ticks": 6,
    "chase_ticks": 4,
    "strike_ticks": None,
    "shoot_ticks": None,
    "death_ticks": None,
    # action at what frame (starts at 0)
    "strike_frame": None,
    "shoot_frame": None,
    "death_frame": None,

    # sprites
    "sprites": FISH_SPRITES,
    "sprites_flipped": FISH_SPRITES_FLIPPED,
    # initial image
    "image": FISH_SPRITES[0],
    "flip_image": False,

    # hitbox
    "hitbox": ((10 * FISH_SIZE), (10 * FISH_SIZE),
               (44 * FISH_SIZE), (35 * FISH_SIZE)),
    "hitbox_offset_x": (10 * FISH_SIZE),
    "hitbox_offset_y": (10 * FISH_SIZE),
    # offsets
    "shoot_offset_x": None,
    "shoot_offset_y": None,
}
