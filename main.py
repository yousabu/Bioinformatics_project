from compliment import compliment
from rna import *
from count_of_bases import *
from reverse_of_seq import *
from CG_CON import CG_contant

print("\t\t\t( This Program to perform operations on DNA )\t\t\t")
print("\t\t\t_____________________________________________\n")
print("\t\t\t  - To Find The Compliment Of DNA Press (1)  \t\t\t")
print("\t\t\t  - To Find The RNA Of DNA Press (2)  \t\t\t")
print("\t\t\t  - To Find The Reverse Of DNA Press (3)  \t\t\t")
print("\t\t\t  - To Find The Reverse of Compliment Of DNA Press (4)  \t\t\t")
print("\t\t\t  - To Find The Count Of Bases of DNA Press (5)  \t\t\t")
print("\t\t\t  - To Find The GC content And Length of seq Press (6)  \t\t\t")
print("\n")

seq = input("Please Enter The sequences Of DNA:  ")
seq = seq.upper()

ask = "y" or "Y"
close_loop = True
while close_loop:
    number_of_op = input("Enter Number Of Operation You Want To Perform:  ")
    if number_of_op == "1":
        print(compliment(seq))
    elif number_of_op == "2":
        print(rna(seq))
    elif number_of_op == "3":
        print(reverse(seq))
    elif number_of_op == "4":
        x = compliment(seq)
        print(reverse(x))
    elif number_of_op == "5":
        find_count(seq)
    elif number_of_op == "6":
        CG_contant(seq)
    elif number_of_op == "7":
        print(len(seq))
    else:
        print("Invalid number  Operation !!!")
    ask = input("Try Another Operation? (y/n)")
    if ask == "n" or "N":
        close_loop = False
