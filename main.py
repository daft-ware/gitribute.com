#!/usr/bin/env python

# this program needs json library in order to further work with it 

import json 


# json file with letters and number of days it takes to write them in the commit map 

json_letters = """
    {
        "a" : "1",
        "h" : "2",
        "o" : "3", 
        "j" : "4"
    }
"""


# parsed_letters stores (surprisengly) parsed json_letters, so that Python is able to work with them

parsed_letters = json.loads(json_letters)


# var phrase stores string that users want to write in their commit map 

phrase = input("Enter a phrase: ")

def main():
    
    
    # var days stores the number of days it's gonna take to write user's phrase, now set to zero 
    
    days = 0

    
    # for loop that goes over every letter in phrase and adds number of days to days var based on json dataset 
    
    for letter in phrase:
        days += int(parsed_letters[letter])

  
    print(days)

    
# this little trick makes an accessible library from code above and executes main() 

if __name__ == '__main__':
    main()
    
