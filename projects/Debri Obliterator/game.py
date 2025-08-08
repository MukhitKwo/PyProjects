import pygame
import sys

from settings import Settings
from sat import Sat
from bullet import Bullet


class Main:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Debri Obliterator")
        self.clock = pygame.Clock()

        self.settings = Settings()

        self.sat = Sat(self)
        self.bullets = pygame.sprite.Group()

    def _run_game(self):
        while True:
            self._events()

            self.sat.update()
            self.bullets.update()

            self._update_screen()

    def _update_screen(self):
        self.clock.tick(60)

        self.screen.fill((30, 30, 30))

        self.sat.draw_sat()
        self._draw_bullets()

        pygame.display.flip()

    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass
                    # self.fire_bullet()

# ================================================

    def fire_bullet(self):
        bullet = Bullet(game)
        self.bullets.add(bullet)

    def _draw_bullets(self):

        screen_x = self.screen.get_rect().width
        screen_y = self.screen.get_rect().height

        for bullet in self.bullets.copy():
            if (bullet.rect.x < screen_x and bullet.rect.x > 0) and (bullet.rect.y < screen_y and bullet.rect.y > 0):
                bullet.draw_bullet()
            else:
                self.bullets.remove(bullet)


if __name__ == "__main__":
    game = Main()
    game._run_game()
