from collections.abc import Generator
import re


def phone_numbers(text: str) -> Generator[str]:
    pattern = r'\+\d-\d{3}-\d{3}-\d{4}|\+\d{11}'
    for number in re.findall(pattern, text):
        yield number
        


if __name__ == "__main__":
    print(list(phone_numbers("Call: +1-123-456-7890 or +112345678901")))
    print(list(phone_numbers("No phones here")))
    print(list(phone_numbers("123-456-7890")))
    print(list(phone_numbers("")))
