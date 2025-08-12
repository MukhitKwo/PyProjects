import math
import pygame
from planet import Planet
from pygame import Vector2, Vector3


class Simulation:

    def __init__(self):
        pygame.init()

        WIDTH, HEIGHT = 1200, 800
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Gravity")
        self.clock = pygame.time.Clock()

        self.G = 500
        planet_mass = 10**5 # max is 10**13

        self.bodies = []
        self.bodies.append(Planet(self, Vector2(400, 400), planet_mass,  Vector2(0, 20), (255, 0, 0)))
        self.bodies.append(Planet(self, Vector2(800, 400), planet_mass + 1,  Vector2(0, -20), (0, 0, 255)))
        # self.bodies.append(Planet(self, Vector2(600, 200), planet_mass,  Vector2(100, 0), (0, 255, 0)))

    def run_game(self):

        while True:

            self._check_event()

            self._update_physics()

            self._update_screen()

    def _update_physics(self):

        to_remove = set()

        for body in self.bodies.copy():
            for other in self.bodies.copy():

                if other != body:

                    body.calc_orbit(other)

                    r_vec = body.pos - other.pos
                    distance = r_vec.length()

                    if distance < other.radius:

                        if body.mass >= other.mass:
                            if body not in to_remove:
                                to_remove.add(other)
                                continue
                        else:
                            if other not in to_remove:
                                to_remove.add(body)
                                break


        for body in to_remove:
            self.bodies.remove(body)

    def _update_screen(self):

        self.clock.tick(60)

        self.screen.fill("black")

        for body in self.bodies:
            body.draw()

        pygame.display.flip()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_r:
                    pass  # restart
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # self.planet.pos = list(event.pos)
                    pass


if __name__ == "__main__":
    sim = Simulation()
    sim.run_game()
