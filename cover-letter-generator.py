#! /usr/bin/env python3

import os
import scraper
import helpers

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

def create_cover_letter(company_name: str, cover_letter_content: str) -> str:
    # get path for new cover letter
    new_cover_letter_path: str = helpers.get_abs_file_path(f'_cover-letters/{company_name}-cover_letter.txt', __file__)

    # save template changes to new cover letter
    f = open(new_cover_letter_path, 'w')
    f.write(cover_letter_content)
    f.close()

    return new_cover_letter_path

def create_example_template(dirname) -> str:
    """
    Creates an example template to place in dirname
    """

    example_template_path = f'{dirname}/example-cover-letter.txt'

    f = open(example_template_path, 'w')
    f.write('This is an example template.\n\nYou can include a variable in your templates by enclosing the variable name in curly braces.\n\ne.g. Dear {contact_name}\n\nPlease remember to keep your variable names one word with no spaces. If you have to seperate words consider using "_" to demarcate.\n\nYou can even set default values for your template by appending them to your variable name with an "=".\n\ne.g. Dear {contact_name=Hiring Team}, I would love to work at {company_name} and have the opportunity to showcase my skills in {skills=development, system design, and much more}.')
    f.close()

    return example_template_path

# execute the script
if __name__ == '__main__':
    templates_dir: str = os.path.abspath('templates')

    helpers.create_dir_if_not_exists(templates_dir)

    if helpers.dir_is_empty(templates_dir):
        # create and place an example template in the dir
        create_example_template(templates_dir)
        # raise Exception('EMPTY templates directory!')

    # get the list of available templates in the templates dir
    available_templates: list = os.listdir(templates_dir)

    # generate list of menu options consisting of the templates in the templates dir
    helpers.generate_menu_options(os.listdir(templates_dir))

    choice: int = int(input('What template would you like to use? '))
    print('\n')

    template_name: str = available_templates[choice]
    template: str = get_template(f'{templates_dir}/{template_name}')

    company_name: str
    modified_template: str
    (company_name, modified_template) = substitute_template_variables(template)

    new_cover_letter_path: str = create_cover_letter(company_name, modified_template)

    print('\n', f'Saved {company_name}-cover-letter.txt to {new_cover_letter_path}', '\n\n', modified_template)

