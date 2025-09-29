def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    else:
        return a / b

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def calculate_percentage(total, part):
    if total == 0:
        return None
    else:
        return (part / total) * 100

while True:
    print("\nChoose what you want to do:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Check Even or Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            result = divide(num1, num2)
            if result is None:
                print("Cannot divide by zero!")
            else:
                print("Result:", result)

    elif choice == "5":
        num = int(input("Enter an integer: "))
        print(f"{num} is", check_even_odd(num))

    elif choice == "6":
        total = float(input("Enter total value: "))
        part = float(input("Enter part value: "))
        result = calculate_percentage(total, part)
        if result is None:
            print("Total cannot be zero!")
        else:
            print("Percentage:", result, "%")

    else:
        print("Please enter a valid choice (1-7).")
