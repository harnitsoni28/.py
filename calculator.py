# Calculator in python +,-,*,/

def calculator():
    operations = {
        '1': lambda x, y: x + y,
        '2': lambda x, y: x - y,
        '3': lambda x, y: x * y,
        '4': lambda x, y: "Error! Division by zero." if y == 0 else x / y
    }

    print("Welcome to the Lambda Calculator!")

    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("Enter 'q' to quit.")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in operations:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = operations[choice](num1, num2)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid operation.")

calculator()
