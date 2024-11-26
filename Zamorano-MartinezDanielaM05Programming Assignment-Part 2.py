"""
Author: Daniela Zamorano-Martinez
Date: 11/25/24
Assignment: M05 Programming Assignment part 2
Decrip: Lets user guess a number 1 through 100. Gives them a hint if its too high or too low
"""
import random

def guessing_game():
    print("I have generated a random number between 1 and 100.")

#For the game to continue  
    while True:  

# Generate a random number
        random_number = random.randint(1, 100)

# Loop until the user guesses correctly
        while True: 
            try:
                guess = int(input("Enter your guess (1-100): "))
                
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                elif guess > random_number:
                    print("Too high, try again.")
                elif guess < random_number:
                    print("Too low, try again.")
                else:
                    print(f"Congratulations! You guessed the number {random_number}!")
# Exit the loop
                    break 
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        

# Call the function to start the game
if __name__ == "__main__":
    guessing_game()
