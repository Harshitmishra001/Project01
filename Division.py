# This function adds two numbers
def divide(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Division by zero not allowed"

