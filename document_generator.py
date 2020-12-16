#! /usr/bin/env python3

import os

import scraper
import helpers
import setup

from typing import List
from constants import TEMPLATES_KEY, TRANSFORMED_DOCUMENTS_KEY

def substitute_template_variables(template: str) -> tuple:
    # scrape the variables and default values from the template
    template_variables: list = scraper.scrape_variables(template)

    substitution_values: dict = {}

    # prompt for input on each variable and set to default value if no input is given
    for variable in template_variables:
        variable_name: str
        default_value: str

        variable_name, default_value = scraper.decouple_variable_and_default(variable)

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
    template_file_path = helpers.get_abs_file_path(rel_path, __file__)

    # read the template cover letter text
    f = open(template_file_path)
    template: str = f.read()
    f.close()

    return template

def create_cover_letter(path: str, company_name: str, document_body: str) -> str:
    with open(path, 'w') as f:
        f.write(document_body)

    return path

def create_example_template(dirname) -> str:
    """
    Creates an example template to place in dirname
    """

    example_template_path = f'{dirname}/example-template.txt'

    f = open(example_template_path, 'w')
    f.write('This is an example template.\n\nYou can include a variable in your templates by enclosing the variable name in curly braces.\n\ne.g. Dear {contact_name}\n\nPlease remember to keep your variable names one word with no spaces. If you have to seperate words consider using "_" to demarcate.\n\nYou can even set default values for your template by appending them to your variable name with an "=".\n\ne.g. Dear {contact_name=Hiring Team}, I would love to work at {company_name} and have the opportunity to showcase my skills in {skills=development, system design, and much more}.\n')
    f.close()

    return example_template_path

# execute the script
if __name__ == '__main__':
    # check if there's a templates
    templates_dir: str = helpers.load_data(TEMPLATES_KEY)
    # CHECK IF THE ACTUAL DIRECTORY EXISTS

    documents_dir: str = helpers.load_data(TRANSFORMED_DOCUMENTS_KEY)
    # CHECK IF THE ACTUAL DIRECTORY EXISTS

    # if there doesn't exists a templates directory
    if not templates_dir or not os.path.exists(templates_dir):
        helpers.generate_menu_header('SETUP')
        templates_dir: str = setup.setup_templates_dir()

        documents_dir_path: str = helpers.setup_documents_dir(TRANSFORMED_DOCUMENTS_KEY)
    
    # load all the templates and enumerate them on a menu
    available_templates: List[str] = os.listdir(templates_dir)
    helpers.generate_menu(available_templates, 'CHOOSE TEMPLATE')

    # prompt the user to choose which template they would like to work on
    choice: int = int(input('What template would you like to use? '))

    # load the variables for the chosen template
    template_name: str = available_templates[choice]
    template: str = get_template(f'{templates_dir}/{template_name}')

    # prompt the user to provide values for the template variables and substitue them
    company_name: str
    modified_template: str
    (company_name, modified_template) = substitute_template_variables(template)

    # create the cover letter file
    document_file_name: str = f'{company_name}-cover_letter.txt'
    new_cover_letter_path: str = create_cover_letter(f'{documents_dir}/{document_file_name}', company_name, modified_template)

    print('\n', f'Saved {company_name}-cover-letter.txt to {new_cover_letter_path}', '\n\n', modified_template)

