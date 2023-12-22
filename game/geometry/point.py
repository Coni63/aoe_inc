from __future__ import annotations

from pydantic import BaseModel


class Point(BaseModel):
    x: int
    y: int

    def sqdist(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def dist(self, other):
        return self.sqdist(other) ** 0.5

    def to_tuple(self, dx, dy):
        return (self.x + dx, self.y + dy)
