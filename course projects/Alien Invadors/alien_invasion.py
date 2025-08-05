from pickle import TRUE
import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.Clock()

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):

        while True:
            self.clock.tick(60)

            self._check_events()

            self.ship.update()
            self.bullets.update()
            self._update_aliens()

            self._update_screen()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        self.ship.draw_ship()
        self.draw_bullets()
        self.aliens.draw(self.screen)

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self.fire_bullet()

    # ==========================================

    def draw_bullets(self):

        for bullet in self.bullets.copy():
            if bullet.rect.bottom < self.screen.get_rect().top:
                self.bullets.remove(bullet)
                continue
            bullet.draw_bullet()

    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _create_fleet(self):

        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien_width, alien_height = alien.rect.size

        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_cols = available_space_x // (2 * alien_width)

        available_space_y = self.settings.screen_height - (2 * alien_height) - 2 * self.ship.rect.height
        number_rows = available_space_y // (2 * alien_height)

        for row in range(number_rows):
            for col in range(number_cols):
                alien = Alien(self)
                alien.rect.x = alien_width + (2 * alien_width * col)
                alien.rect.y = alien_height + (2 * alien_height * row)
                self.aliens.add(alien)

    def _update_aliens(self):

        for alien in self.aliens:
            if not alien.check_edges():
                self.settings.alien_direction *= -1

                for a in self.aliens.sprites():
                    a.rect.y += self.settings.alien_drop_speed

                break

        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit")

        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()
