from pygame import Vector2
import math


class Settings:
    def __init__(self):
        self.camera_pos = Vector2(600, 400)
        self.camera_zoom = 1
        self.camera_speed = 10
        self.G = 500

    def _orbit_vel(self, mass, distance):
        vel = math.sqrt(self.G * mass/distance)
        print(vel)


if __name__ == "__main__":
    settings = Settings()
    settings._orbit_vel(10**8, 4900)
