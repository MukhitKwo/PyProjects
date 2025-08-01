import math
import pygame
from pygame.sprite import Sprite
from bullet import Bullet


class Sat(Sprite):
    def __init__(self, game):
        super().__init__()  # init the Sprite
        self.screen = game.screen
        self.settings = game.settings

        self.original_image = pygame.image.load("Debri Obliterator/imgs/sat.png")
        self.original_image = pygame.transform.scale(self.original_image, self.settings.sat_size)
        self.image = self.original_image.copy()

        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center

        # for bullet
        self.fire_offset = pygame.math.Vector2(0, -self.rect.height // 2 + 5)
        self.angle = 0

        # for smooth movement
        self.inertia = pygame.math.Vector2(0, 0)

    def update(self):
        self._handle_movement()
        self._point_at_mouse()

    def _handle_movement(self):

        screen_x, screen_y = self.screen.get_rect().size
        screen_x -= 20
        screen_y -= 20

        moved = pygame.math.Vector2(0, 0)

        key_pressed = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 10:
            self.rect.y -= self.settings.sat_speed
            key_pressed = True
            moved.y = -1
        if keys[pygame.K_s] and self.rect.bottom < screen_y:
            self.rect.y += self.settings.sat_speed
            key_pressed = True
            moved.y = 1
        if keys[pygame.K_a] and self.rect.left > 10:
            self.rect.x -= self.settings.sat_speed
            key_pressed = True
            moved.x = -1
        if keys[pygame.K_d] and self.rect.right < screen_x:
            self.rect.x += self.settings.sat_speed
            key_pressed = True
            moved.x = 1

        # print(moved, moved.x, moved.y)
        self._inertia(key_pressed, moved)

    def _inertia(self, key_pressed, moved):
        if not key_pressed:

            fr = self.settings.friction

            if self.inertia.x != 0:
                self.inertia.x -= fr * (1 if self.inertia.x > 0 else -1)
                if -fr < self.inertia.x < fr:
                    self.inertia.x = 0
                self.rect.x += self.inertia.x * self.settings.sat_speed

            if self.inertia.y != 0:
                self.inertia.y -= fr * (1 if self.inertia.y > 0 else -1)
                if -fr < self.inertia.y < fr:
                    self.inertia.y = 0
                self.rect.y += self.inertia.y * self.settings.sat_speed

        else:
            self.inertia = moved

    def _point_at_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        sat_x, sat_y = self.rect.center

        dx = mouse_x - sat_x
        dy = mouse_y - sat_y

        angle_rad = math.atan2(-dy, dx)
        angle_deg = math.degrees(angle_rad) - 90
        self.angle = (angle_deg + 360) % 360  # Normalise angle to 0–360

        # Rotate image and update its rect to keep the same center
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw_sat(self):
        self.screen.blit(self.image, self.rect)

    def get_bullet_spawn_point(self):
        # Rotate the offset vector to get the spawn point relative to rotation
        rotated_offset = self.fire_offset.rotate(-self.angle)  # ? creates a cicle around the sat and
        # ? adds the rotated offect to sat's center position
        return pygame.math.Vector2(self.rect.center) + rotated_offset

    def get_direction_vector(self):
        # Get unit direction vector based on satellite rotation
        angle_rad = math.radians(self.angle)
        dx = math.cos(angle_rad + math.pi / 2)  # ? angle will shot to side, math.pi/2 is to correct direction
        dy = -math.sin(angle_rad + math.pi / 2)
        return pygame.math.Vector2(dx, dy)
