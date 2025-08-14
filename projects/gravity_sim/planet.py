import math
import pygame
from pygame import Vector2


class Planet:
    def __init__(self, sim, pos, vel, mass,  radius, color):

        self.sim = sim

        self.pos = pos
        self.mass = mass
        self.vel = vel

        self.color = color
        self.radius = radius if radius is not None else math.log(mass, 10) * 5

        self.dt = 1/60

    def calc_vel(self, body):

        # get x and y values from ball to center
        r_vec = self.pos - body.pos

        # get distance ball to center (hypotenuse)
        distance = r_vec.length()

        # normalize vector (0-1)
        direction = r_vec.normalize()

        # get acceleration for x and y
        a = -self.sim.settings.G * body.mass / distance**2 * direction

        self.vel += a * self.dt

    def calc_pos(self):
        self.pos += self.vel * self.dt

    def draw(self):
        cx = self.sim.camera.camera_pos.x
        cy = self.sim.camera.camera_pos.y
        cz = self.sim.camera.camera_zoom

        x = (int(self.pos[0]) * cz + cx)
        y = (int(self.pos[1]) * cz + cy)

        pygame.draw.circle(self.sim.screen, self.color, (x, y), self.radius * cz)

    def __repr__(self):
        return f"Planet(mass={self.mass}, pos={tuple(round(p, 1) for p in self.pos)})"
