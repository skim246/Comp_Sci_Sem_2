import datetime

peoplelist = []
with open('People.txt') as f:
    for line in f:
        l = line.strip()
        peoplelist.append(1)

complist = []
with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        complist.append(1)

import random
pnum = random.randrange(0,len(peoplelist))
cnum = random.randrange(0,len(complist))

print(peoplelist[pnum] + " " + complist[cnum])


x = datetime.datetime.now()

print()
print("The date and time are:")
print(str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " at " + str(x.hour))

f.close()
