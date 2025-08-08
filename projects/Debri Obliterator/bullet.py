import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.sat.rect.midtop

        # Get the bullet's spawn position and direction from the satellite
        self.pos = game.sat.get_bullet_spawn_point()
        self.direction = game.sat.get_direction_vector()

    def update(self):
        # Move bullet in the direction the satellite was facing
        self.pos += self.direction * self.settings.bullet_speed  # * pos will be [x,y]
        self.rect.center = self.pos

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
