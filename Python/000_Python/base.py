import random

complist = ["is amazing!", "is wonderful!", "is kind!", "is the best!", "is lovely!", "is great!"]
peoplelist = ["Your Mom ", "Your Dad ", "Your Family ", "Your Dog ", "Angel ", "The One ", "Your Friend "]

a = peoplelist[random.randrange(7)] 
b = complist[random.randrange(6)]
print(a + b)

