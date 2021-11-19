#!/usr/bin/env python

import json 

json_letters = """
    {
        "a" : "1",
        "h" : "2",
        "o" : "3", 
        "j" : "4"
    }
"""

phrase = input("Enter a phrase: ")

parsed_letters = json.loads(json_letters)

def main():
    days = 0

    for letter in phrase:
        days += int(parsed_letters[letter])

    print(days)

main()
