from os import getcwd

with open(f'{getcwd()}\day02\input.txt', 'r') as file:
    guide = list(map(lambda x: x.split(" "), file.read().split('\n')))

points = 0

plusPoints = {'X': 1, 'Y': 2, 'Z': 3}

# needs to be redone

for strat in guide:
    elf = strat[0]
    user = strat[1]
    if(strat[0] == 'A'):
        if(user == 'X'):
            points = points + 3
        elif(user == 'Y'):
            points = points + 3 + 1
        else:
            points = points + 6 + 2
    elif(elf == 'B'):
        if(user == 'X'):
            points = points + 1
        elif(user == 'Y'):
            points = points + 3 + 2
        else:
            points = points + 6 + 3
    else:
        if(user == 'X'):
            points = points + 2
        elif(user == 'Y'):
            points = points + 3 + 3
        else:
            points = points + 6 + 1

print(points)



