import os
from pathlib import Path

folder = Path(r"C:\Users\anton\Desktop")
jpgs = list(folder.glob("*.jpg"))
gifs = list(folder.glob("*.gif"))

jpgs.extend(gifs)

for jpg in jpgs:
    print(jpg)
