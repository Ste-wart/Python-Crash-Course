"""
10-11. Favorite Number: Write a program that prompts for the user’s
favorite number. Use json.dumps() to store this number in a file. Write a
separate program that reads in this value and prints the message “I know
your favorite number! It’s _____.”
"""
from pathlib import Path
import json


def ask_fav_num():
    """Prompts for the user’s favorite number"""
    fav = input(" Enter your favourite number; ")
    return fav


def store(path):
    """Stores The user's favorite number"""
    fav_num = ask_fav_num()
    contents = json.dumps(fav_num)
    path.write_text(contents)
    return fav_num


def bring(path):
    """Retrieves The user's favorite number"""
    if path.exists():
        contents = path.read_text()
        value = json.loads(contents)
        return value
    else:
        return None


def favour(file):
    path = Path(file)
    number = bring(path)
    if number:
        print(f"I know your favorite number! It’s {number}")
    else:
        store(path)


favour('fav_num.json')
