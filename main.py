import json 

json_letters = """
{
    "a" : {
        "days" : "34"
        }
}
"""

phrase = input("Enter a phrase: ")

parsed_letters = json.loads(json_letters)

print(parsed_letters["a"])
