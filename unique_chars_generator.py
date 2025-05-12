from collections.abc import Generator

def unique_chars(s: str) -> Generator[str]:
    seen = set()
    
    if not s:
        return
    
    for char in s.lower():
        if char not in seen:
            seen.add(char)
            yield char
        
print(list(unique_chars("hello")))
print(list(unique_chars("Привет")))
print(list(unique_chars("Python Programming")))