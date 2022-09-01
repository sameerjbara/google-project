from typing import List
from string import ascii_lowercase
from pathlib import Path
# from autocomplete import AutoCompleter
import os
import classes

# FILES_PATH = r"Archive/python-3.8.4-docs-text/my_file"
FILES_PATH = r"Archive"


def insert_to_tree(t: classes.Trie, dictionary: dict):
    files = list(Path(FILES_PATH).rglob("*.[tT][xX][tT]"))
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            filename = os.path.basename(f.name)
            for line in f.readlines():
                t.insert(line, filename)
                # dictionary[line] = filename


def get_best_k_completions(prefix: str) -> List[classes.AutoCompleteData]:
    lst = []
    pass


def autocomplete() -> None:
    tree = classes.Trie()
    dictionary_filename_sentences = {}
    insert_to_tree(tree, dictionary_filename_sentences)
    inp = ""

    while True:
        current = input(f"Enter search: {inp}")
        if current == '#':
            inp = input("Enter new search pattern: ")
        else:
            inp += current
        print(tree.search(inp, inp.rsplit(None, 1)[-1]))


if __name__ == '__main__':
    autocomplete()

# def get_score(e):
#     return e.score
