from __future__ import annotations

from .point import Point


class Entity(Point):
    hp: int
    damage: int
    radius: int
    speed: int = 20

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
