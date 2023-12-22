from __future__ import annotations

import pygame

from game.geometry.point import Point
from game.utils.translator import convert_coordinates_to_pixels
from game.utils.translator import scale_to_pixel


class AOE(Point):
    radius: int
    damage: int
    remaining: int = 300
    color: tuple[int, int, int] = (0, 0, 0)

    def contains(self, other):
        return self.sqdist(other) <= self.radius**2

    def update(self):
        self.remaining -= 1
        return self.remaining <= 0

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, convert_coordinates_to_pixels(self.x, self.y), scale_to_pixel(self.radius))


class Poison(AOE):
    color: tuple[int, int, int] = (0, 255, 0)


class Fire(AOE):
    color: tuple[int, int, int] = (255, 0, 0)


class Ice(AOE):
    color: tuple[int, int, int] = (0, 0, 255)


class Flashbang(AOE):
    radius: int = 1
    damage: int = 0
    remaining: int = 5
    color: tuple[int, int, int] = (255, 255, 255)
    max_radius: int = 5000
    step_radius: int = 1000

    def update(self):
        self.radius += self.step_radius
        return self.radius >= self.max_radius

    def draw(self, surf):
        r = scale_to_pixel(self.radius)
        r_max = scale_to_pixel(self.max_radius)

        surface1 = pygame.Surface((r_max * 2, r_max * 2))
        surface1.set_colorkey((0, 0, 0))
        surface1.set_alpha(255 - 0.1 * r**2)
        pygame.draw.circle(surface1, self.color, (r_max, r_max), r)

        x1, y1 = convert_coordinates_to_pixels(self.x - self.max_radius, self.y - self.max_radius)
        x2, y2 = convert_coordinates_to_pixels(self.x + self.max_radius, self.y + self.max_radius)
        surf.blit(surface1, (x1, y1, x2, y2))
