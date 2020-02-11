from pathlib import Path

FILENAME = "U5.txt"

file_contents = Path(FILENAME).read_text()

body = file_contents.split('\n')[1:]

x = body.replace('"', "").replace("\n", "").split(',')

print(x)
