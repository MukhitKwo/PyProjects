import time

start_time = time.time()

with open("2of4brif.txt", "r") as file:

    words = file.readlines()

with open("2of4brif.txt", "w") as file:

    for w in words:
        if len(w.strip("\n")) > 1:
            file.write(w)

end_time = time.time()

print(round(end_time-start_time, 3))