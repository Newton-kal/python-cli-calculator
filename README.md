# Simple Command-Line Calculator

A basic interactive calculator built in Python for performing fundamental arithmetic operations (+, -, *, /) via the command line. This project highlights user input handling, conditional logic, and essential error management.

---

## Features

* Performs addition, subtraction, multiplication, and division.
* Handles non-numeric input gracefully.
* Prevents division by zero.
* Allows multiple calculations or an option to exit.

---

## Technologies Used

* Python 3.x

---

## How to Run

1.  **Clone the repository (if you're running it locally):**
    ```bash
    git clone [https://github.com/Newton-Kal/python-cli-calculator.git](https://github.com/Newton-Kal/python-cli-calculator.git)
    cd python-cli-calculator
    ```
2.  **Run the calculator:**
    ```bash
    python calculator.py
    ```

---

## Example Usage

   Welcome to the Command-Line Calculator!
   Operations: +, -, *, /
   Type 'exit' to quit.
   Enter first number (or 'exit'): 10
   Enter operator (+, -, *, /): +
   Enter second number: 5
   Result: 15.0
   Enter first number (or 'exit'): hello
   Error: Invalid number input. Please enter numerical values.
   Enter first number (or 'exit'): 7
   Enter operator (+, -, *, /): /
   Enter second number: 0
   Result: Error: Cannot divide by zero!
   Enter first number (or 'exit'): exit
   Exiting calculator. Goodbye!
   
---

## Future Enhancements (Ideas for continued development)

* Add more mathematical operations (e.g., modulo, power).
* Implement a history feature to review past calculations.
* Improve user interface with clear prompts and formatting.

