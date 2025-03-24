import logging

# Set up logging to save calculations to a file
logging.basicConfig(filename='calculator_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Define the functions for the calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

# Display the available operations
def display_operations():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate (x^y)")
    print("6. Modulus (x % y)")
    print("7. View History")
    print("8. Clear History")

# Function to display the history of calculations
def view_history():
    try:
        with open("calculator_log.txt", "r") as file:
            print("\nCalculation History:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No history available.")
        
# Function to clear the history of calculations
def clear_history():
    try:
        with open("calculator_log.txt", "w") as file:
            file.truncate(0)
        print("History cleared.")
    except Exception as e:
        print(f"Error clearing history: {e}")

# Main function to run the calculator
def calculator():
    while True:
        display_operations()
        
        try:
            choice = input("\nEnter choice (1/2/3/4/5/6/7/8 or 'q' to quit): ")
            
            if choice == 'q':
                print("Exiting the calculator. Goodbye!")
                break
            
            if choice == '7':  # View history
                view_history()
                continue
            elif choice == '8':  # Clear history
                clear_history()
                continue
            elif choice in ['1', '2', '3', '4', '5', '6']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                    operation = f"{num1} + {num2} = {result}"
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = f"{num1} - {num2} = {result}"
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = f"{num1} * {num2} = {result}"
                elif choice == '4':
                    result = divide(num1, num2)
                    operation = f"{num1} / {num2} = {result}"
                elif choice == '5':
                    result = exponentiate(num1, num2)
                    operation = f"{num1} ^ {num2} = {result}"
                elif choice == '6':
                    result = modulus(num1, num2)
                    operation = f"{num1} % {num2} = {result}"

                print(operation)
                logging.info(operation)  # Log the calculation

            else:
                print("Invalid input! Please enter a number between 1 and 8 or 'q' to quit.")
        
        except ValueError:
            print("Invalid input! Please enter numeric values for the numbers.")

# Run the calculator program
if __name__ == "__main__":
    calculator()
