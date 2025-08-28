# add  obsidian notes

import os

note = "###### Tags: #python\n\n---\n\ntext\n\n```python\ncode\n```\n\ntext\n\n---"

note_name = input("Note name: ") + ".md"


folder_path = r"C:\Users\anton\Documents\Obsidian Vault\Python\New"

file_path = os.path.join(folder_path, note_name)

with open(file_path, "w") as f:
    f.write(note)

print(f"Note {note_name} created and added to obsidian")
