import re
def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents

def count_words(book_contents):
    words = book_contents.split()
    return len(words)

def count_characters(book_contents):
    letters = {}
    book_contents = book_contents.lower()
    for char in book_contents:
        if char in letters:
            letters[char] += 1
        else :
            letters[char] = 1
    return letters

# def sort_on(dict):
#     return dict["num"]

total_words = count_words(main("books/frankenstein.txt"))
letter_dict = count_characters(main("books/frankenstein.txt"))
# letter_dict.sort(reverse=True, key=sort_on)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{total_words} words found in the document")
print()
for entry in letter_dict:
    if entry.isalpha():
        print(f"The {entry} character was found {letter_dict[entry]} times")
print("--- End report ---")