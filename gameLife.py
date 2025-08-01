import pygame
from sys import exit
from collections import defaultdict


def main():

    pygame.init()

    window_x = 1000
    window_y = 700
    info = pygame.display.Info()
    window_x = info.current_w
    window_y = info.current_h
    speed = 20
    cell_size = 10

    grid_rows = int(window_y / cell_size)  # * y is rows
    grid_cols = int(window_x / cell_size)  # * x is collumns

    screen = pygame.display.set_mode((window_x, window_y))

    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()
    screen.fill((30, 30, 30))

    cells = {}
    game_on = False

    while True:

        updated_cells = defaultdict(float)

        pygame.time.wait(int(1000/speed))

        pygame.display.flip()
        if game_on:
            screen.fill("black")
        else:
            screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_on = not game_on
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()

                col = x // cell_size
                row = y // cell_size

                cells[(row, col)] = 1

        for (row, col), cell in cells.items():

            pygame.draw.rect(
                screen, "white", (col * cell_size, row * cell_size, cell_size, cell_size))

            if game_on:

                check_col = [-1, 0, 1]
                check_row = [-1, 0, 1]

                if col == 0:
                    check_col.remove(-1)
                elif col == grid_cols - 1:
                    check_col.remove(1)
                if row == 0:
                    check_row.remove(-1)
                elif row == grid_rows - 1:
                    check_row.remove(1)

                for cc in check_col:  # * cc ->  check column
                    for cr in check_row:  # * cr -> check row
                        if (cc, cr) == (0, 0):
                            continue

                        if (row + cr, col + cc) in cells:
                            updated_cells[(row, col)] += 1
                        elif (row + cr, col + cc) not in cells:
                            updated_cells[(row + cr, col + cc)] += 0.1

        if game_on:
            cells.clear()
            for (row, col), value in updated_cells.items():
                if value == 2 or value == 3 or round(value, 2) == 0.3:
                    cells[(row, col)] = 1


if __name__ == "__main__":
    main()
