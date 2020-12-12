#! /usr/bin/env python3

from os import path

def get_file_dir(file_path: str) -> str:
    return path.dirname(path.abspath(file_path))

def get_abs_file_path(rel_path: str, file_path: str) -> str:
    abs_path: str = get_file_dir(file_path)
    abs_file_path: str = path.join(abs_path, rel_path)

    return abs_file_path

