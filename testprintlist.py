"""
Author: Daniela Zamorano-Martinez
Date: 11/25/24
Assignment: Module 05 Practice Exercise 7-5
"fixing" lee code, as well as write a scipt

"""
###
'''
This function works as expected because it prints the sequence and the element 
As the sequence continues, is shorten itself until its empty. 

The seq[1:] slices by creating a new sequence as well as create new memory for
the new sequence. 

It seems to me that like its almost a loop however we can see that it doesnt use
the for or while functions. It also uses multiple personal calls for each frame

Rescursion is more of an option, its more better to use in factorials and etc.. 
'''
####
"""
File: printAll.py
Starter code for Programming Exercise 7.5
Lee has discovered what he thinks is a clever recursive strategy for printing
the elements in a sequence (string, tuple, or list). He reasons that he can get
at the first element in a sequence using the 0 index, and he can obtain a sequence
of the rest of the elements by slicing from index 1. This strategy is realized in
a function that expects just the sequence as an argument. If the sequence is not
empty,
the first element in the sequence is printed and then a recursive call is executed.
On each recursive call, the sequence argument is sliced using the range `1:`.
Here is Lee’s function definition:
"""
def printAll(seq):
    if seq:
        print(seq, "->", seq[0])
        printAll(seq[1:])


# Testing the function
if __name__ == "__main__":
    print("Testing with a list:")
    printAll([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    printAll([0, 1, 2, 3, 4, 5, 6, 7, 8])
    printAll([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 11, ])