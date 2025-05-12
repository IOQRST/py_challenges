from collections.abc import Generator

def squares(number: int) -> Generator[int]:
    if number < 0:
        raise ValueError("Input must be non-negative")
    
    for i in range(1, number + 1):
        yield i ** 2
        

if __name__ == '__main__':
    print(list(squares(3)))
    print(list(squares(5)))
    print(list(squares(0)))
    print(list(squares(-2)))