
#find the X item in the given list

num = int(input("ENter the one given list number : "))

nums = [1,4,9,16,25,36,49,64,81,100]

i = 0

while i<len(nums) :
    if(nums[i]==num):
     print("Yes")
    i += 1

print("end of searching")
