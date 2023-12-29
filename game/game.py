from __future__ import annotations

import math
import random

from game.entities.aoe import AOE
from game.entities.aoe import Fire
from game.entities.aoe import Flashbang
from game.entities.aoe import Ice
from game.entities.entity import Enemy
from game.entities.entity import Entity
from game.entities.entity import Hero


class Game:
    def __init__(self):
        self.me = Hero(x=0, y=0, hp=100, damage=1)
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

    def tick(self, dt: int) -> bool:
        hit = self.move_enemies(dt)
        self.apply_aoe(dt)
        return hit

    def move_enemies(self, dt: int):
        hit = False
        for enemy in self.enemies:
            dist = self.me.dist(enemy)
            travel_dist = enemy.speed * dt

            if dist < travel_dist + self.me.radius:
                self.enemies.remove(enemy)
                self.generate_random_enemy(1)
                hit = True
                continue

            dx = -enemy.x * travel_dist / dist
            dy = -enemy.y * travel_dist / dist

            enemy.move(int(dx), int(dy))
        return hit

    def apply_aoe(self, dt: int):
        for aoe in self.AOE[::-1]:
            is_over = aoe.update(dt)
            if is_over:
                self.AOE.remove(aoe)
                continue

            for enemy in self.enemies[::-1]:
                if aoe.contains(enemy):
                    self.enemies.remove(enemy)
                    self.generate_random_enemy(1)

    def generate_random_enemy(self, n=1):
        for _ in range(n):
            theta = random.random() * 2 * math.pi
            radius = random.randint(10000, 20000)
            x = int(radius * math.cos(theta))
            y = int(radius * math.sin(theta))
            self.enemies.append(Enemy(x=x, y=y, hp=100, damage=1, speed=10))
