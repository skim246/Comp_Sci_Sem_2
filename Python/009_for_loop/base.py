a = int(input("Please enter line length: "))
b = input("Do you want a horizontal or vertical line: ")
if b == "vertical":
    for a in range (1,a+1):
        print("*")
else:
    for a in range (1,a+1):
        print("*", end=" ")
    