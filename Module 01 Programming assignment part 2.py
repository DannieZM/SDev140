def meal_total():
   
    ''' user inputs meal amount'''
meal_purchase = float(input("Enter the amount charge for the food: $"))
    
""" calculate tip and tax"""
meal_tip = 0.18
    
tip_amount = meal_purchase * meal_tip

meal_tax = .07

tax_amount = meal_purchase * meal_tax
   
total_meal = meal_purchase + tip_amount + tax_amount

print(f"Amount of food purchased: ${meal_purchase:.2f}")

print(f"Tip (18%): ${tip_amount:.2f}")

print(f"Tax (7%): ${tax_amount:.2f}")

print(f"Total Amount with tip and tax: ${total_meal}")

