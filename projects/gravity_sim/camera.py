import pygame
from pygame import Vector2


class Camera:
    def __init__(self, sim):
        self.sim = sim
        self.camera_pos = Vector2(600, 400)
        self.camera_zoom = 1
        self.camera_speed = 10

        self.pressed = False
        self.last_pos = None

    def mouse_move(self):

        mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())

        if self.pressed:
            distance = mouse_pos - self.last_pos
            self.camera_pos = distance

    def mouse(self, event, pressed):
        self.pressed = pressed
        mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
        if event.button == 1:
            if self.pressed:
                self.last_pos = mouse_pos - self.camera_pos

    def mouse_scroll(self, event):
        if event.y > 0:
            self.camera_zoom *= 1.1
        elif event.y < 0:
            self.camera_zoom /= 1.1
