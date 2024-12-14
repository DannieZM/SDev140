"""
Name: Daniela Zamorano-Martinez




"""
#Imports allow images and pop-up messages to appear in the GUI
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Main Application Class
class GroceryListManager:
#Method
    def __init__(self, root):
#The main window of the application
        self.root = root
        self.root.title("Grocery List")
        
#Initialize grocery list (create an empty list to store items)
        self.grocery_list = []

#Main Window
#Create frame widget
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

#Load and display the main image using Pillow
#Open the image file
        self.image = Image.open("C:/Users/danie/Downloads/Grocery Basket.jpg")
#Convert to Tkinter
        self.photo = ImageTk.PhotoImage(self.image)
#Creates label
        self.image_label = tk.Label(self.main_frame, image=self.photo)
        self.image_label.pack(pady=10)

#Title Label
#Creates the text with certain fonts
        self.title_label = tk.Label(self.main_frame, text="Grocery List", font=("Open Sans", 16,"bold"), padx=20, pady=20)
        self.title_label.pack()

#Add Item Button
#Creates add item button label
#Also has an assign command
        self.add_item_button = tk.Button(self.main_frame, text="Add Item", command=self.open_add_window)
        self.add_item_button.pack(pady=5)

#View List Button
#Creates a button label "View grocery list"
#Also has a command 
        self.view_list_button = tk.Button(self.main_frame, text="View Grocery List", command=self.open_view_window)
        self.view_list_button.pack(pady=5)

#Remove Item Button
#Creates a button label for removing items
#Also assigned command
        self.remove_item_button = tk.Button(self.main_frame, text="Remove Item", command=self.open_remove_window)
        self.remove_item_button.pack(pady=5)

#Exit Button
#Creates a button label for exit
#Assign to close the main window when clicked
        self.exit_button = tk.Button(self.main_frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

#This opens a new window 
    def open_add_window(self):
        self.new_window = tk.Toplevel(self.root)
#Open window is called "add Item"
        self.new_window.title("Add Item")

#Entry Box that allows users to add items
        tk.Label(self.new_window, text="Enter Item Name:").pack(pady=5)
        self.item_entry = tk.Entry(self.new_window, width=30)
        self.item_entry.pack(pady=5)

#Add Button recalls to the add_item button method
        add_button = tk.Button(self.new_window, text="Add", command=self.add_item)
        add_button.pack(pady=5)

#Opens a new window titles "Grocery List"
    def open_view_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Grocery List")

#Load and display the view image using Pillow
        self.view_image = Image.open("C:/Users/danie/Downloads/fruit-transparent-background.png")
#This resizes the image to 500 x 300 pixels
        self.view_image_resized = self.view_image.resize((500,300))
        self.view_photo = ImageTk.PhotoImage(self.view_image_resized)
        self.view_image_label = tk.Label(self.new_window, image=self.view_photo)
        self.view_image_label.pack(pady=5)

#Display the list
        tk.Label(self.new_window, text="Your Grocery List:", font=("Open Sans", 14, "bold")).pack(pady=10)
        for item in self.grocery_list:
            tk.Label(self.new_window, text=item).pack()

#Close Button
#Closes the window when clicked
        close_button = tk.Button(self.new_window, text="Close", command=self.new_window.destroy)
        close_button.pack(pady=5)

#Open a new window titled "Remove item"
    def open_remove_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Remove Item")

#Entry Box
#Allows the user to enter the item name to remove
        tk.Label(self.new_window, text="Enter Item Name to Remove:").pack(pady=5)
        self.item_entry_remove = tk.Entry(self.new_window, width=30)
        self.item_entry_remove.pack(pady=5)

#Remove Button
#Recalls the remove_item method when clicked
        remove_button = tk.Button(self.new_window, text="Remove", command=self.remove_item)
        remove_button.pack(pady=5)

#Validates the inputs from "add Item" window
#Displays a success or error
    def add_item(self):
        item = self.item_entry.get().strip()
        if not item:
            messagebox.showwarning("Input Error", "Please enter a valid item!")
            return
        if not item.isalpha():
            messagebox.showwarning("Input Error", "Item name must be alphabetic!")
            return
        self.grocery_list.append(item)
        messagebox.showinfo("Success", f"'{item}' has been added to your grocery list!")
        self.new_window.destroy()
#Validates the inputs from "remove item" window
#Displays an error or success
    def remove_item(self):
        item = self.item_entry_remove.get().strip()
        if not item:
            messagebox.showwarning("Input Error", "Please enter a valid item!")
            return
        if item not in self.grocery_list:
            messagebox.showwarning("Input Error", f"'{item}' is not in the grocery list!")
            return
        self.grocery_list.remove(item)
        messagebox.showinfo("Success", f"'{item}' has been removed from your grocery list!")
        self.new_window.destroy()

# Run the program
if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryListManager(root)
    root.mainloop()
