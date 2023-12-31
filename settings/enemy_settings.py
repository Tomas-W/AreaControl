import os
import sys

from settings.general_settings import SKULL_COLLECTOR_SIZE, RUSHER_SIZE, GOLEM_SIZE
from sprites.enemy_sprites import GOLEM_DEATH_SPRITES, GOLEM_STRIKE_SPRITES, \
    GOLEM_STRIKE_SPRITES_FLIPPED, GOLEM_RUN_SPRITES_FLIPPED, GOLEM_RUN_SPRITES, \
    GOLEM_WALK_SPRITES_FLIPPED, GOLEM_WALK_SPRITES, RUSHER_DEATH_SPRITES, \
    RUSHER_STRIKE_SPRITES_FLIPPED, RUSHER_STRIKE_SPRITES, RUSHER_RUN_SPRITES_FLIPPED, \
    RUSHER_RUN_SPRITES, RUSHER_IDLE_SPRITES_FLIPPED, RUSHER_IDLE_SPRITES, \
    SKULL_COLLECTOR_DEATH_SPRITES, SKULL_COLLECTOR_SHOOT_SPRITES_FLIPPED, \
    SKULL_COLLECTOR_SHOOT_SPRITES, SKULL_COLLECTOR_WALK_SPRITES_FLIPPED, \
    SKULL_COLLECTOR_WALK_SPRITES, SKULL_COLLECTOR_DEATH_SPRITES_FLIPPED, \
    RUSHER_DEATH_SPRITES_FLIPPED, GOLEM_DEATH_SPRITES_FLIPPED, RUSHER_SPAWN_SPRITES

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# skull = [2, 3, 8, 3, 7, 7, 14]
# rush = [3, 7, 3, 6, 7, 11, 4]
# bat = [3, 4, 12, 0, 5, 8, 15]
# fish = [3, 3, 0, 20, 7, 11, 7]
# ############################################################### #
# ####################### SKULL COLLECTOR ####################### #
SKULL_COLLECTOR = {
    # main
    "start_position": [(1000, 560), (1400, 560), (1800, 560), (2200, 560), (2600, 560), (3000, 560),
                       (1000, 2950), (1400, 2950), (1800, 2950), (2200, 2950), (2600, 2950), (3000, 2950)],
    "spawn_opacity": 0,
    "size": SKULL_COLLECTOR_SIZE,
    "name": "skull_collector",

    # attributes
    "health": 260,
    "damage": None,
    "speed": 4,
    "walk_speed": 3,
    "run_speed": None,
    "chase_state": "random",
    "wave_spawns": [2, 3, 8, 3, 7, 7, 14],

    # states
    "spawn": True,
    "idle": None,
    "walk": False,
    "run": None,
    "strike": None,
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

    # frame attributes
    "frame": 0,
    "frame_ticks": 0,
    # ticks per frame
    "spawn_ticks": None,
    "idle_ticks": None,
    "walk_ticks": 4,
    "run_ticks": None,
    "strike_ticks": None,
    "shoot_ticks": 5,
    "death_ticks": 4,
    # action at what frame (starts at 0)
    "strike_frame": None,
    "shoot_frame": 5,
    "death_frame": 8,
    # track state for frame reset
    "current_state": "walk",
    "last_state": "walk",

    # sprites
    "spawn_sprites": None,
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

    # sounds
    "death_sound_path": os.path.join(base_dir, "sounds/skull_collector_death_sound.mp3"),
    "attack_sound_path": None,

    # hitbox
    "hitbox": ((16 * SKULL_COLLECTOR_SIZE), (20 * SKULL_COLLECTOR_SIZE),
               (24 * SKULL_COLLECTOR_SIZE), (44 * SKULL_COLLECTOR_SIZE)),
    "hitbox_offset_x": (16 * SKULL_COLLECTOR_SIZE),
    "hitbox_offset_y": (20 * SKULL_COLLECTOR_SIZE),
    # offsets
    "shoot_offset_x": (21 * SKULL_COLLECTOR_SIZE),
    "shoot_offset_y": (-6 * SKULL_COLLECTOR_SIZE),
}

