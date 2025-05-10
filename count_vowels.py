def count_vowels(s: str) -> int:
    vowels = {'а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'a', 'e', 'i', 'o', 'u'}
    return sum(1 for v in s.lower() if v in vowels)

print(count_vowels("python"))
print(count_vowels("однажды в студеную зимнюю пору я из лесу вышел был сильный мороз"))
print(count_vowels("the quick brown fox jumps over the wood"))
print(count_vowels("пайтон"))