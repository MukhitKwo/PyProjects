import json

with open("sudoku.json", "r") as soduku:
    sudokus = json.load(soduku)
    amount_grids = len(sudokus)

with open("sudoku/sudoku_form.txt", "r") as file:

    data = []
    for line in file:
        value = int(line.strip()) if line.strip() != "" else 0
        data.append(value)

    # print(data)

    grid = []
    for i in range(0, len(data), 9):
        chunk = data[i: i + 9]
        grid.append(chunk)

    print(f',\n"grid{amount_grids + 1}": [')
    for i, row in enumerate(grid):
        if i < len(grid) - 1:
            print(row, end=",\n")
        else:
            print(row)
    print(']')
