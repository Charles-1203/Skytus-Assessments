# Write a program to read a file and display its contents.

with open("file.txt", "r") as file:
    contents = file.read()
    print(contents)
file.close()

# Write a program to count the number of lines in a file.


with open("file.txt", "r") as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")
file.close() 


# Write a program to count how many times each word appears in a file.

from collections import Counter
with open("file.txt", "r") as file:
    contents = file.read()
    words = contents.split()
    word_count = Counter(words)
    print(word_count)
file.close()
# Write a program to write 5 user-entered sentences to a file.

file = open("file.txt", "a")

for i in range(5):
    sentence = input(f"Enter sentence {i+1}: ")
    file.write(sentence + "\n")

file.close()



# Write a program to append a list of strings to an existing file.

list=[  "this is charles",
        "hiii i am charles patel",]

with open("file.txt", "a") as file:
    for sentence in list:
        file.write(sentence + "\n")
file.close()

# Write a program to read a file and print only lines containing a specific word.

word = input("Enter the word to search: ")

with open("file.txt", "r") as file:
    for line in file:
        if word in line:
            print(line.strip())
file.close()

# Write a program to replace a specific word in a file and save changes.

search_word = input("Enter the word to search: ")
replace_word = input("Enter the replacement word: ")

with open("file.txt", "r", encoding="utf-8") as file:
    contents = file.read()

if search_word not in contents:
    print("Word not found.")
else:
    new_contents = contents.replace(search_word, replace_word)
    with open("file.txt", "w", encoding="utf-8") as file:
        file.write(new_contents)
    print(f"Replaced all occurrences of '{search_word}' with '{replace_word}'.")


# Write a program to merge the contents of two text files into a third file.

file1 = "file1.txt" 
file2 = "file2.txt"
merged_file = "merged_file.txt"
with open(file1, "r") as f1, open(file2, "r") as f2, open(merged_file, "w") as mf:
    contents1 = f1.read()
    contents2 = f2.read()
    mf.write(contents1 + "\n" + contents2)
f1.close()
f2.close()
mf.close()

# Write a program to read a CSV file and display its content in a formatted way.

import csv
csv_file = "data.csv"
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("\t".join(row))
file.close()


# Write a program to back up a file by copying its contents into another file.

import shutil
source_file = "file.txt"
backup_file = "file_backup.txt"
shutil.copy(source_file, backup_file)