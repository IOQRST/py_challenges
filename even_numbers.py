from collections.abc import Generator

def even_numbers(n: int) -> Generator[int]:
    if n < 0:
        return

    for i in range(0, n + 1, 2):
        yield i
        
print(list(even_numbers(6)))