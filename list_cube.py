def cube (x):
    return x*x*x

list=[2,5,4,7,3,2]

new_list=[]

for item in list:
    new_list.append(cube(item))

print(new_list)