from os import getcwd

with open(f'{getcwd()}\day03\input.txt', 'r') as file:
    rucksack = file.read().splitlines()

def lettersToPriority():
    priorities = {}
    for i in range(1, 27):
        priorities[chr(i+96)] = i
        priorities[chr(i+64)] = i+26
    return priorities

priorities = lettersToPriority()

def getTotalPriority(rucksack):
    sum = 0
    for sacks in rucksack:
        result = ', '.join(set(sacks[:len(sacks)//2]).intersection(set(sacks[len(sacks)//2:])))
        sum += priorities[result]

    return sum

print(getTotalPriority(rucksack))