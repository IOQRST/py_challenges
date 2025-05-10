def decompose_list(ls: list) -> list:
    only_letters = [letter for letter in ls if letter.isalpha()]
    letters_with_digits = [letter for letter in ls if letter.isalnum()]
    return(f"{only_letters}\n{letters_with_digits}")

print(decompose_list(["apple", "123", "cat!", "dog", "45ab"]))