"""
Author: Daniela Zamorano-Martinez
Date: 12/2/2024
Assignment: Module 06 Practice Exercise 9-5
Descrip: Practice using GUI and create a guessing game with it. 

"""
import tkinter as tk

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")

#set variables      
        self.lower_bound = 1
        self.upper_bound = 100
        
        self.label = tk.Label(root, text="Think of a number between 1 and 100.\nClick 'New Game' to start.")
        self.label.pack(pady=10)
        
        self.guess_label = tk.Label(root, text="")
        self.guess_label.pack(pady=10)
        
        self.too_small_button = tk.Button(root, text="Too Small", command=self.too_small, state=tk.DISABLED)
        self.too_small_button.pack(side=tk.LEFT, padx=5)
        
        self.too_large_button = tk.Button(root, text="Too Large", command=self.too_large, state=tk.DISABLED)
        self.too_large_button.pack(side=tk.LEFT, padx=5)
        
        self.correct_button = tk.Button(root, text="Correct", command=self.correct, state=tk.DISABLED)
        self.correct_button.pack(side=tk.LEFT, padx=5)
        
        self.new_game_button = tk.Button(root, text="New Game", command=self.new_game)
        self.new_game_button.pack(pady=10)
#Begin a new game
    def new_game(self):
        self.lower_bound = 1
        self.upper_bound = 100
        self.current_guess = (self.lower_bound + self.upper_bound) // 2
        self.guess_label.config(text=f"My guess is: {self.current_guess}")
        self.enable_buttons()

#The guess was too small    
    def too_small(self):
        self.lower_bound = self.current_guess + 1
        self.update_guess()

#The guess was too big    
    def too_large(self):
        self.upper_bound = self.current_guess - 1
        self.update_guess()
    
#Guessed right and display the correct number
    def correct(self):
        self.guess_label.config(text=f"Hoorayyyyy! The number is {self.current_guess}.")
        self.disable_buttons()
    
    def update_guess(self):
        self.current_guess = (self.lower_bound + self.upper_bound) // 2
        self.guess_label.config(text=f"My guess is: {self.current_guess}")

#Set the buttons    
    def enable_buttons(self):
        self.too_small_button.config(state=tk.NORMAL)
        self.too_large_button.config(state=tk.NORMAL)
        self.correct_button.config(state=tk.NORMAL)

#This will disable to buttons 
    def disable_buttons(self):
        self.too_small_button.config(state=tk.DISABLED)
        self.too_large_button.config(state=tk.DISABLED)
        self.correct_button.config(state=tk.DISABLED)

# Run the program
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
