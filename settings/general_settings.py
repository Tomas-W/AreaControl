import os
import sys

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

GENERAL = {
    # window
    "width": 1600,
    "height": 900,
    "half_width": 800,
    "half_height": 450,

    # main
    "title": "AreaControl",
    "FPS": 60,
    "origin": (0, 0),

    # level
    "background_path": os.path.join(base_dir, "./images/game/level_medium.png"),
    "menu_background_path": os.path.join(base_dir, "./images/game/menu_background.png"),

    # menus
    "play_btn_img": os.path.join(base_dir, "images/game/btn_play.png"),
    "settings_btn_img":  os.path.join(base_dir, "images/game/btn_settings.png"),
    "leaderboard_btn_img":  os.path.join(base_dir, "images/game/btn_leaderboard.png"),
    "credits_btn_img":  os.path.join(base_dir, "images/game/btn_credits.png"),
    "sounds_on_btn_img":  os.path.join(base_dir, "images/game/btn_sounds_on.png"),
    "sounds_off_btn_img":  os.path.join(base_dir, "images/game/btn_sounds_off.png"),
    "continue_btn_img":  os.path.join(base_dir, "images/game/btn_continue.png"),
    "restart_btn_img":  os.path.join(base_dir, "images/game/btn_restart.png"),
    "game_over_btn_img":  os.path.join(base_dir, "images/game/btn_game_over.png"),
    "main_menu_btn_img":  os.path.join(base_dir, "images/game/btn_main_menu.png"),

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

    "left_mouse_button": (1, 0, 0),
    "right_mouse_button": (0, 0, 1),

    # player attributes display
    "health_bar_x_offset": 750,
    "health_bar_y_offset": 425,
    "health_bar_height": 25,

    "wave_text_x_offset": 250,
    "wave_text_y_offset": 330,

    "buy_menu_x_offset": 250,
    "buy_menu_y_offset": -125,

    "countdown_x_offset": 60,
    "countdown_y_offset": 30,

    # colors
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),

    # credits
    "credits": ["pixelied.com", "craftpix.net", "pngtree.com", "vhv.rs", "freepik.com", "opengameart.org", "pngimages.in", "bdragon1727.itch.io", "ellr.itch.io", "digigrand.itch.io", "humblepixel.itch.io", "spoadr.itch.io", "gerald-burke.itch.io"]
}

# Characters
PLAYER_SIZE = 0.4
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
