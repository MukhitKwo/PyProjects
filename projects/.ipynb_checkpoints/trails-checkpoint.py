import pygame
from sys import exit
import random
from typing import Dict, Tuple

window_x = 1280
window_y = 720

turn = 45
size = 3
trail_size = 700
points = 16

# trail_size = 100
# points = 20


def main():

    global trail_size, window_x, window_y

    pygame.init()

    info = pygame.display.Info()
    window_x = info.current_w
    window_y = info.current_h

    screen = pygame.display.set_mode((window_x, window_y))
    pygame.display.set_caption("Trails")
    clock = pygame.time.Clock()
    paused = False

    # x, y, d
    coordinates = []
    heat_map = {}

    for i in range(points):
        coordinates.append((random.randint(0, window_x), random.randint(
            0, window_y), random.randint(0, 360)))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_SPACE:
                    paused = not paused

                if event.key == pygame.K_UP:
                    coordinates.append((random.randint(0, window_x), random.randint(
                        0, window_y), random.randint(0, 360)))
                    print("Points", len(coordinates))
                if event.key == pygame.K_DOWN:
                    if (len(coordinates) > 0):
                        coordinates.pop(0)
                        print("Points", len(coordinates))

                if event.key == pygame.K_LEFT:
                    if trail_size > 50:
                        trail_size -= 50
                    print("Trail size", trail_size)
                if event.key == pygame.K_RIGHT:
                    trail_size += 50
                    print("Trail size", trail_size)

        if not paused:

            screen.fill("black")

            for i in range(len(coordinates)):
                x, y, d = coordinates[i]
                coordinates[i] = point_move(heat_map, x, y, d)

            for coord in list(heat_map.keys()):
                heat_map[coord] -= 1
                heat = heat_map[coord]
                if heat < 1:
                    del heat_map[coord]
                    continue

                # coord is the (x, y) tuple for this rect
                x, y = coord
                color = value_to_color(heat)
                # rect: (x, y, width, height)
                # pygame.draw.rect(screen, white, (x, y, step, step))
                pygame.draw.rect(screen, color, (x, y, size, size))

            # print(len(heat_map))

        pygame.display.flip()

        clock.tick(60)


def point_move(heat_map, x, y, d):

    direction = (d + random.randint(-turn, turn)) % 360

    if 0 <= direction < 45:
        y -= size
    elif 45 <= direction < 90:
        y -= size
        x += size
    elif 90 <= direction < 135:
        x += size
    elif 135 <= direction < 180:
        y += size
        x += size
    elif 180 <= direction < 225:
        y += size
    elif 225 <= direction < 270:
        y += size
        x -= size
    elif 270 <= direction < 315:
        x -= size
    elif 315 <= direction < 360:
        y -= size
        x -= size

    if x < 0:
        x = window_x
    elif x > window_x:
        x = 0
    if y < 0:
        y = window_y
    elif y > window_y:
        y = 0

    heat_map[(x, y)] = trail_size + 1

    return (x, y, direction)


def lerp_color(color1, color2, t):
    """
    Blend two colors together based on t (0.0 to 1.0).

    color1, color2: Tuples of (R, G, B) values (0-255)
    t: How much to blend color2 into color1
       - 0.0 returns color1
       - 1.0 returns color2
       - 0.5 returns the color halfway between them
    """
    new_color = []
    for c1, c2 in zip(color1, color2):
        diff = c2 - c1          # Find difference between each color channel
        new_val = int(c1 + diff * t)  # Move from c1 towards c2 by t percent
        new_color.append(new_val)      # Add the blended channel value
    # Return the new blended color as a tuple
    return tuple(new_color)


def value_to_color(value, min_val=1):
    """
    Convert a numeric value into a color on a gradient from black to yellow.

    value: The heat value to convert
    min_val, max_val: The expected range of values (for normalization)
    """
    # Normalize value to a 0-1 range (0 = min_val, 1 = max_val)
    t = (value - min_val) / (trail_size - min_val)  # ! 0.62

    # Define the color stops for the gradient
    colors = [
        (0.0,   (0, 0, 0)),          # Black
        (0.125, (64, 0, 64)),        # Dark violet
        (0.25,  (128, 0, 128)),      # Purple
        (0.375, (191, 0, 64)),       # Deep magenta
        (0.5,   (255, 0, 0)),        # Red
        (0.625, (255, 69, 0)),       # Reddish-orange (like OrangeRed)
        (0.75,  (255, 165, 0)),      # Orange
        (0.875, (255, 210, 100)),    # Light orange
        (1.0,   (255, 255, 0))       # Yellow
    ]

    # Find which two colors t falls between
    for i in range(len(colors) - 1):
        start_pos, start_color = colors[i]  # ! 0.5 , (255,0,0)
        end_pos, end_color = colors[i + 1]  # ! 0.75, (255,165,0)

        if start_pos <= t <= end_pos:  # ! if 0.5 <= 0.62 <= 0.75 TRUE
            # Calculate how far t is between the two color stops
            # ! (0.62 - 0.5) / (0.75 - 0.62) = 0.12 / 0.13 = 0.923
            local_t = (t - start_pos) / (end_pos - start_pos)
            # Blend those two colors and return the result
            # ! ((255,0,165), (255,165,0), 0.923)
            return lerp_color(start_color, end_color, local_t)

    # If t is exactly 1, return the last color (yellow)
    return colors[-1][1]


value_to_color(135)


if __name__ == "__main__":
    main()
