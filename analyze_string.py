def analyze_string(s: str) -> tuple:
    letter_count = sum(1 for letter in s if letter.isalpha())
    digit_count = sum(1 for letter in s if letter.isdigit())
    alnum_count = sum(1 for letter in s if letter.isalnum())    
    
    return (letter_count, digit_count, alnum_count)

print(analyze_string("Попробуй написать код для этой функции"))
print(analyze_string("Попробуй нап1исать код 3для эasdтой;;;; функции"))