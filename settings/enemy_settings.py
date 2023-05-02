# ############################################################### #
# ####################### SKULL COLLECTOR ####################### #
from settings.general_settings import SKULL_COLLECTOR_SIZE, RUSHER_SIZE, GOLEM_SIZE
from sprites.enemy_sprites import GOLEM_DEATH_SPRITES, GOLEM_STRIKE_SPRITES, \
    GOLEM_STRIKE_SPRITES_FLIPPED, GOLEM_RUN_SPRITES_FLIPPED, GOLEM_RUN_SPRITES, \
    GOLEM_WALK_SPRITES_FLIPPED, GOLEM_WALK_SPRITES, RUSHER_DEATH_SPRITES, \
    RUSHER_STRIKE_SPRITES_FLIPPED, RUSHER_STRIKE_SPRITES, RUSHER_RUN_SPRITES_FLIPPED, \
    RUSHER_RUN_SPRITES, RUSHER_IDLE_SPRITES_FLIPPED, RUSHER_IDLE_SPRITES, \
    SKULL_COLLECTOR_DEATH_SPRITES, SKULL_COLLECTOR_SHOOT_SPRITES_FLIPPED, \
    SKULL_COLLECTOR_SHOOT_SPRITES, SKULL_COLLECTOR_WALK_SPRITES_FLIPPED, \
    SKULL_COLLECTOR_WALK_SPRITES

SKULL_COLLECTOR = {
    "start_position": (1400, 1250),
    "size": SKULL_COLLECTOR_SIZE,
    "health": 200,
    "damage": None,
    "walk_speed": 4,
    "run_speed": None,

    "idle": False,
    "walk": True,
    "run": False,
    "strike": False,
    "shoot": False,
    "death": False,

    "walk_duration": None,
    "run_duration": None,

    "walk_distance": None,
    "run_distance": None,
    "strike_distance": None,
    "shoot_distance": 350,

    "strike_tick": None,
    "shoot_tick": 65,
    "death_tick": 50,

    "idle_sprites": None,
    "idle_sprites_flipped": None,
    "walk_sprites": SKULL_COLLECTOR_WALK_SPRITES,
    "walk_sprites_flipped": SKULL_COLLECTOR_WALK_SPRITES_FLIPPED,
    "run_sprites": None,
    "run_sprites_flipped": None,
    "strike_sprites": None,
    "strike_sprites_flipped": None,
    "shoot_sprites": SKULL_COLLECTOR_SHOOT_SPRITES,
    "shoot_sprites_flipped": SKULL_COLLECTOR_SHOOT_SPRITES_FLIPPED,
    "death_sprites": SKULL_COLLECTOR_DEATH_SPRITES,

    "image": SKULL_COLLECTOR_WALK_SPRITES[0],
    "flip_image": False,

    "hitbox": ((68 * SKULL_COLLECTOR_SIZE), (67 * SKULL_COLLECTOR_SIZE),
               (25 * SKULL_COLLECTOR_SIZE), (47 * SKULL_COLLECTOR_SIZE)),
    "hitbox_offset_x": (71 * SKULL_COLLECTOR_SIZE),
    "hitbox_offset_y": (65 * SKULL_COLLECTOR_SIZE),

    "fire_skull_x_offset": 20,
    "fire_skull_y_offset": -55,
}

# ############################################################## #
# ########################### RUSHER ########################### #
RUSHER = {
    "start_position": (2100, 1250),
    "size": RUSHER_SIZE,
    "walk_speed": None,
    "run_speed": 8,
    "health": 120,
    "damage": None,
    "strike_damage": 100,

    "idle": True,
    "walk": False,
    "run": False,
    "strike": False,
    "shoot": False,
    "death": False,

    "walk_duration": None,
    "run_duration": None,

    "walk_distance": None,
    "run_distance": 400,
    "strike_distance": 75,
    "shoot_distance": None,

    "strike_tick": 16,
    "shoot_tick": None,
    "death_tick": 71,

    "idle_sprites": RUSHER_IDLE_SPRITES,
    "idle_sprites_flipped": RUSHER_IDLE_SPRITES_FLIPPED,
    "walk_sprites": None,
    "walk_sprites_flipped": None,
    "run_sprites": RUSHER_RUN_SPRITES,
    "run_sprites_flipped": RUSHER_RUN_SPRITES_FLIPPED,
    "strike_sprites": RUSHER_STRIKE_SPRITES,
    "strike_sprites_flipped": RUSHER_STRIKE_SPRITES_FLIPPED,
    "shoot_sprites": None,
    "shoot_sprites_flipped": None,
    "death_sprites": RUSHER_DEATH_SPRITES,

    "image": RUSHER_IDLE_SPRITES[0],
    "flip_image": False,

    "hitbox": ((30 * RUSHER_SIZE), (35 * RUSHER_SIZE),
               (25 * RUSHER_SIZE), (28 * RUSHER_SIZE)),
    "hitbox_offset_x": 0,
    "hitbox_offset_y": 0,
}

# ############################################################### #
# ############################ GOLEM ############################ #
GOLEM = {
    "start_position": (1750, 1100),
    "size": GOLEM_SIZE,
    "walk_speed": 1,
    "run_speed": 5,
    "health": 500,
    "damage": None,
    "strike_damage": 200,

    "idle": False,
    "walk": True,
    "run": False,
    "strike": False,
    "shoot": False,
    "death": False,

    "walk_duration": 180,
    "run_duration": 120,

    "walk_distance": None,
    "run_distance": None,
    "strike_distance": 75,
    "shoot_distance": None,

    "strike_tick": None,
    "shoot_tick": None,
    "death_tick": None,

    "idle_sprites": None,
    "idle_sprites_flipped": None,
    "walk_sprites": GOLEM_WALK_SPRITES,
    "walk_sprites_flipped": GOLEM_WALK_SPRITES_FLIPPED,
    "run_sprites": GOLEM_RUN_SPRITES,
    "run_sprites_flipped": GOLEM_RUN_SPRITES_FLIPPED,
    "strike_sprites": GOLEM_STRIKE_SPRITES,
    "strike_sprites_flipped": GOLEM_STRIKE_SPRITES_FLIPPED,
    "shoot_sprites": None,
    "shoot_sprites_flipped": None,
    "death_sprites": GOLEM_DEATH_SPRITES,

    "image": GOLEM_WALK_SPRITES[0],
    "flip_image": False,

    "hitbox": ((93 * GOLEM_SIZE), (93 * GOLEM_SIZE),
               (70 * GOLEM_SIZE), (70 * GOLEM_SIZE)),
    "hitbox_offset_x": (93 * GOLEM_SIZE),
    "hitbox_offset_y": (93 * GOLEM_SIZE),
}
