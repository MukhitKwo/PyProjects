
def find_pali():
    with open("2of4brif.txt", "r") as file:

        palidromes = []

        for word in file:
            word = word.strip("\n")
            if word == word[::-1]:
                palidromes.append(word)

    print(f"Theres {len(palidromes)} palindromes")

    for pali in palidromes:
        print(pali, end=", ")

find_pali()