"""

Author:  Daniela Zamorano-Martinez
Date written: 11/18/24
Assignment:   Module04 Programming Assignment 
part1
Short Desc:   Lets user enter an integer greater than 1
and display the prime numbers less or equal to the number
the user entered. 

"""

def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def show_prime(toward):
    for num in range(2, toward + 1):
        if prime(num):
            print(num)

def main():
    num = int(input("Enter an integer greater than 1: "))

    if num <= 1:
        print("The number must be greater than 1.")
    else:
        print(f"Prime numbers less than or equal to {num}:")
        show_prime(num)

if __name__ == "__main__":
    main()