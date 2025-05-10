from typing import Iterator
import re


def long_words(text: str, min_len: int) -> Iterator[str]:
    for word in re.findall(r"[a-zA-Zа-яА-ЯёЁ]+", text):
        if len(word) >= min_len:
            yield word


if __name__ == "__main__":
    print(list(long_words("Hello world код", 4)))
    print(
        list(
            long_words(
                "Я вас любил, любовь еще быть может в душе моей угасла не совсем", 5
            )
        )
    )
    print(list(long_words("a b cd", 4)))  # []
    print(list(long_words("", 4)))  # []
