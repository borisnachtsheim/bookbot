import time
path_to_file = "github.com/bookbot/books/frankenstein.txt"
with open(path_to_file, encoding="utf-8") as f:
    file_content = f.read()
    file_content_lower = file_content.lower()
    letter_count = {}
    for char in file_content_lower:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    total_count = []
    for char in letter_count:
        total_count.append(letter_count[char])  
    sorted_letter_count = {k: letter_count[k] for k in sorted(letter_count)}
    print(f"Here's is a summary of the word count in the document {path_to_file}:")
    print(f"The total string count in this document is: {sum(total_count)}")
    print(f"These strings are distributed as follows:")
    for key, value in sorted_letter_count.items():
        print(f"The {key} character was found {value} times")
        time.sleep(1)
    