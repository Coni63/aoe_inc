from __future__ import annotations

from game.point import Point


def convert_coordinates_to_pixels(element: Point):
    """
    Converts coordinates to pixels.
    """
    return element.x // 100 + 200, element.y // 100 + 250


def convert_pixel_to_coordinates(pixel):
    """
    Converts pixels to coordinates.
    """
    return (pixel[0] - 200) * 100, (pixel[1] - 250) * 100
