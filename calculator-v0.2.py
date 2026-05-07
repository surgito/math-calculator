history = []

def clean(number0):
    if number0 == int(number0):
        return int(number0)
    else:
        return number0

def get_number(word):
    while True:
        user_input = input(f"Please enter the {word} the number: ")
        try:
            return float(user_input)
        except:
            print("Please enter a valid number!")
while True:
    while True:
        number1 = get_number("first")
        number2 = get_number("second")
        
        operation = input("Which operation? (+, -, *, /): ")
        if operation == "+":
            print("Result: ", clean(number1) + clean(number2))
            history.append(f"{clean(number1)} + {clean(number2)} = {clean(number1 + number2)}")
            break
        elif operation == "-":
            print("Result: ", clean(number1) - clean(number2))
            history.append(f"{clean(number1)} - {clean(number2)} = {clean(number1 - number2)}")
            break
        elif operation == "*":
            print("Result: ", clean(number1) * clean(number2))
            history.append(f"{clean(number1)} * {clean(number2)} = {clean(number1 * number2)}") 
            break
        elif operation == "/":
            if number2 != 0:
                print("Result:", clean(number1) / clean(number2))
                history.append(f"{clean(number1)} / {clean(number2)} = {clean(number1 / number2)}") 
            else:
                print("Error: Cannot divide by zero.")
            break
        else:
            print("Invalid operation.")
            
    while True:
        answer = input("Would you like another operation? (Y/n):")
        if answer.lower() in ("y","yes",""):
            print("")
            break
        elif answer.lower() in ("n","no"):
            print("") 
        else:
            print("")
            print("Please respond with Yes(y) or No(n) only!")
            print("")
            continue

        while True:
            history_answer = input("Would you like to see the calculation history?(Y/n): ")
            if history_answer.lower() in ("y","yes",""):
                for operation in history:
                    print("")
                    print(operation)
                print("")
                exit()
            elif history_answer.lower() in ("no","n"):
                print("Bye!")
                exit()
            else:
                print("")
                print("Please respond with Yes(y) or No(n) only!")
                print("")
                continue
        
        
            