#Step 1: collect the necessary inputs: principal, apr, years
#Step 2: Calculate monthly payment 
#Step 3: show the monthly payment to the user

principal = float(input("Enter the loan amount: "))
apr = float(input("Enter the annual interest rate: "))
years = int(input("Enter the number of years: "))

monthly_rate = apr / 1200
months = years * 12
monthly_payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)

print("The monthly payment is: $%.2f" % monthly_payment)
 