from __future__ import annotations

import pygame

from game.game import Game
from game.utils.translator import convert_pixel_to_coordinates


class GameRenderer:
    @staticmethod
    def run(game: Game):
        game.generate_random_enemy(50)

        # initializing imported module
        pygame.init()
        pygame.display.set_caption("AoE Inc.")
        clock = pygame.time.Clock()

        display = pygame.display.set_mode((400, 500))
        aoe_type = "fire"

        running = True
        while running:
            display.fill((128, 128, 128))

            dt = clock.tick(60)

            game.tick(dt)

            for aoe in game.AOE[::-1]:
                is_over = aoe.update()
                if is_over:
                    game.AOE.remove(aoe)
                    continue
                aoe.draw(display)

                # pygame.draw.circle(display, aoe.color, convert_coordinates_to_pixels(aoe), aoe.radius)

            # pygame.draw.circle(display, (255, 0, 0), convert_coordinates_to_pixels(game.me), game.me.radius)

            # for enemy in game.enemies:
            #     pygame.draw.circle(display, (0, 0, 0), convert_coordinates_to_pixels(enemy), enemy.radius)

            # Check for event if user has pushed
            # any event in queue
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_click, y_click = pygame.mouse.get_pos()
                    x, y = convert_pixel_to_coordinates(x_click, y_click)
                    game.place(aoe_type, x, y)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        print("fire")
                        aoe_type = "fire"
                    if event.key == pygame.K_2:
                        print("ice")
                        aoe_type = "ice"
                    if event.key == pygame.K_3:
                        print("flashbang")
                        aoe_type = "flashbang"

                # if event is of type quit then set
                # running bool to false
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
