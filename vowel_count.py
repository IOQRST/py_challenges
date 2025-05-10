def get_count(sentence):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in sentence:
        if i in vowels:
            count += 1
    return count


print(get_count("aeiou"))
