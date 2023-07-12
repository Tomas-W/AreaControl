import os
import sys

from settings.general_settings import PLAYER_HITBOX_SIZE
from sprites.player_sprites import PLAYER_SPRITE, PLAYER_SHOOT_SPRITE

base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

PLAYER_SIZE = 0.4

PLAYER = {
    # main
    "start_position": (1750, 1450),
    "size": PLAYER_SIZE,
    "hitbox_size": PLAYER_HITBOX_SIZE,
    "name": "player",

    # attributes
    "health": 1000,
    "max_health": 1000,
    "speed": 8,

    # states
    "shoot": False,
    "bomb": False,
    "is_invincible": False,

    "wave_level": 0,

    # state durations
    "shoot_cooldown": 15,
    "muzzle_flash_cooldown": 8,
    "bomb_cooldown": 120,

    # items
    "skull_level": 0,
    "energy_level": 0,
    "coin_level": 110,
    "total_bombs": 33,
    "total_portals": 0,
    "total_health_potions": 22,
    "health_potion_boost": 250,  # linked with health_potion settings

    # kill points
    "skull_collector_points": 65,
    "rusher_points": 50,
    "bat_points": 30,
    "fish_points": 35,

    # buy menu
    "buy_multiplier": 1.1,
    "buy_multiplier_addition": 0.25,
    "bullet_upgrade_cost": 4,
    "bomb_upgrade_cost": 5,
    "buy_bomb_cost": 2,
    "buy_portal_cost": 3,

    # portal
    "new_location": None,
    "teleport_location": None,
    "left_portal": None,
    "right_portal": None,
    "new_location_tick": 120,
    # invincibility attributes
    "invincibility_ticks": 240,

    # sprites
    "sprite": PLAYER_SPRITE,
    "shoot_sprite": PLAYER_SHOOT_SPRITE,
    "hitbox": ((20 * PLAYER_SIZE), (20 * PLAYER_SIZE),
               (180 * PLAYER_SIZE), (180 * PLAYER_SIZE)),
    "sprite_width": 220,
    "sprite_height": 220,

    # sounds
    "lose_health_sound_path": os.path.join(base_dir, "sounds/player_hit_sound.mp3"),
    "gain_health_sound_path": os.path.join(base_dir, "sounds/player_add_health_sound.mp3"),
    "death_sound_path": os.path.join(base_dir, "sounds/player_death_sound.mp3"),
}
