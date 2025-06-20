# calculator.py

# A Simple Command-Line Calculator in Python.

# This script creates an interactive calculator that performs basic arithmetic operations
# (addition, subtraction, multiplication, and division) directly in your terminal.
# It's designed for simplicity, demonstrating fundamental Python concepts like
# user input, conditional logic, functions, and essential error handling.

# The goal is to provide a clear, easy-to-understand example of a functional
# command-line application.

# Function Definitions for Arithmetic Operations 

def add(num1, num2):
    """Adds two numbers and returns their sum."""
    return num1 + num2

def subtract(num1, num2):
    """Subtracts the second number from the first and returns the difference."""
    return num1 - num2

def multiply(num1, num2):
    """Multiplies two numbers and returns their product."""
    return num1 * num2

def divide(num1, num2):
    """
    Divides the first number by the second.
    Handles division by zero to prevent errors.
    """
    if num2 == 0:
        # Return a string message to indicate an error, rather than crashing
        return "Error: Cannot divide by zero!"
    return num1 / num2

# Main Calculator Logic

def run_calculator():
    """
    Manages the main flow of the calculator application.
    It takes user input, performs calculations, and handles errors.
    """
    print("Welcome to the Command-Line Calculator!")
    print("Operations: +, -, *, /")
    print("Type 'exit' to quit.")

    while True: # Loop indefinitely until the user decides to exit
        try:
            # Get User Input for Numbers 
            num1_input = input("Enter first number (or 'exit'): ")
            if num1_input.lower() == 'exit':
                print("Exiting calculator. Goodbye!")
                break # Break out of the while loop to end the program

            num1 = float(num1_input) # Convert input string to a floating-point number

            operator = input("Enter operator (+, -, *, /): ")

            num2_input = input("Enter second number: ")
            num2 = float(num2_input) # Convert input string to a floating-point number

            # Perform Calculation Based on Operator 
            result = None # Initialize result to None, will be set by the operation

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Error: Invalid operator. Please use +, -, *, or /.")
                continue # Skip to the next iteration of the loop to ask for input again

            # Display Result
            if result is not None: # Only print if a valid operation was performed
                print(f"Result: {result}")

        except ValueError:
            # Catch errors if the user enters text instead of numbers
            print("Error: Invalid number input. Please enter numerical values.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

        print("-" * 30) # Print a separator for readability between calculations

# Entry Point of the Program
if __name__ == "__main__":
    # This ensures that run_calculator() is called only when the script is executed directly,
    # not when it's imported as a module into another script.
    run_calculator()
          
