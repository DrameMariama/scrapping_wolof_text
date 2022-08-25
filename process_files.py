import os
import re

files = os.listdir("wolof")

print(len(files))
with open("combined_text.txt", "w") as file1:
    for file in files:
        if file != ".DS_Store":
            file_path = os.path.join("wolof", file)
            print(file_path)
            with open(file_path) as file2:
                text = file2.readlines()
                for line in text:
                    if len(line.split()) >= 5:
                        line = re.sub("\s", " ", line)
                        line = re.sub("[«”»“]", "", line)
                        line = line.lstrip(".")
                        line = line.strip()
                        # line = line.replace("”", "")
                        # line = line.replace("»", "")
                        file1.write(line)
                        file1.write("\n")


