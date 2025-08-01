import pygame

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()  # rect is size and position(s)
        self.settings = game.settings

        self.image = pygame.image.load('Alien Invadors/images/ship.png')
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 50

    def draw_ship(self):
        # blit (place) what and where on self.screen
        self.screen.blit(self.image, self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.rect.left > self.screen_rect.left:
                self.rect.x -= self.settings.ship_speed
        if keys[pygame.K_RIGHT]:
            if self.rect.right < self.screen_rect.right:
                self.rect.x += self.settings.ship_speed
        
   
   