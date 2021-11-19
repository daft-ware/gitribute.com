import json 

letters = """
{
    "a" : {
        "days" : "34"
        }
}
"""


parsed_letters = json.loads(letters)

print(parsed_letters["a"])

