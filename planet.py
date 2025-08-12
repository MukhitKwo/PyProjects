import math
import pygame
from pygame import Vector2


class Planet:
    def __init__(self, sim, pos, mass, vel, color, radius=None):

        self.sim = sim

        self.pos = pos
        self.mass = mass
        self.vel = vel

        self.color = color
        self.radius = radius if radius is not None else math.log(mass, 10)*10

        self.dt = 1/60

    def calc_orbit(self, body):

        # get x and y values from ball to center
        r_vec = self.pos - body.pos

        # get distance ball to center (hypotenuse)
        distance = r_vec.length()

        # normalize vector (0-1)
        direction = r_vec.normalize()

        # get acceleration for x and y
        a = -self.sim.G * body.mass / distance**2 * direction

        self.vel += a * self.dt
        self.pos += self.vel * self.dt

    def draw(self):
        pygame.draw.circle(self.sim.screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)
