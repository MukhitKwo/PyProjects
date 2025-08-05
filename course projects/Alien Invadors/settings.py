class Settings:
    def __init__(self):
        # SCREEN
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30, 30, 30)

        # SHIP
        self.ship_speed = 7

        # BULLET
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 5

        # ALIENS
        self.alien_speed = 20.0
        self.alien_drop_speed = 10
        self.alien_direction = 1
