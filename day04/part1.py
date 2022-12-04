from os import getcwd

with open(f'{getcwd()}\day04\input.txt', 'r') as file:
    pairs = file.read().splitlines()

pairs = [pair.split(',') for pair in pairs]

def getPairs(pairs):
    count = 0
    for pair in pairs:
        p1,p2 = map(int, pair[0].split('-'))
        p3,p4 = map(int, pair[1].split('-'))
        if (p1 <= p3 and p2 >= p4) or (p3 <= p1 and p4 >= p2):
            count += 1

    return count

print(getPairs(pairs))