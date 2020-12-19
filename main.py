#! /usr/bin/env python3

from typing import List

from os import path, listdir

from document_templating import helpers, setup, document_generator, scraper
from document_templating.constants import TRANSFORMED_DOCUMENTS_KEY, TEMPLATES_KEY

if __name__ == '__main__':
    # load the templates directory path
    templates_dir: str = helpers.load_data(TEMPLATES_KEY)

    # if there doesn't exists a templates directory
    if not templates_dir or not path.exists(templates_dir):
        helpers.generate_menu_header('SETUP')
        templates_dir: str = setup.setup_templates_dir()

    # load the transformed documents directory path
    documents_dir: str = helpers.load_data(TRANSFORMED_DOCUMENTS_KEY)

    # if there doesn't exists a transformed documents directory
    if not documents_dir or not path.exists(documents_dir):
        documents_dir: str = helpers.setup_documents_dir(TRANSFORMED_DOCUMENTS_KEY)
    
    # load all the templates and enumerate them on a menu
    available_templates: List[str] = listdir(templates_dir)
    helpers.generate_menu(available_templates, 'CHOOSE TEMPLATE')

    # prompt the user to choose which template they would like to work on
    choice: int = int(input('What template would you like to use? '))

    # load the variables for the chosen template
    template_name: str = available_templates[choice]
    template: str = document_generator.get_template(f'{templates_dir}/{template_name}')

    print('\n')
    helpers.generate_menu_header(template_name.upper())

    print(helpers.highlight_variables(template))
    print('\n')

    # prompt the user to provide values for the template variables and substitue them
    company_name: str
    modified_template: str
    (company_name, modified_template) = document_generator.substitute_template_variables(template)

    # create the cover letter file
    document_file_name: str = f'{company_name}-cover_letter.txt'
    new_cover_letter_path: str = document_generator.create_cover_letter(f'{documents_dir}/{document_file_name}', company_name, modified_template)

    print('\n', f'Saved {company_name}-cover-letter.txt to {new_cover_letter_path}', '\n\n', modified_template)
