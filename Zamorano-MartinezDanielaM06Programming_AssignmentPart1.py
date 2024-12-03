"""
Author: Daniela Zamorano-Martinez
Date: 12/2/24
Assignment: Module 06 Programming Assignment
Descrip: While using GUI, let users enter a temperature and let them choose between C to F OR
F to C. 

"""
import tkinter as tk

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        
#Input
        self.label = tk.Label(root, text="Enter temperature:", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, width=10, font=("Arial", 12))
        self.entry.pack(pady=5)
        
#Output
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
        
#Buttons
        self.c_to_f_button = tk.Button(root, text="Convert to Fahrenheit", command=self.convert_to_fahrenheit)
        self.c_to_f_button.pack(side=tk.LEFT, padx=10)
        
        self.f_to_c_button = tk.Button(root, text="Convert to Celsius", command=self.convert_to_celsius)
        self.f_to_c_button.pack(side=tk.LEFT, padx=10)

#Convert Celsius to Fahrenheit. 
    def convert_to_fahrenheit(self):
        
        try:
            celsius = float(self.entry.get())
            fahrenheit = 9 / 5 * celsius + 32
            self.result_label.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
#Convert Fahrenheit to Celsius.
    def convert_to_celsius(self):
        try:
            fahrenheit = float(self.entry.get())
            celsius = (fahrenheit - 32) * 5 / 9
            self.result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()
