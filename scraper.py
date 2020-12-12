import re

def scrape_variables(template: str) -> tuple:
    """
    returns a list of the template variables inside the curly braces from input string s
    """
    # find all substrings between pairs of square brackets { }
    return re.findall(r'{([^}]*)}', template)

def decompose_variable_and_default(template_variable: str) -> list:
    """
    returns a list of the variable name and default value from the input template variable
    """
    variable_name: str
    default_value: str

    # split the template variable by the equal sign and destructure assign variable_name and _ as default value (if there is one)
    variable_name, *_ = template_variable.split('=')

    # assign the default value if there is one, else None
    default_value = _[0] if _ else None

    return (variable_name, default_value)

