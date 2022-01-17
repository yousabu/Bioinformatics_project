DNA_sequence=input("Please enter seq to check it ")
DNA_Nucleotides=["A","T","C","G"]
RNA_Nucleotides=["U","T","C","G"]
def check_seq(seq):
    DNA_temp=seq.upper()
    for nuc in DNA_temp:
        if "U" in DNA_temp:
            return "This seq is  RNA strand "
        else:
            return "this seq is DNA strand "

    return "This Not Nucleic acid"
print(check_seq(DNA_sequence))