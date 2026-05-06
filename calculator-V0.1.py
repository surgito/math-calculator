while True:
    while True:
        firstn = input("Please enter the first number: ")
        try:
            number1 = float(firstn)
            break
        except:
            print("Enter a number!")
                
    while True:
        secondn = input("Please enter the second number: ")
        try:
            number2 = float(secondn)
            break
        except:
            print("Enter a number!")
                
    operation = input("Which operation?(+,-,*,/): ")
    if operation == "+":
        print("Result: ", number1 + number2)
    elif operation == "-":
        print("Result: ", number1 - number2)
    elif operation == "*":
        print("Result: ", number1 * number2)
    elif operation == "/":
        if number2 != 0:
            print("Result:", number1 / mumber2)
        else:
            print("Error: Divide by zero.")
    else:
        print("Invalid operation.")
    answer = input("Another operation?(y/n) ")
    if answer == "y":
        print("")
    elif answer == "n":
        break
    else:
        print("Please respond with Yes or NO only!")
        break
            
        
        
            