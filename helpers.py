#! /usr/bin/env python3

from os import path

def get_file_dir(file_path: str) -> str:
    return path.dirname(path.abspath(file_path))

def get_abs_file_path(rel_path: str, file_path: str) -> str:
    abs_path: str = get_file_dir(file_path)
    abs_file_path: str = path.join(abs_path, rel_path)

    return abs_file_path

def generate_menu_options(options: list, menu_name = 'MENU') -> None:
    border_char = '*'
    border_width = 30
    border_height = 5
    s = int((border_width - len(menu_name))/2 - 3)

    print(border_char * border_width)

    for i in range(border_height - 2):
        if i == (border_height - 3)/2:
            print(border_char, ' ' * s, menu_name, ' ' * s, border_char)
        else:
            print(border_char, ' ' * (border_width - 4), border_char)

    print(border_char * border_width)

    for i in range(len(options)):
        print(i, ':', options[i])

    print('\n')

