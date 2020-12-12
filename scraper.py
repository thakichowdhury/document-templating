import re

def scrape_variables(template: str) -> list:
    """
    returns a list of the template variables inside the curly braces from input string s
    """
    # find all substrings between pairs of square brackets { }
    return re.findall(r'{([^}]*)}', template)

def decompose_variable_and_default(template_variable: str) -> list:
    """
    returns a list of the variable name and default value from the input template variable
    """
    variable = template_variable
    default = None

    # if template_variable has an equal sign, it means it has a default
    # find the index of the '=' in the string, else it will be -1
    i = template_variable.find('=')

    # if there's a default
    if i != -1:
        # find the variable (substring before the equal sign)
        variable = template_variable[:i]
        # find the default (substring after the equal sign)
        default = template_variable[i + 1:]

    return [variable, default]

