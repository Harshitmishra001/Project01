# This is complete calculator
import Add
import Sub
import Multiplication
import Division

# This is to present a menu to the user
print("Select operation.")
print("a.Addition")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(a/b/c/d): ")
    
    # check if choice is one of the four options
    if choice in ('a', 'b','c','d'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 'a':
            print(num1, "+", num2, "=", Add.add(num1, num2))

        elif choice == 'b':
            print(num1, "-", num2, "=", Sub.subtract(num1, num2))

        elif choice == 'c':
            print(num1, "*", num2, "=", Multiplication.multiply(num1, num2))

        elif choice == 'd':
            print(num1, "/", num2, "=", Division.divide(num1, num2))


        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")



