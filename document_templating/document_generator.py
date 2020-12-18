#! /usr/bin/env python3

from typing import List

import os

from .scraper import scrape_variables, decouple_variable_and_default
from .helpers import get_abs_file_path
from .setup import setup_templates_dir

def substitute_template_variables(template: str) -> tuple:
    # scrape the variables and default values from the template
    template_variables: list = scrape_variables(template)

    substitution_values: dict = {}

    # prompt for input on each variable and set to default value if no input is given
    for variable in template_variables:
        variable_name: str
        default_value: str

        variable_name, default_value = decouple_variable_and_default(variable)

        if variable_name not in substitution_values:
            # get the user-input value for the given variable
            input_value: str = input(f'Enter {variable_name}: ')

            # throw exception if there's no given input or default value given to the variable
            if input_value == '' and default_value == None:
                raise Exception(f'There was no user-input or default value for {variable_name}')

            # assign the subtitution value of the variable name to the user-input or default value
            substitution_values[variable_name]: str = input_value or default_value

        # search and replace all variables in the template (enclosed by curly braces) with their substitution value
        template = template.replace('{' + variable + '}', substitution_values[variable_name])

    # format the company name for saving to disk
    company_name: str = substitution_values['company_name'].lower().replace(' ', '-')

    return (company_name, template)

def get_template(rel_path: str) -> str:
    template_file_path = get_abs_file_path(rel_path, __file__)

    # read the template cover letter text
    f = open(template_file_path)
    template: str = f.read()
    f.close()

    return template

def create_cover_letter(path: str, company_name: str, document_body: str) -> str:
    with open(path, 'w') as f:
        f.write(document_body)

    return path

