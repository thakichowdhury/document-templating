import re

def scrape_variables(s: str) -> list:
    # find all substrings between pairs of square brackets { }
    return re.findall(r'{([^}]*)}', s)

# def scrape_defaults(l: list) -> dict:
#     defaults: dict = {}

#     # iterate through each string in input list of variables
#     for v in l:
#         # list destucture assign variable and default
#         variable, default = decompose_variable_and_default(v)

#         # to avoid overwriting a default with None, check if variable is NOT already in defaults before assigning
#         if variable not in defaults:
#             defaults[f'\{{v}\}'] = default

#     return defaults

def decompose_variable_and_default(s: str) -> list:
    variable = s
    default = None

    # if s has an equal sign, it means it has a default
    # find the index of the '=' in the string, else it will be -1
    i = s.find('=')

    # if there's a default
    if i != -1:
        # find the variable (substring before the equal sign)
        variable = s[:i]
        # find the default (substring after the equal sign)
        default = s[i + 1:]

    return [variable, default]

def scrape_variables_and_defaults(s: str) -> dict:
    v = scrape_variables(s)
    d = scrape_defaults(v)
    return d
