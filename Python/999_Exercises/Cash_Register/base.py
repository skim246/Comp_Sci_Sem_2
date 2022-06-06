items = int(input("How many items are you purchasing? "))

total = 0
for i in range(0,items):
    a = input("What item are you purchasing? ")
    b = float(input("How much is the item? "))
    print("Thanks for buying " + a + "!")
    print("____________________________________")
    total = total + b
    

print("Your total is: " + str(total))
