from typing import Iterator

def even_numbers(n: int) -> Iterator[int]:
    if n < 0:
        return

    for i in range(0, n + 1, 2):
        yield i
        
print(list(even_numbers(6)))