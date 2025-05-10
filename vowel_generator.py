def vowel_generator(s: str) -> str:
    vowels = {"а", "е", "и", "о", "у", "ы", "э", "ю", "я", "a", "e", "i", "o", "u"}
    for letter in s.lower():
        if letter in vowels:
            yield letter


print(list(vowel_generator("hello")))
