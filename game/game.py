from __future__ import annotations

import random

from .aoe import AOE
from .aoe import Fire
from .aoe import Ice
from .aoe import Poison
from .entity import Entity


class Game:
    def __init__(self):
        self.me = Entity(x=0, y=0, hp=100, damage=1, radius=10)
        self.AOE: list[AOE] = []
        self.enemies: list[Entity] = []

    def place(self, type: str, x: int, y: int):
        match type:
            case "fire":
                self.AOE.append(Fire(x=x, y=y, damage=10, radius=30))
            case "ice":
                self.AOE.append(Ice(x=x, y=y, damage=5, radius=50))
            case "poison":
                self.AOE.append(Poison(x=x, y=y, damage=1, radius=100))

    def tick(self, dt):
        for enemy in self.enemies[::-1]:
            dist = self.me.dist(enemy)
            travel_dist = enemy.speed * dt

            if dist < travel_dist:
                self.enemies.remove(enemy)
                self.generate_random_enemy(1)
                continue

            dx = -enemy.x * travel_dist / dist
            dy = -enemy.y * travel_dist / dist

            enemy.move(int(dx), int(dy))

    def generate_random_enemy(self, n=1):
        for _ in range(n):
            x = random.randint(-10000, 10000)
            self.enemies.append(Entity(x=x, y=20000, hp=100, damage=1, radius=10, speed=10))
