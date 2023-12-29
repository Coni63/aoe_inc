from __future__ import annotations

import pygame

from game.geometry.point import Point
from game.utils.translator import convert_coordinates_to_pixels
from game.utils.translator import scale_to_pixel


class Entity(Point):
    hp: int
    damage: int
    radius: int = 1000
    speed: int = 20
    color: tuple[int, int, int] = (0, 0, 0)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, display):
        r = scale_to_pixel(self.radius)
        pos = convert_coordinates_to_pixels(self.x, self.y)
        pygame.draw.circle(display, self.color, pos, r)


class Hero(Entity):
    color: tuple[int, int, int] = (255, 0, 0)
    radius: int = 1000


class Enemy(Entity):
    color: tuple[int, int, int] = (0, 255, 255)
    radius: int = 200
