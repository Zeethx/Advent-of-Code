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
    batches = [rucksack[sack:sack+3] for sack in range(0, len(rucksack), 3)]
    answer = [priorities[', '.join(set.intersection(*map(set, sack)))] for sack in batches]
    return sum(answer)


print(getTotalPriority(rucksack))