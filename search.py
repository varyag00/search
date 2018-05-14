"""Efficiently search for text recursively using generators"""
import os
import sys
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')
SearchResult.__str__ = lambda self: f' \n---------- MATCH ---------- \n' \
                                    f'file: {self.file} \n' \
                                    f'line: {self.line} \n' \
                                    f'text: {self.text.strip()}'

APP_NAME = 'SEARCHER'


def main():
    print_header()

    if len(sys.argv) < 2:
        dir_name = get_dir_input()
        text = get_search_text_input()
    else:
        dir_name, text = get_argv_input()
        print(f'Searching {dir_name} for {text}')

    results = search_dir(dir_name, text)
    for result in results:
        print(result)


def print_header():
    print(f'{APP_NAME}\n')


def get_argv_input():
    dir_name = sys.argv[1]
    if not validate_dir(dir_name):
        raise IOError('Invalid directory.')
    text = sys.argv[2].lower()
    return dir_name, text


def get_dir_input():
    dir_path = ''
    while not validate_dir(dir_path):
        dir_path = input('Enter directory to search for: ')
    return os.path.abspath(dir_path)


def validate_dir(dir_path):
    if not dir_path.strip():
        print('Search directory cannot be empty.')
        return False
    if not os.path.isdir(dir_path):
        print('Search directory not found.')
        return False
    return True


def get_search_text_input():
    text = ''
    while not text.strip():
        text = input('Enter text to search for: ')
    return text.lower()


def search_dir(dir, text):
    all_matches = []
    items = os.listdir(dir)

    for item in items:
        full_item = os.path.join(dir, item)
        if os.path.isdir(full_item):
            all_matches.extend(search_dir(full_item, text))
        else:
            matches = search_file(full_item, text)
            all_matches.extend(matches)

    return all_matches


def search_file(filename, text):
    matches = []
    with open(filename, 'r', encoding='utf-8') as file:

        for line_index, line in enumerate(file):
            if line.lower().find(text) >= 0:
                m = SearchResult(file=filename, line=line_index, text=line)
                matches.append(m)

    return matches


if __name__ == '__main__':
    main()
