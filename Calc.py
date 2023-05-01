# This function adds and subtracts two numbers 
import Add
import Sub

# This is to present a menu to the user
print("Select operation.")
print("a.Addition")
print("b.Subtract")

while True:
    # take input from the user
    choice = input("Enter choice(a/b): ")
    
    # check if choice is one of the two options
    if choice in ('a', 'b'):
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

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")



