from __future__ import annotations

SCALE = 100


def convert_coordinates_to_pixels(x, y):
    """
    Converts coordinates to pixels.
    """
    return x // SCALE + 200, y // SCALE + 250


def convert_pixel_to_coordinates(x, y):
    """
    Converts pixels to coordinates.
    """
    return (x - 200) * SCALE, (y - 250) * SCALE


def scale_to_game(x):
    return x * SCALE


def scale_to_pixel(x):
    return x // SCALE
