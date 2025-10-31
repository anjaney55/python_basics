
# #to repplace Java into Phythod

# with open("practice.txt","r+") as f :
#     data = f.read()
#     print(data)

# new_data = data.replace("Java","Python")

# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)


# #to find the word

# word = "learning"

# with open("practice.txt","r") as f:
#     new = f.read()
#     if(new.find(word) != -1):
#         print("Found")
#     else:
#         print("not found")


#using function 

def chec_for_word():
    word = "xlearn"

    with open("practice.txt","r") as f:
        new = f.read()
        if(new.find(word) != -1):
            print("Found")
        else:
            print("not found")

chec_for_word()     