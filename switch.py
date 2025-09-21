x = int(input("Enter a number : "))

match x:
    case 0:
        print("you entered zero number")
    case 1:
        print("you enter 1 number")
    case _ if x<0:
        print("you enter negetive number")
    case _:
        print("you entered",x,"number")