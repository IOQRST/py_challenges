from collections.abc import Generator
import re


def dates(text: str) -> Generator[str]:
    pattern = r'(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.\d{4}'
    for date in re.findall(pattern, text):
        yield date


if __name__ == '__main__':
    print(list(dates("Born: 01.01.2023, died: 15.12.2024")))
    print(list(dates("14.12.1990")))
    print(list(dates("No dates here")))
    print(list(dates("1.1.23")))
    print(list(dates("")))