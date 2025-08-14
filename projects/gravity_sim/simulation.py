import math
import pygame
from planet import Planet
from pygame import Vector2, Vector3
from settings import Settings
from camera import Camera


class Simulation:

    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Gravity")
        WIDTH, HEIGHT = 1200, 800
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        self.camera = Camera(self)

        self.camera.camera_zoom = 0.1

        planet_mass = 10**3  # max is 10**13

        self.bodies = []
        self.bodies.append(Planet(self, Vector2(0, 0), Vector2(0, 0), 10**8, 500, (230, 0, 0)))
        self.bodies.append(Planet(self, Vector2(1000, 0), Vector2(0, -7071), planet_mass, 20, (0, 255, 0)))
        self.bodies.append(Planet(self, Vector2(3000, 0), Vector2(0, -4082), planet_mass, 20, (0, 0, 255)))
        self.bodies.append(Planet(self, Vector2(5000, 0), Vector2(0, -3162), planet_mass, 20, (255, 255, 0)))
        # self.bodies.append(Planet(self, Vector2(-10000, 0), Vector2(0, 1362), 10**8, 50, (230, 230, 230)))

        # self.bodies.append(Planet(self, Vector2(10000, 0), 10**7, Vector2(0, -2236), (255, 255, 255)))

    def run_game(self):

        while True:

            self._check_events()

            self.camera.mouse_move()

            self._update_physics()

            self._update_screen()

    def _update_physics(self):

        to_delete = set()

        # update velocity
        for body in self.bodies.copy():
            for other in self.bodies.copy():

                if other != body:

                    distance = (body.pos - other.pos).length()

                    if distance > body.radius:
                        body.calc_vel(other)
                        continue

                    if not any(body in pair or other in pair for pair in to_delete):  # ? what

                        if body.mass >= other.mass:
                            to_delete.add((other, body))  # being deleted and the one deleting
                        else:
                            to_delete.add((body, other))

        # update position
        for body in self.bodies:
            body.calc_pos()

        # delete colided bodies
        for body in to_delete:
            body[1].mass += body[0].mass
            # body[1].vel += body[0].mass/body[1].mass * body[0].vel
            # body[1].radius = math.log(body[1].mass, 10)*5

            self.bodies.remove(body[0])

    def _update_screen(self):

        self.clock.tick(60)

        self.screen.fill("black")

        for body in self.bodies:
            body.draw()

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEWHEEL:
                self.camera.mouse_scroll(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.camera.mouse(event, True)
            if event.type == pygame.MOUSEBUTTONUP:
                self.camera.mouse(event, False)
                pass


if __name__ == "__main__":
    sim = Simulation()
    sim.run_game()
