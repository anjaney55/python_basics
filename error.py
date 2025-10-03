#errorr handling using try and except and expection

a = input("enter the table number : ")

try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")

except Exception as e:  #we can use except only and also we use multiple except according to the errorrs
    print(e)
    print("some errorr")

print("Hello")
print("Hello")
print("Hello")
print("Hello")