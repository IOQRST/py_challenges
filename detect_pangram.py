def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    st = st.lower()
    for i in alphabet:
        if i not in st:
            return False
    return True


print(is_pangram("The quick brown fox jumps over the lazy dog."))
print(is_pangram("Cwm fjord bank glyphs vext quiz."))
print(is_pangram("Pack my box with five dozen liquor jugs."))
print(is_pangram("How quickly daft jumping zebras vex."))
print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"))
print(is_pangram("This isn't a pangram!"))
print(is_pangram("abcdefghijklm opqrstuvwxyz"))
print(is_pangram("Aacdefghijklmnopqrstuvwxyz"))
