""" This function ensures user is inputting
    a valid postfix, the postfix is capable of handling
    spaces and will only process a postfix with letters and these characters '+-^*/'
"""


def is_postfix_valid(postfix):
    # Remove white spaces
    tokens = postfix.replace(' ', '')

    # check if postfix has valid characters
    for char in tokens:
        if not (char.isalpha() or char in '^*/+-'):
            return False

    # Check if the first two characters are not operators
    if tokens[0] in '*/+-^' or tokens[1] in '^*/+-':
        return False
    return True