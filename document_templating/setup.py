#! /usr/bin/env python3

from .helpers import setup_documents_dir

def setup_templates_dir() -> str:
    template_dir_path: str = setup_documents_dir('templates')

    create_example_template(template_dir_path)

    return template_dir_path

def create_example_template(dirname) -> str:
    """
    Creates an example template to place in dirname
    """

    example_template_path = f'{dirname}/example-template.txt'

    f = open(example_template_path, 'w')
    f.write('This is an example template.\n\nYou can include a variable in your templates by enclosing the variable name in curly braces.\n\ne.g. Dear {contact_name}\n\nPlease remember to keep your variable names one word with no spaces. If you have to seperate words consider using "_" to demarcate.\n\nYou can even set default values for your template by appending them to your variable name with an "=".\n\ne.g. Dear {contact_name=Hiring Team}, I would love to work at {company_name} and have the opportunity to showcase my skills in {skills=development, system design, and much more}.\n')
    f.close()

    return example_template_path

