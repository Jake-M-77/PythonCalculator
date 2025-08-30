import os

print("Hello World!")


while True:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("\n To exit use CTRL + C")
    try:
        answer = 0
        num1 = float(input("Please enter the first number: "))
        operator = input("Please enter operator (+/-/%/*): ")
        num2 = float(input("Please enter your second number: "))

        if operator == "+":
            answer = num1 + num2
        elif operator == "-":
            answer = num1 - num2
        elif operator == "*":
            answer = num1 * num2
        elif operator == "/":
            answer = num1 / num2
        else:
            print("Not a valid operator!")
            
        print(f"Answer: {answer}")

        restart = input("Do you want to continue? (Y/N): ")
        restart = restart.upper()
        if restart == "Y":
            continue
        else:
            break

    except ValueError:
        print("Invalid format!")

    except ZeroDivisionError:
        print("Cannot divide by zero!")