# A - T G - C
def DNA_strand(dna):
    lst = []
    for i in dna:
        if i == "A":
            lst.append("T")
        elif i == "T":
            lst.append("A")
        elif i == "C":
            lst.append("G")
        elif i == "G":
            lst.append("C")
    return "".join(lst)


print(DNA_strand("AAAA"))
print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))
