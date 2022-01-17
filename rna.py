from compliment import compliment


def rna(seq):
    com = compliment(seq)
    cop_to_list = list(com)
    for base in cop_to_list:
        if base == "T":
            index_of_base = cop_to_list.index(base)
            cop_to_list[index_of_base] = "U"
    return ''.join(cop_to_list)
