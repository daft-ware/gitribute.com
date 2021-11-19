# gitribute.com lets you create custom text in GitHub commit map!
 
## Master the UI

## Understand the code 

The program is written in Python 3.10

### Code structure with snippets of code 

+ The program is given a json file with letters and number of days it takes to write them to the commit map 

```py
json_letters = """
    {
        "a" : "1",
        "h" : "2",
        "o" : "3", 
        "j" : "4"
    }
"""
```

+ The data is parsed to parsed_letters so Python can further work with them 

```py
parsed_letters = json.loads(json_letters)
```
