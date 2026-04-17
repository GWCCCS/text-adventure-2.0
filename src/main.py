# dep

import os

from adventure import Adventure


# const

ADVENTURES_DIR = "res"


# util

def choose_file(dir: str) -> str:
    print("Choose a file:")
    filenames = [ f for f in os.listdir(dir) if f.endswith(".json") ]
    for i, f in enumerate(filenames): print(f"{i+1}. {f}")
    while True:
        user_input = input("> ")
        try:
            idx = int(user_input) - 1
            if 0 >= idx < len(filenames):
                return f"{dir}/{filenames[idx]}"
        except ValueError: pass

# main

def main():
    filename = choose_file(ADVENTURES_DIR)
    print("\n" * 2)
    adventure = Adventure(filename)
    adventure.begin()


# main

if __name__ == '__main__':
    print("\n" * 3)
    main()