#!/usr/bin/env python

# this program needs json library in order to further work with it 

import json 

# json file with letters and numbers of days it takes to write them in the commit map 


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

    
if __name__ == '__main__':
    main()

    
