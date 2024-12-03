"""
Author: Daniela Z.M
Assignment: Final project
Date: 12/2/24

"""



'''
Notes:
Add a remove item button
resize windows
figure out how to add images
add category button
*maybe add a save button and implication*

DOUBLE check requiements

*maybe add color*
'''


import tkinter as tk
from tkinter import messagebox

#Main Application Class
class GroceryListManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery List Manager")
        
#Initialize grocery list
        self.grocery_list = []

#Main Window
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
#POSSIBILY RESIZE#
#Title Label
        self.title_label = tk.Label(self.main_frame, text="Grocery List Manager", font=("Arial", 16), padx=20, pady=20)
        self.title_label.pack()


 #Add Item Button
        self.add_item_button = tk.Button(self.main_frame, text="Add Item", command=self.open_add_window)
        self.add_item_button.pack(pady=5)

#View List Button
        self.view_list_button = tk.Button(self.main_frame, text="View Grocery List", command=self.open_view_window)
        self.view_list_button.pack(pady=5)

#Exit Button
        self.exit_button = tk.Button(self.main_frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def open_add_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Add Item")

#Entry Box
        tk.Label(self.new_window, text="Enter Item Name:").pack(pady=5)
        self.item_entry = tk.Entry(self.new_window, width=30)
        self.item_entry.pack(pady=5)

#Add Button
        add_button = tk.Button(self.new_window, text="Add", command=self.add_item)
        add_button.pack(pady=5)

    def open_view_window(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Grocery List")

#Display the list
        tk.Label(self.new_window, text="Your Grocery List:").pack(pady=10)
        for item in self.grocery_list:
            tk.Label(self.new_window, text=item).pack()

#Close Button
        close_button = tk.Button(self.new_window, text="Close", command=self.new_window.destroy)
        close_button.pack(pady=5)

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


#Run the program
if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryListManager(root)
    root.mainloop()
