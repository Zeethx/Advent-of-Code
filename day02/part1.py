from os import getcwd

with open(f'{getcwd()}\day02\hbedi.txt', 'r') as file:
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

print(sum([getScore(elf, user) for elf, user in guide]))



