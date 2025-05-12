from collections.abc import Generator

def fibonacci(n: int) -> Generator[int]:
    a = 0
    b = 1
    
    if n <= 0:
        return
    
    for _ in range(n):
        yield a
        a, b = b, a + b
        
print(list(fibonacci(5)))
print(list(fibonacci(3)))
print(list(fibonacci(0)))
print(list(fibonacci(1)))