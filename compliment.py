
def compliment(seq):
    comp = []
    for i in seq:
        if i == "T":
            comp.append("A")
        elif i == "A":
            comp.append("T")
        elif i == "G":
            comp.append("C")
        elif i == "C":
            comp.append("G")

    return ''.join(comp)

