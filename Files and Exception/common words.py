"""
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text. This will be
an approximation because it will also count words such as 'then' and 'there'.
Try counting 'the ', with a space in the string, and see how much lower your
count is.
"""


def read_file(files, word):
    for filename in files:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                print(filename.upper())
                print('+-' * 10)
                contents = file.read()

        except FileNotFoundError:
            print(f'{filename} not found in the directory specified')
            print('')
            continue

        except UnicodeDecodeError:
            print('Error: Unable to decode the file due to unsupported characters')
            continue

        for i in word:
            count = contents.lower().count(i)
            print(f"The word '{i}' appears {count} times in {filename} ")

        print('~'*50)


words = ['the', 'the ', 'Police']
notes = ['cats.txt', 'dogs.txt', 'Alice.txt']
read_file(notes, words)
