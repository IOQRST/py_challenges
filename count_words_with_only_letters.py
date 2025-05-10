def count_words(s: str) -> int:
    count_only_letters = sum(1 for x in s.split(" ") if x.isalpha())
    count_letters_and_digits = sum(1 for x in s.split(" ") if x.isalnum())
    return f"В строке слов только с буквами - {count_only_letters}\nВ строке слов из букв и цифр - {count_letters_and_digits}"


print(count_words("Hello123 world! 45 python"))
