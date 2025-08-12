import math
import pygame
from planet import Planet
from pygame import Vector2, Vector3
from settings import Settings


class Simulation:

    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Gravity")
        WIDTH, HEIGHT = 1200, 800
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        planet_mass = 10**5  # max is 10**13

        self.bodies = []
        self.bodies.append(Planet(self, Vector2(0, 0), 10**8, Vector2(0, 0), (0, 0, 255)))
        self.bodies.append(Planet(self, Vector2(1000, 0), planet_mass, Vector2(0, -7071), (0, 255, 0)))
        self.bodies.append(Planet(self, Vector2(2000, 0), planet_mass, Vector2(0, -5000), (255, 0, 0)))
        self.bodies.append(Planet(self, Vector2(5000, 0), planet_mass, Vector2(0, -3162), (255, 255, 0)))

        # self.bodies.append(Planet(self, Vector2(10000, 0), 10**7, Vector2(0, -2236), (255, 255, 255)))

    def run_game(self):

        while True:

            self._check_event()
            self._screen_movement()

            self._update_physics()

            self._update_screen()

    def _update_physics(self):

        to_delete = set()

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

        for body in to_delete:

            body[1].mass += body[0].mass
            body[1].vel += body[0]/body[1] * body[0].vel
            body[1].radius = math.log(body[1].mass, 10)*5

            self.bodies.remove(body[0])
            print("yum")

        for body in self.bodies:
            body.calc_pos()

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
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    self.settings.camera_zoom *= 1.1
                elif event.y < 0:
                    self.settings.camera_zoom /= 1.1

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # self.planet.pos = list(event.pos)
                    pass

    def _screen_movement(self):
        keys = pygame.key.get_pressed()

        mouse_buttons = pygame.mouse.get_pressed()

        if keys[pygame.K_w]:
            self.settings.camera_pos += Vector2(0, self.settings.camera_speed)
        if keys[pygame.K_s]:
            self.settings.camera_pos += Vector2(0, -self.settings.camera_speed)
        if keys[pygame.K_a]:
            self.settings.camera_pos += Vector2(self.settings.camera_speed, 0)
        if keys[pygame.K_d]:
            self.settings.camera_pos += Vector2(-self.settings.camera_speed, 0)


if __name__ == "__main__":
    sim = Simulation()
    sim.run_game()
