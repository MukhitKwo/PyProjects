with open("txt_files/cypherText.txt", "r") as file:
    # cypher = file.readline().replace(",", "").replace(".", "").split()

    cypher_line = file.readline()  # reads the first line
    cypher_line = cypher_line.replace(",", "").replace(
        ".", "")  # replaces , and . with nothing
    cypher = cypher_line.split()  # stores each word in a separate index in the list

# cols, rows = int(input("Cols: ")), int(input("Rows: "))

cols, rows = 5, 4

key = [int(k) for k in input("Key: ").split()]

for k in key:
    if k < 0:
        pass
    elif k > 0:
        pass

print(key)
