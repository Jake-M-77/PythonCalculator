import os
import time

print("Hello World!")




class Calculator:

    def __init__(self):
        """Initialise attributes"""
        self.calculation_history = []

    def clear_console(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def calculate_answer(self,num1,num2,operator):
        if operator == "+":
            return  num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 / num2
        elif operator == "%":
            return num1 % num2
        elif operator == "**":
            return num1 ** num2
        elif operator == "//":
            return num1 // num2
        else:
            print("Not a valid operator!")

    def run_calculator(self):
        try:
            self.clear_console()

            print("\n To exit use CTRL + C")

            if len(self.calculation_history) > 0:
                print(f"Calculation History:")
                for calculation in self.calculation_history:
                    print(calculation)
            else:
                print(f"No previous calculations at the moment!")

            print("\n")

            answer = 0
            num1 = float(input("Please enter the first number: "))
            operator = input("Please enter operator (+ - / *  % ** // ): ")
            num2 = float(input("Please enter your second number: "))

            answer = self.calculate_answer(num1, num2, operator)

            if answer is None:
                time.sleep(2)
                self.run_calculator()
                return


            print(f"Answer {answer}")

            if len(self.calculation_history) > 6:
                self.calculation_history.pop(0)

            self.calculation_history.append(answer)

            restart = input("Do you want to continue? (Y/N): ")
            restart = restart.upper()
            if restart == "Y":
                self.run_calculator()
            else:
                print("Closing program!")

        except ValueError:
            print("Invalid Format!")
            time.sleep(2)
            self.run_calculator()
        except ZeroDivisionError:
            print("Cannot divide by zero")
            time.sleep(2)
            self.run_calculator()


calc = Calculator()

calc.run_calculator()