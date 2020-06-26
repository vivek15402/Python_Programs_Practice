# program to find all close matches of string

from difflib import get_close_matches

word = input("Enter the Word\n")

patterns = ['ape', 'apple', 'peach', 'puppy', 'viv', 'vivek']

print(get_close_matches(word, patterns))
