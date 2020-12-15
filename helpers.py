#! /usr/bin/env python3

import os
from typing import List

def get_file_dir(file_path: str) -> str:
    return os.path.dirname(os.path.abspath(file_path))

def get_abs_file_path(rel_path: str, file_path: str) -> str:
    abs_path: str = get_file_dir(file_path)
    abs_file_path: str = os.path.join(abs_path, rel_path)

    return abs_file_path

def create_dir_if_not_exists(dirname: str) -> str:
    """
    Creates dir if it does not exist
    """
    # check if there is a templates dir
    if not os.path.exists(dirname):
        # create one if none exist
        os.makedirs(dirname)

    return os.path.exists(dirname)

def dir_is_empty(dirname: str) -> bool:
    """
    Returns bool indicating if dir is empty
    """
    return not os.listdir(dirname)

def generate_menu_header(menu_name: str = 'MENU', border_char: str = '*', border_width: int = 30, border_height: int = 5) -> None:
    """
    Generates a command-line menu header
    """
    # create the top and bottom menu rows
    top_bottom_rows: str = border_char * border_width

    # create the column rows
    column_rows: str = border_char + (' ' * (border_width - 2)) + border_char

    # create the center menu_name row
    is_menu_name_even: bool = len(menu_name) % 2 == 0
    number_of_enclosing_spaces: int = int((border_width - len(menu_name))/2 - 1)
    enclosing_spaces: str = ' ' * number_of_enclosing_spaces
    menu_name_row: str = border_char + enclosing_spaces + menu_name + (enclosing_spaces if is_menu_name_even else enclosing_spaces + ' ') + border_char

    for i in range(border_height):
        # if i is the top or bottom of the menu print the top or bottom rows
        if i == 0 or i == border_height - 1:
            print(top_bottom_rows)
        # if i is the center of the menu print the menu_name row
        elif i == (border_height - 1)/2:
            print(menu_name_row)
        else:
            print(column_rows)

def generate_menu_options(options: List[str]) -> None:
    """
    Generates menu options on the command line
    """

    for i in range(len(options)):
        print(i, ':', options[i])

    print('\n')

def generate_menu(options: List[str], menu_name: str) -> None:
    """
    Generates a command-line menu consisting of a header and menu options
    """

    generate_menu_header(options)
    generate_menu_options(options)

