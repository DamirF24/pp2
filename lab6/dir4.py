
with open("text.txt", "r") as file:
    lines = file.readlines()
    line_count = len(lines)


print(f"Number of lines in the file: {line_count}")
