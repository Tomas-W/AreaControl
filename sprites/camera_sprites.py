import os
import sys

import pygame


base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


# Characters
SKULL_COLLECTOR_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/skull_collector.png")).convert_alpha()

RUSHER_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/rusher.png")).convert_alpha()

# Creepers
BAT_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/bat.png")).convert_alpha()

FISH_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/fish.png")).convert_alpha()


# PickUps
SKULL_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/skull.png")).convert_alpha()

ENERGY_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/energy.png")).convert_alpha()

COIN_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/coin.png")).convert_alpha()

# Keys
KEY_RED_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/key_red.png")).convert_alpha()
KEY_BLUE_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/key_blue.png")).convert_alpha()
KEY_GREEN_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/key_green.png")).convert_alpha()
KEY_YELLOW_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/key_yellow.png")).convert_alpha()


# Items
BOMB_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/bomb.png")).convert_alpha()

PORTAL_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/portal.png")).convert_alpha()

HEALTH_POTION_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/health_potion.png")).convert_alpha()

# Button images
BUTTON_1_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_1.png")).convert_alpha()
BUTTON_2_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_2.png")).convert_alpha()
BUTTON_3_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_3.png")).convert_alpha()
BUTTON_4_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_4.png")).convert_alpha()

BUTTON_Q_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_q.png")).convert_alpha()
BUTTON_W_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_w.png")).convert_alpha()
BUTTON_E_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_e.png")).convert_alpha()
BUTTON_A_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_a.png")).convert_alpha()
BUTTON_S_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_s.png")).convert_alpha()
BUTTON_D_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/btn_d.png")).convert_alpha()

MOUSE_L_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/mouse_l.png")).convert_alpha()
MOUSE_R_CAMERA_IMAGE = pygame.image.load(
            os.path.join(base_dir, "./images/camera/mouse_r.png")).convert_alpha()

