from __future__ import annotations

import math
import random

from game.entities.aoe import AOE
from game.entities.aoe import Fire
from game.entities.aoe import Flashbang
from game.entities.aoe import Ice
from game.entities.entity import Entity


class Game:
    def __init__(self):
        self.me = Entity(x=0, y=0, hp=100, damage=1, radius=10)
        self.AOE: list[AOE] = []
        self.enemies: list[Entity] = []

    def place(self, type: str, x: int, y: int):
        match type:
            case "fire":
                self.AOE.append(Fire(x=x, y=y, damage=10, radius=3000))
            case "flashbang":
                self.AOE.append(Flashbang(x=x, y=y, damage=0, radius=1, max_radius=5000, step_radius=1000))
            case "ice":
                self.AOE.append(Ice(x=x, y=y, damage=0, radius=3000))

    def tick(self, dt: int):
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
            theta = random.random() * 2 * math.pi
            radius = random.randint(10000, 20000)
            x = int(radius * math.cos(theta))
            y = int(radius * math.sin(theta))
            self.enemies.append(Entity(x=x, y=y, hp=100, damage=1, radius=10, speed=10))
