#! /usr/bin/env python3

import tkinter as tk
from tkinter import filedialog

from typing import List

from helpers
import document_generator

def setup_initial_templates_dir() -> str:

    print('Please select a location to store your templates.')

    dir_path: str = filedialog.askdirectory(title='Select folder to store your templates')
    template_dir_path: str = dir_path + '/_templates'

    helpers.create_dir_if_not_exists(template_dir_path)
    document_generator.create_example_template(template_dir_path)

    return template_dir_path

