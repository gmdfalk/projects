#!/usr/bin/env python2

# Counts the number of individual words in a string. For added complexity
# read these strings in from a text file and generate a summary.

def read_file():
    with open("string_list", "r") as f:
        return f.read()

def print_length():
    content = read_file()
    word_count = len(content.split(" "))
    print word_count

print_length()
