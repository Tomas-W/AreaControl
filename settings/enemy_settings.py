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
    SKULL_COLLECTOR_WALK_SPRITES, SKULL_COLLECTOR_DEATH_SPRITES_FLIPPED, \
    RUSHER_DEATH_SPRITES_FLIPPED

SKULL_COLLECTOR = {
    "start_position": (1280, 720),
    "size": SKULL_COLLECTOR_SIZE,
    "health": 300,
    "damage": None,
    "speed": 2,
    "walk_speed": 2,
    "run_speed": None,
    # state
    "idle": False,
    "walk": True,
    "run": False,
    "strike": False,
    "shoot": False,
    "death": False,
    # state duration
    "idle_duration": None,
    "walk_duration": None,
    "run_duration": None,
    # state distance
    "walk_distance": None,
    "run_distance": None,
    "strike_distance": None,
    "shoot_distance": 350,

    # ticks per frame
    "idle_ticks": None,
    "walk_ticks": 4,
    "run_ticks": None,
    "strike_ticks": None,
    "shoot_ticks": 5,
    "death_ticks": 4,
    # action at what frame
    "strike_frame": None,
    "shoot_frame": 5,
    "death_frame": 8,
    # track state for tick reset
    "current_state": "walk",
    "last_state": "walk",

    # sprites
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
    "death_sprites_flipped": SKULL_COLLECTOR_DEATH_SPRITES_FLIPPED,
    # initial image
    "image": SKULL_COLLECTOR_WALK_SPRITES[0],
    "flip_image": False,

    # hitbox
    "hitbox": ((16 * SKULL_COLLECTOR_SIZE), (20 * SKULL_COLLECTOR_SIZE),
               (24 * SKULL_COLLECTOR_SIZE), (44 * SKULL_COLLECTOR_SIZE)),
    "hitbox_offset_x": (16 * SKULL_COLLECTOR_SIZE),
    "hitbox_offset_y": (20 * SKULL_COLLECTOR_SIZE),
    # shooting offset
    "shoot_offset_x": (21 * SKULL_COLLECTOR_SIZE),
    "shoot_offset_y": (-6 * SKULL_COLLECTOR_SIZE),
}

# ############################################################## #
# ########################### RUSHER ########################### #
RUSHER = {
    "start_position": (1280, 920),
    "size": RUSHER_SIZE,
    "health": 120,
    "damage": 40,
    "speed": 5,
    "walk_speed": None,
    "run_speed": 5,
    # state
    "idle": True,
    "walk": False,
    "run": False,
    "strike": False,
    "shoot": False,
    "death": False,
    # state duration
    "idle_duration": None,
    "walk_duration": None,
    "run_duration": None,
    # state distance
    "walk_distance": None,
    "run_distance": 400,
    "strike_distance": 40,
    "shoot_distance": None,
    # ticks per frame
    "idle_ticks": 5,
    "walk_ticks": None,
    "run_ticks": 5,
    "strike_ticks": 4,
    "shoot_ticks": None,
    "death_ticks": 3,
    # action at what frame (starts at 0)
    "strike_frame": 5,
    "shoot_frame": None,
    "death_frame": 18,
    # track state for tick reset
    "current_state": "idle",
    "last_state": "idle",
    # sprites
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
    "death_sprites_flipped": RUSHER_DEATH_SPRITES_FLIPPED,
    # initial image
    "image": RUSHER_IDLE_SPRITES[0],
    "flip_image": False,
    # hitbox
    "hitbox": ((15 * RUSHER_SIZE), (20 * RUSHER_SIZE),
               (21 * RUSHER_SIZE), (25 * RUSHER_SIZE)),
    "hitbox_offset_x": 15,
    "hitbox_offset_y": 20,

    "shoot_offset_x": None,
    "shoot_offset_y": None,
}

# ############################################################### #
# ############################ GOLEM ############################ #
GOLEM = {
    "start_position": (1750, 1100),
    "size": GOLEM_SIZE,
    "speed": 1,
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

    "shoot_offset_x": None,
    "shoot_offset_y": None,
}
