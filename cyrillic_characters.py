from collections.abc import Generator

def cyrillic_characters(s: str) -> Generator[str]:
    if not s:
        return
    
    for c in s.lower():
        if c.isalpha() and 'а' <= c <= 'я':
            yield c


print(list(cyrillic_characters('привет 123!')))
print(list(cyrillic_characters('Hello_код')))
print(list(cyrillic_characters('Python123')))
print(list(cyrillic_characters('')))