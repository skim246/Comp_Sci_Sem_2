import random
a = int(input("How many random numbers would you like? "))
thislist = ["1","2","3","4","5","6","7","8","9","10"]

print("Your numbers are: ", end="")
for i in range(0,a):
    print(thislist[random.randrange(1,10)], end=", ")