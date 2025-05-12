from collections.abc import Generator
import re


def emails(text: str) -> Generator[str]:
    for address in re.findall(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text):
        yield address


print(list(emails("Contact: user@example.com, admin@test.ru")))
print(list(emails("No emails here")))
print(list(emails("user@com")))
print(list(emails("")))
