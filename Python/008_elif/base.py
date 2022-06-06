a = int(input("Please enter the first number: "))
b = input("Please enter an operation: ")
c = int(input("Please enter the second number: "))
d = int(a+c)
e = int(a-c)
f = int(a*c)
g = int(a/c)
if b == "+":
    print(str(a) + " + " + str(c) + " = " + str(d))
elif b == "-":
    print(str(a) + " - " + str(c) + " = " + str(e))
elif b == "*":
    print(str(a) + " * " + str(c) + " = " + str(f))
else:
    print(str(a) + " / " + str(c) + " = " + str(g))