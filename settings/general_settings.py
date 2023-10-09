import os
import sys

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

GENERAL = {
    # main
    "title": "AreaControl",
    "FPS": 60,
    "origin": (0, 0),

    # window
    "width": 1600,
    "height": 900,
    "half_width": 800,
    "half_height": 450,

    # level
    "background_path": os.path.join(base_dir, "images/game/level_medium.png"),
    "menu_background_path": os.path.join(base_dir, "./images/game/menu_background.png"),

    "left_x_min": 900,
    "left_x_max": 2100,
    "right_x_min": 2200,
    "right_x_max": 3400,
    "y_min": 800,
    "y_max": 2700,

    "level_left_x": 850,
    "level_right_x": 3450,
    "level_top_y": 750,
    "level_bottom_y": 2750,

    # buy menu
    "wave_pause": 240,
    "buy_tick": 240,

    # buttons
    "left_mouse_button": (1, 0, 0),
    "right_mouse_button": (0, 0, 1),

    # sounds
    "button_hover_sound_path": os.path.join(base_dir, "sounds/button_hover_sound.mp3"),
    "button_click_sound_path": os.path.join(base_dir, "sounds/button_click_sound.mp3"),
    "play_game_sound_path": os.path.join(base_dir, "sounds/play_game_sound.mp3"),
    "buy_sound_path": os.path.join(base_dir, "sounds/coin_pickup_sound.mp3"),

    # colors
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),

    # credits
    "credits": ["pixelied.com", "craftpix.net", "pngtree.com", "vhv.rs", "freepik.com", "opengameart.org", "pngimages.in", "freeiconspng.com", "creativekind.itch.io", "bdragon1727.itch.io", "ellr.itch.io", "digigrand.itch.io", "humblepixel.itch.io", "spoadr.itch.io", "gerald-burke.itch.io", "lornent.itch.io", "chierit.itch.io", "audiotrimmer.com", "cloudconvert.com", "freesound.org", "mixkit.co", "imgonline.com.ua", "pngfind.com"]
}

# Characters
PLAYER_SIZE = 0.4
PLAYER_HITBOX_SIZE = 1
PLAYER_SPRITE_WIDTH = 220
PLAYER_SPRITE_HEIGHT = 220

SKULL_COLLECTOR_SIZE = 2.5
SKULL_COLLECTOR_SPRITE_WIDTH = 56
SKULL_COLLECTOR_SPRITE_HEIGHT = 73

RUSHER_SIZE = 2.5
RUSHER_SPRITE_WIDTH = 51
RUSHER_SPRITE_HEIGHT = 53

GOLEM_SIZE = 3
GOLEM_SPRITE_WIDTH = 256
GOLEM_SPRITE_HEIGHT = 256

# Creepers
BAT_SIZE = 2
BAT_SPRITE_WIDTH = 28
BAT_SPRITE_HEIGHT = 28

FISH_SIZE = 0.7
FISH_SPRITE_WIDTH = 64
FISH_SPRITE_HEIGHT = 55

# Projectiles
FLAMING_SKULL_SIZE = 1.5
FLAMING_SKULL_SPRITE_WIDTH = 15
FLAMING_SKULL_SPRITE_HEIGHT = 25

BULLET_SIZE = 1
BULLET_SPRITE_WIDTH = 16
BULLET_SPRITE_HEIGHT = 16

BOMB_SIZE = 1
BOMB_SPRITE_WIDTH = 38
BOMB_SPRITE_HEIGHT = 38

# Interactives
ENERGY_SIZE = 0.5
ENERGY_SPRITE_WIDTH = 100
ENERGY_SPRITE_HEIGHT = 100

SKULL_SIZE = 0.4
SKULL_SPRITE_WIDTH = 75
SKULL_SPRITE_HEIGHT = 100

PORTAL_SIZE = 1
PORTAL_SPRITE_WIDTH = 75
PORTAL_SPRITE_HEIGHT = 85

COIN_SIZE = 0.15
COIN_SPRITE_WIDTH = 200
COIN_SPRITE_HEIGHT = 175

HEALTH_POTION_SIZE = 1
HEALTH_POTION_SPRITE_WIDTH = 50
HEALTH_POTION_SPRITE_HEIGHT = 60

DOOR_SIZE = 0.5
DOOR_SPRITE_WIDTH = 266
DOOR_SPRITE_HEIGHT = 335
