import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def isNumOrDot(value: str) -> bool:
    return bool(NUM_OR_DOT_REGEX.search(value))

def isValidNumber(value: str) -> bool:
    valid = False
    try:
        float(value)
        valid = True
    except ValueError:
        print('Value error')
    return valid