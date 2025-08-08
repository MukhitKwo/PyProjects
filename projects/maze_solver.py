
from time import sleep


maze = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 0]
]

path = [0]


def maze_solver(pos, last, end):

    # sleep(0.1)

    x, y = pos

    if (-1 > x > len(maze) - 1) or (-1 > x > len(maze[0]) - 1):
        return False

    if maze[y][x] == 1:
        print("wall")
        return False

    print(f"x: {x}  y:{y} ; last: {last}")

    if pos == end:
        print("Found exit")
        path.append(pos)
        return True

    if ((x + 1, y) != last and maze_solver((x + 1, y), pos, end)) or \
        ((x, y + 1) != last and maze_solver((x, y + 1), pos, end)) or \
            ((x - 1, y) != last and maze_solver((x - 1, y), pos, end)):
        path.append(pos)
        return True


if __name__ == "__main__":
    maze_solver((0, 0), None, (3,4))

    path.reverse()
    path.remove(0)
    print(path)
