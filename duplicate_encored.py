def duplicate_encode(word):
    word = word.lower()
    counter = []
    letters = [x for x in word]

    for i in letters:
        counter.append(letters.count(i))

    return "".join(list(map(lambda x: "(" if x == 1 else ")", counter)))


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