# ############################################################## #
# ########################### RUSHER ########################### #
RUSHER = {
    # main
    "start_position": [(x, y) for x in range(1000, 3301, 130) for y in range(900, 2601, 140)],
    "spawn_opacity": 0,
    "size": RUSHER_SIZE,
    "name": "rusher",

    # attributes
    "health": 105,
    "damage": 40,
    "speed": 7,
    "walk_speed": None,
    "run_speed": 7,
    "chase_state": "player",
    "wave_spawns": [3, 7, 3, 6, 7, 11, 4],

    # states
    "spawn": True,
    "idle": False,
    "walk": None,
    "run": False,
    "strike": False,
    "shoot": None,
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

    # frame attributes
    "frame": 0,
    "frame_ticks": 0,
    # ticks per frame
    "spawn_ticks": 5,
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
    # track state for frame  reset
    "current_state": "idle",
    "last_state": "idle",

    # sprites
    "spawn_sprites": RUSHER_SPAWN_SPRITES,
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
    "image": RUSHER_SPAWN_SPRITES[0],
    "flip_image": False,

    # sounds
    "death_sound_path": os.path.join(base_dir, "sounds/rusher_death_sound.mp3"),
    "attack_sound_path": os.path.join(base_dir, "sounds/rusher_strike_sound.mp3"),

    # hitbox
    "hitbox": ((15 * RUSHER_SIZE), (20 * RUSHER_SIZE),
               (21 * RUSHER_SIZE), (25 * RUSHER_SIZE)),
    "hitbox_offset_x": 15 * RUSHER_SIZE,
    "hitbox_offset_y": 20 * RUSHER_SIZE,
    # offsets
    "shoot_offset_x": None,
    "shoot_offset_y": None,
}

# ############################################################### #
# ############################ GOLEM ############################ #
GOLEM = {
    "start_position": (1750, 1100),
    "spawn_opacity": 0,
    "size": GOLEM_SIZE,

    # attributes
    "speed": 1,
    "walk_speed": 1,
    "run_speed": 3,
    "chase_state": "player",
    "health": 720,
    "damage": 150,

    # states
    "spawn": True,
    "idle": False,
    "walk": False,
    "run": False,
    "strike": False,
    "shoot": False,
    "death": False,
    # state duration
    "walk_duration": 180,
    "run_duration": 120,
    # state distance
    "walk_distance": None,
    "run_distance": None,
    "strike_distance": 75,
    "shoot_distance": None,

    # frame attributes
    "frame": 0,
    "frame_ticks": 0,
    # ticks per frame
    "spawn_ticks": None,
    "idle_ticks": 5,
    "walk_ticks": 5,
    "run_ticks": 4,
    "strike_ticks": 4,
    "shoot_ticks": None,
    "death_ticks": 5,
    # action at what frame
    "strike_frame": 5,
    "shoot_frame": None,
    "death_frame": 8,
    # track state for frame  reset
    "current_state": "idle",
    "last_st    ate": "idle",

    # sprites
    "spawn_sprites": None,
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
    "death_sprites_flipped": GOLEM_DEATH_SPRITES_FLIPPED,
    # initial image
    "image": GOLEM_WALK_SPRITES[0],
    "flip_image": False,

    # hitbox
    "hitbox": ((93 * GOLEM_SIZE), (93 * GOLEM_SIZE),
               (70 * GOLEM_SIZE), (70 * GOLEM_SIZE)),
    "hitbox_offset_x": (93 * GOLEM_SIZE),
    "hitbox_offset_y": (93 * GOLEM_SIZE),
    # offsets
    "shoot_offset_x": None,
    "shoot_offset_y": None,
}

# ############################################################### #
# ############################ ARCHER ########################### #
ARCHER = {
    "start_position": (1280, 720),
    "spawn_opacity": 0,
    "size": SKULL_COLLECTOR_SIZE,

    # attributes
    "health": 170,
    "damage": None,
    "speed": 2,
    "walk_speed": 2,
    "run_speed": 3,
    "chase_state": "player",

    # states
    "spawn": True,
    "idle": False,
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
    "run_distance": None,
    "strike_distance": None,
    "shoot_distance": 150,

    # frame attributes
    "frame": 0,
    "frame_ticks": 0,
    "spawn_ticks": 0,
    # ticks per frame
    "idle_ticks": 5,
    "walk_ticks": 4,
    "run_ticks": 4,
    "strike_ticks": None,
    "shoot_ticks": 5,
    "death_ticks": 4,
    # action at what frame
    "strike_frame": None,
    "shoot_frame": 7,
    "death_frame": 8,
    # track state for frame  reset
    "current_state": "walk",
    "last_state": "walk",

    # sprites
    "spawn_sprites": None,
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
    # offsets
    "shoot_offset_x": (21 * SKULL_COLLECTOR_SIZE),
    "shoot_offset_y": (-6 * SKULL_COLLECTOR_SIZE),
}
