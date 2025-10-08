import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp1 = int(time.strftime('%H'))
print(timestamp1)

timestamp = time.strftime('%M')
print(timestamp)

timestamp = time.strftime('%S')
print(timestamp)

if timestamp1>=0 and timestamp1<12:
    print("good morning")
elif timestamp1>=12 and timestamp<16:
    print("Goood Afternoon")
elif timestamp>=16 and timestamp<20:
    print("Good Evening")
else:
    print("Good Night")
    