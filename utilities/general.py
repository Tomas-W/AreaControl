import colorsys
import csv

import numpy as np
import pygame
import soundfile as sf


HIGHSCORES_PATH = "./highscores.csv"


def get_sprites(sheet, number_sprites, width, height, scale, color):
    """
    Returns a list of individual sprites taken from the given sheet.

    :param sheet: Image file containing the sprites (png).
    :param number_sprites: Number of sprites to obtain (int).
    :param width: Sprite width in pixels (int).
    :param height: Sprite height in pixels (int).
    :param scale: Magnification in comparison with the original (int).
    :param color: Pixel color of background to remove (pygame wants this)(str rgb).

    :return: List of sprite images.
    """
    sprites = []
    for i in range(0, number_sprites):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), ((i * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        sprites.append(image)

    return sprites


def get_player_score(player):
    return (player.kill_points['skull_collector'] * player.kills['skull_collector']) + (
                player.kill_points['rusher'] * player.kills['rusher']) + (
                player.kill_points['bat'] * player.kills['bat']) + (
                player.kill_points['fish'] * player.kills['fish'])


def get_leaderboard_scores():
    scores = []
    with open(HIGHSCORES_PATH, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        scores = list(reader)

    # Sort scores descending
    scores.sort(key=lambda x: int(x[1]), reverse=True)

    top_scores = scores[:10]
    top_scores = [(entry[0], int(entry[1])) for entry in top_scores]

    return top_scores


def save_player_score(player):
    scores = []
    with open(HIGHSCORES_PATH, "r") as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip the header row
        scores = list(reader)

    score = get_player_score(player)
    scores.append([player.highscore_name, str(score)])

    # Sort in descending order
    scores.sort(key=lambda x: int(x[1]), reverse=True)

    # Save the top 10
    with open(HIGHSCORES_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(scores[:10])


def shorten_audio(source_file, destination_file, desired_duration):
    # Read the audio file
    audio, sample_rate = sf.read(source_file)

    # Calculate the desired number of samples
    desired_samples = int(desired_duration * sample_rate / 1000)

    # Shorten the audio by truncating or zero-padding
    if len(audio) > desired_samples:
        shortened_audio = audio[:desired_samples]
    else:
        padding = np.zeros((desired_samples - len(audio), audio.shape[1]), dtype=audio.dtype)
        shortened_audio = np.concatenate((audio, padding))

    # Write the shortened audio to a new file
    sf.write(destination_file, shortened_audio, sample_rate)


def get_health_color_list():
    """
    Returns a list of 101 colors going from red to green.
    :return: color_list (list tuple).
    """
    green_hue = 120  # Green hue value in HSL color model
    red_hue = 0  # Red hue value in HSL color model

    color_list = [
        colorsys.hls_to_rgb(
            (red_hue + ((i / 99) * (green_hue - red_hue))) / 360,  # Hue
            0.5,  # Saturation
            1  # Lightness
        )
        for i in range(101)
    ]
    color_list = [
        (
            int(color[0] * 255),  # Convert RGB values to 0-255 range
            int(color[1] * 255),
            int(color[2] * 255)
        )
        for color in color_list
    ]

    return color_list
