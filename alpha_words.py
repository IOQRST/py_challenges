from collections.abc import Generator
import re


def alpha_words(s: str) -> Generator[str]:
    for word in re.findall(r'[a-zA-Zа-яА-Я]+', s):
        if re.match(r"^[a-zа-я]+$", word.lower()):
            yield word


print(list(alpha_words("Hello 123 world! код")))
print(list(alpha_words("Python_код 2023")))
print(list(alpha_words("123 !@#")))
print(list(alpha_words("")))
