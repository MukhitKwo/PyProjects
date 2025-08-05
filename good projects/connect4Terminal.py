import os

redPin = '🔴 '
yellowPin = '🟡 '

# ! 6 rows ; 7 cols


def show_connect4(con4):
    print()
    for row in reversed(con4):
        print("|", end="")
        for col in row:
            print(redPin if col == 1 else yellowPin if col ==
                  2 else "   ", end="|")
        print("\n+---+---+---+---+---+---+---+")
    print("=-1-=-2-=-3-=-4-=-5-=-6-=-7-=\n")


def drop_piece(con4, col, player):
    col -= 1
    if col > 6:
        print("Column doesnt exist")
        return False, (None, None)

    # * len gives list size (6), range separates size (1,2,...,6) and reversed inverts the numbers (6,5,...,1)
    for row in range(len(con4)):
        if con4[row][col] == 0:
            con4[row][col] = player
            # show_connect4(con4)
            return True, check_win(con4, row, col)
    print(f"No left space on {col + 1}")
    return False, (None, None)


def check_win(con4, lastRow, lastCol):

    currentPin = con4[lastRow][lastCol]

    for i in range(4):

        rowPins = 1

        xAdd = 1
        yAdd = 1

        if i == 0:
            pass
        elif i == 1:
            xAdd = 0
        elif i == 2:
            xAdd = -1
        elif i == 3:
            yAdd = 0

        x = xAdd
        y = yAdd

        while True:

            if ((lastRow + x) < 0 or (lastRow + x > 5)) or ((lastCol + y) < 0 or (lastCol + y) > 6):
                break

            checkPin = con4[lastRow + x][lastCol + y]

            if currentPin == checkPin and i != 3:
                rowPins += 1

                x += xAdd
                y += yAdd
            else:
                break

        x = xAdd
        y = yAdd

        while True:

            if ((lastRow - x) < 0 or (lastRow - x > 5)) or ((lastCol - y) < 0 or (lastCol - y) > 6):
                break

            checkPin = con4[lastRow - x][lastCol - y]

            if currentPin == checkPin:

                rowPins += 1

                x += xAdd
                y += yAdd
            else:
                break

        if rowPins >= 4:
            return True, currentPin

        # print("In row:", rowPins)
    return False, None


def main():

    p1Name = input("Nome jogador 1: ")
    p2Name = input("Nome jogador 2: ")

    p1Points = 0
    p2Points = 0

    player = 1
    # show_connect4(con4)

    while True:

        con4 = [[0 for _ in range(7)] for _ in range(6)]

        while True:
            os.system('cls')

            show_connect4(con4)

            print("Play:", p1Name if player == 1 else p2Name, end=" ")
            print(redPin if player == 1 else yellowPin)

            add_to_col = input("Column: ")
            if add_to_col == "e":
                break
            elif add_to_col == "":
                continue

            pinDropped, win = drop_piece(con4, int(add_to_col), player)
            playerWon, whichPlayer = win

            if pinDropped:

                player = player % 2 + 1

                if playerWon:
                    os.system('cls')
                    show_connect4(con4)

                    if whichPlayer == 1:
                        print(f"{p1Name} ganhou!")
                        p1Points += 1
                    else:
                        print(f"{p2Name} ganhou!")
                        p2Points += 1

                    print(f"{p1Name}: {p1Points} | {p2Name}: {p2Points}")
                    break


        if input("\nQueres jogar outra vez? (s/n): ") == "n":
            break


if __name__ == "__main__":
    main()
