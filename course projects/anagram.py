
import time


start_time = time.time()

words = []

with open("2of4brif.txt", "r") as file:
    words = file.readlines()

name = input("Write a name: ").lower()

for anag in words:
    anag = anag.strip("\n")
    if sorted(anag) == sorted(name):
        if anag != name:
            print(anag)

print(time.time()-start_time)