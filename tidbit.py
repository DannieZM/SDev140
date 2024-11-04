
def credit_plan(purchase_price):
### Format is important here: since some information was "out" of the loop" try organzing idents as well as double check while loops for identing###     

#Constants
    annual_rate = 0.12
    monthly_rate = annual_rate/12
    downpayment_rate = .10
    TABLEFORMATSTRING = "%2d%15.2f%15.2f%17.2f%17.2f%17.2f"
        
# Initialize Variables
    monthly_Payment = 0.05 * float(purchase_price)
    month = 1
    balance = float(purchase_price) - (float(purchase_price)* downpayment_rate)

#Output
    print("Month Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

#Loop
    while balance > 0:
        if monthly_Payment > balance:
                monthly_Payment = balance
                interest = 0
        else:
                interest = balance * monthly_rate
            
#calculate 
        principal = monthly_Payment - interest
        remaining = balance - monthly_Payment
#output data in order
        print(TABLEFORMATSTRING % (month, balance, interest, principal, monthly_Payment, remaining))

#update payment plan 
        balance = remaining
        month += 1

#input data from user
purchase_price = float(input("Enter the purchase price : $"))
credit_plan(purchase_price)
