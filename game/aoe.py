from __future__ import annotations

from .point import Point


class AOE(Point):
    radius: int
    damage: int
    remaining: int = 300
    color: tuple[int, int, int] = (0, 0, 0)

    def contains(self, other):
        return self.sqdist(other) <= self.radius**2

    def tick(self):
        self.remaining -= 1

    def is_over(self):
        return self.remaining <= 0


class Poison(AOE):
    color: tuple[int, int, int] = (0, 255, 0)


class Fire(AOE):
    color: tuple[int, int, int] = (255, 0, 0)


class Ice(AOE):
    color: tuple[int, int, int] = (0, 0, 255)
