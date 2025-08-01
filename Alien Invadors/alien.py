import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load("Alien Invadors/images/alien.png")
        self.image = pygame.transform.scale(self.image, (80, 60))

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def check_edges(self):

        screen_rect = self.screen.get_rect()

        if self.rect.x <= (screen_rect.left + 10) or (self.rect.x + self.rect.width) >= (screen_rect.right - 10):
            return False  # if touching edges
        return True

    def update(self):
        self.rect.x += self.settings.alien_speed * self.settings.alien_direction
