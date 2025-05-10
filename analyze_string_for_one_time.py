from typing import Tuple

def analyze_string(s: str) -> Tuple[int, int, int, int]:
    count_letters = 0
    count_digits = 0
    count_alnum = 0
    count_cyrillic = 0
    
    if not s:
        return (0, 0, 0, 0)
    
    for char in s:
        if char.isalpha():
            count_letters += 1
        if char.isdigit():
            count_digits += 1
        if char.isalnum():
            count_alnum += 1
        if char.isalpha() and 'а' <= char.lower() <= 'я':
            count_cyrillic += 1
    return (count_letters, count_digits, count_alnum, count_cyrillic) 