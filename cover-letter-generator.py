#! /usr/bin/env python3

"""
TODO:
    - abstract out variables to scrape from template
    - abstract out default values to pull from template
        - e.g. ${contact_name:Hiring Manager}

"""

from os import path
# from scraper import scrape_variables_and_defaults
import scraper

# find path to template cover letter
abs_path = path.dirname(path.abspath(__file__))
rel_path = '_cover-letters/_template-cover-letter.txt'
file_path = path.join(abs_path, rel_path)

# read and store the template cover letter
f = open(file_path)
template: str = f.read()
f.close()

# scrape the variables and default values from the template
template_variables: list = scraper.scrape_variables(template)

substitution_values: dict = {}

# prompt for input on each variable and set to default value if no input is given
for variable in template_variables:
    variable_name, default_value = scraper.decompose_variable_and_default(variable)

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

# create a new cover letter file
company_name: str = substitution_values['company_name'].lower().replace(' ', '-')

new_cover_letter_path = f'{abs_path}/_cover-letters/{company_name}-cover_letter.txt'
f = open(new_cover_letter_path, 'x')

# save template changes to new cover letter
f.write(template)
f.close()

print('\n')
print(f'Saved {company_name}-cover-letter.txt to {new_cover_letter_path}')
print('\n')
print(template)

