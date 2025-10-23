# Simple Python program: Greeting and factorial calculator

def factorial(n):
    """Return the factorial of a given number."""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 2
        for i in range(2, n + 1):
            result *= i
        return result

# Main program
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the Python demo.")

try:
    number = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {number} is {factorial(number)}.")
except ValueError:
    print("Please enter a valid integer.")
