from __future__ import annotations

import math
import random

import pygame

from game.game import Game
from game.utils.translator import convert_coordinates_to_pixels
from game.utils.translator import convert_pixel_to_coordinates
from rendering.prefabs.sparks import Spark


class GameRenderer:
    @staticmethod
    def run(game: Game):
        sparks = []
        game.generate_random_enemy(10)

        pygame.init()
        pygame.display.set_caption("AoE Inc.")
        clock = pygame.time.Clock()

        display = pygame.display.set_mode((400, 500))
        aoe_type = "fire"

        running = True
        while running:
            display.fill((128, 128, 128))

            dt = clock.tick(60)

            print(1000 / dt)

            hit = game.tick(dt)

            for aoe in game.AOE:
                aoe.draw(display)

            game.me.draw(display)

            for enemy in game.enemies:
                enemy.draw(display)

            if hit and len(sparks) < 100:
                x, y = convert_coordinates_to_pixels(game.me.x, game.me.y)
                sparks += [
                    Spark([x, y], random.random() * math.pi * 2, random.randint(3, 6), (255, 255, 255), 2)
                    for _ in range(20)
                ]

            for i, spark in sorted(enumerate(sparks), reverse=True):
                spark.move(1)
                spark.draw(display)
                if not spark.alive:
                    sparks.pop(i)

            # Check for event if user has pushed
            # any event in queue
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_click, y_click = pygame.mouse.get_pos()
                    x, y = convert_pixel_to_coordinates(x_click, y_click)
                    game.place(aoe_type, x, y)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        aoe_type = "fire"
                    if event.key == pygame.K_2:
                        aoe_type = "ice"
                    if event.key == pygame.K_3:
                        aoe_type = "flashbang"

                # if event is of type quit then set
                # running bool to false
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
