# ############################################################ #
# ############################ BAT ########################### #
from settings.general_settings import BAT_SIZE
from sprites.creeper_sprites import BAT_SPRITES, BAT_SPRITES_FLIPPED

BAT = {
    "start_position": [(800, 900), (2700, 900), (800, 2000), (2700, 2000)],
    "name": "bat",
    "size": BAT_SIZE,
    "health": 60,
    "damage": 50,
    "speed": 2,
    "idle_speed": 2,
    "chase_speed": 4,
    "circle_radius": 150,
    "angle": 90,

    # state
    "idle": True,
    "chase": False,
    "strike": None,
    "shoot": None,
    "death": None,

    # state distance
    "chase_distance": 300,
    "strike_distance": None,
    "shoot_distance": None,

    # frame attributes
    "frame": 0,
    "frame_ticks": 0,
    # ticks per frame
    "idle_ticks": 6,
    "chase_ticks": 4,
    "strike_ticks": None,
    "shoot_ticks": None,
    "death_ticks": None,

    # action at what frame
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