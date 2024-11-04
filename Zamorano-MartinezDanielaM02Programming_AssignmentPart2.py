"""

Author:  Daniela Zamorano-Martinez
Date written: 01/04/24
Assignment:   Module02 Programming Assignment part2
Short Desc: Lets the user enter a non negative number and 
calculates the factorial of that number

"""
#Get a nonnegative integar from user
number = int (input("Enter a nonnegative integer: "))

#initialize
factorial = 1

#loop for calculation
for i in range (1, number+1):
    factorial *= i


#output the results
print(f"The factorial of {number} is {factorial}")
