def spin_words(sentence):
    wrds = sentence.split(" ")
    for i in range(len(wrds)):
        if len(wrds[i]) >= 5:
            wrds[i] = "".join(reversed(wrds[i]))
    return " ".join(wrds)


print(spin_words("Welcome"))
print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))
