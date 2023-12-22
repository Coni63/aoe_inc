from __future__ import annotations

import pygame


class Flashbang:
    max_radius = 50
    step_radius = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1
        self.color = (255, 255, 255)

    def update(self):
        self.radius += Flashbang.step_radius
        self.color = (255, 255, 255)
        if self.radius >= Flashbang.max_radius:
            return None
        return self

    def draw(self, surf):
        surface1 = pygame.Surface((Flashbang.max_radius * 2, Flashbang.max_radius * 2))
        surface1.set_colorkey((0, 0, 0))
        surface1.set_alpha(255 - 0.1 * self.radius**2)
        pygame.draw.circle(surface1, self.color, (Flashbang.max_radius, Flashbang.max_radius), self.radius)
        surf.blit(
            surface1,
            (
                self.x - Flashbang.max_radius,
                self.y - Flashbang.max_radius,
                self.x + Flashbang.max_radius,
                self.y + Flashbang.max_radius,
            ),
        )


"""
Q = []
Q2 = []
while True:
    screen.fill((0, 0, 0))

    while len(Q) > 0:
        flash = Q.pop(0)
        flash.draw(screen)
        flash = flash.update()
        if flash is not None:
            Q2.append(flash)
    Q, Q2 = Q2, []

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print("jkqfhsg")
            Q.append(Flashbang(mx, my))
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    mainClock.tick(60)
"""
