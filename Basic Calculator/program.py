#Step 1: define the functiones needed for the calculator: add, sub, mul, div
#Step 2: print options to the user 
#Step 3: take input from the user
#Step 4: perform the operation by calling functions
#Step 5: while loop to keep the program running until user chooses to exit

while True:
    operation = input("Enter the operation you want to perform. Your options are add, sub, mul, and div: ")

    def add(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mul(a, b):
        return a * b
    def div(a, b):
        return a / b

    if operation == 'add' or operation == 'Add':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(add(num1, num2) + "\n")
    elif operation == 'sub':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(sub(num1, num2) + "\n")
    elif operation == 'mul':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(mul(num1, num2) + "\n")
    elif operation == 'div':
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(div(num1, num2) + "\n")
    elif operation == 'exit':
        print("Goodbye!")
        quit()
    else:
        print("Invalid operation")

