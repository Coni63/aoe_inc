from __future__ import annotations

from game.geometry.point import Point


class Entity(Point):
    hp: int
    damage: int
    radius: int
    speed: int = 20

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
