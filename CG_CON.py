def CG_contant(seq):
    C = seq.count("C")
    G = seq.count("G")
    total = len(seq)
    gccontent = (G + C) / total
    print("the length of seq is :")
    print(total)
    print("the GC content is " + 'gccontent :')
    print(gccontent * 100)


