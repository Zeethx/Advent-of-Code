from os import getcwd

def getMaxCalories():
    with open(f'{getcwd()}\day01\input.txt', 'r') as file:
        elves = map(lambda x: x.splitlines(), file.read().split('\n\n'))
        elves = list(map(lambda x: sum(list(map(int, x))), elves))

    return(max(elves))

    
print("Maximum calories with an Elf:", getMaxCalories()) #74394
