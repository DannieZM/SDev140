"""
Author: Daniela Zamorano-Martinez
Date: 11/25/24
Assignment: Module 05 Programming Assignment
Descrip: Create a sales tax report: county, state, and total based on the users total sale.
"""

def calculatesales_tax():
    try:
#Ask the user to enter the total sales

        total_sales = float(input("Enter the total sales for the month: $"))
        
#Tax rates

        STATE_TAX_RATE = 0.05  # 5%
        COUNTY_TAX_RATE = 0.025  # 2.5%
        
#Calculate taxes
        county_tax = total_sales * COUNTY_TAX_RATE
        state_tax = total_sales * STATE_TAX_RATE
        total_tax = county_tax + state_tax
        
#Outputs
        print(f"\nSales Tax Report:")
        print(f"Total Sales: ${total_sales:,.2f}")
        print(f"County Sales Tax: ${county_tax:,.2f}")
        print(f"State Sales Tax: ${state_tax:,.2f}")
        print(f"Total Sales Tax: ${total_tax:,.2f}")

#In case user enters a non numeric        
    except ValueError:
        print("Invalid input. Please enter a numeric value for total sales.")


if __name__ == "__main__":
    calculatesales_tax()
