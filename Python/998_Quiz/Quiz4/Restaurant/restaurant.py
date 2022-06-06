import random

restaurants = ["In-n-Out", "McDonalds", "Habit"]
InnOut = ["Hamburger","Cheeseburger","Double Double"]
McDonalds = ["Chicken Nuggets","Big Mac","French Fries"]
Habit = ["Burger","Chicken Sandwich", "Milkshake"]

restaurants = restaurants[random.randrange(0,3)]
print("The restaurant is " + restaurants)

if restaurants =="In-n-Out":
    item = InnOut[random.randrange(0,3)]
    print("The menu item is " + item)
    
elif restaurants =="McDonalds":
    item = McDonalds[random.randrange(0,3)]
    print("The menu item is " + item)
    
elif restaurants =="Habit":
    item = Habit[random.randrange(0,3)]
    print("The menu item is " + item)
