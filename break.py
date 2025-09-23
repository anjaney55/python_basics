

i = 1

while i<=5 :
    if(i==3):
       break
    print(i) 
    i+=1

print("end of loop")  

n = 1

while n<=5 :
    if(n==3):
       n +=1
       continue  #skip
    print(n) 
    n+=1

print("end of loop")  

num= 1

while num<=15 :
    if(num %2 == 0):
       num+=1
       continue
    print(num) 
    num+=1
