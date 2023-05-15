import os
import sys

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

DISPLAY = {
    # buttons
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

    # offsets
    "health_bar_x_offset": 750,
    "health_bar_y_offset": 425,
    "health_bar_height": 25,

    "wave_text_x_offset": 250,
    "wave_text_y_offset": 330,

    "buy_menu_x_offset": 250,
    "buy_menu_y_offset": -125,

    "countdown_x_offset": 60,
    "countdown_y_offset": 30,
}