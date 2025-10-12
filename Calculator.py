def calculator():
    print("Simple calculator")
    print("Operations '+'(Addition), '-'(Substraction), '*'(Multi),'/'(Division)")

    num1 = int(input("Enter a first number : "))
    operator = input("Enter an operator : ")
    num2 = int(input("Enter a second number : "))

    if operator=="+":
        result = num1+num2
        print(f"{num1} +{num2} = {result}")
    elif operator=="-":
        dif = num1-num2
        print(f"{num1} - {num2} = {dif}")
    elif operator=="*":
        mul = num1*num2
        print(f"{num1} * {num2} = {mul}")
    elif operator=="/":
        if num2!=0:
            div = num1/num2
            print(f"{num1} / {num2} = {div}")
        else:
            print("num2 is not to be zero!..")

    else:
        print("invalid operator!...")

calculator()