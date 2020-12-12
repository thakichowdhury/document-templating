#! /usr/bin/env python3

import scraper
import helpers

def substitute_template_variables(template: str) -> str:
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

def get_template(rel_path: str = '_cover-letters/_template-cover-letter.txt') -> str:
    template_file_path = helpers.get_abs_file_path(rel_path, __file__)

    # read the template cover letter text
    f = open(template_file_path)
    template: str = f.read()
    f.close()

    return template

def generate_cover_letter(cover_letter_content: str) -> tuple:
    # format the company name for saving to disk
    company_name: str = substitution_values['company_name'].lower().replace(' ', '-')

    # get path for new cover letter
    new_cover_letter_path str = helpers.get_abs_file_path('_cover-letters/{company_name}-cover_letter.docx', __file__)

    # save template changes to new cover letter
    f = open(new_cover_letter_path, 'x')
    f.write(cover_letter_content)
    f.close()

    return (company_name, new_cover_letter_path)

# execute the script
if __name__ == '__main__':
    template: str = get_template()
    modified_template: str = substitute_template_variables(template)

    new_cover_letter_path: str
    company_name: str
    company_name, new_cover_letter_path = generate_cover_letter(modified_template)

    print('\n', f'Saved {company_name}-cover-letter.txt to {new_cover_letter_path}', '\n', template)

