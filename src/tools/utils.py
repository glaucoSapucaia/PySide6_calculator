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
        ...
    return valid

def isEmpty(value: str) -> bool:
    return len(value) == 0

def checkInt(value: str):
    number = float(value)
    if number.is_integer():
        number = int(number)
    
    return number