from os import getcwd

with open(f'{getcwd()}\day02\input.txt', 'r') as file:
    guide = list(map(lambda x: x.split(" "), file.read().split('\n')))

points = 0
plusPoints = {'X': 1, 'Y': 2, 'Z': 3}

def getScore(elf, user):
    if(elf == 'A'):
        return 3 + plusPoints[user] if user == 'X' else 6 + plusPoints[user] if user == 'Y' else  plusPoints[user] 
    elif(elf == 'B'):
        return plusPoints[user] if user == 'X' else 3 + plusPoints[user] if user == 'Y' else 6 + plusPoints[user]
    else:
        return 6 + plusPoints[user] if user == 'X' else plusPoints[user] if user == 'Y' else 3+ plusPoints[user]

for strat in guide:
    points = points + getScore(strat[0], strat[1])

print(points)

