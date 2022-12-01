from os import getcwd

def topThreeElves():
    with open(f'{getcwd()}\day01\input.txt', 'r') as file:
        elves = map(lambda x: x.splitlines(), file.read().split('\n\n'))
        elves = list(map(lambda x: sum(list(map(int, x))), elves))

        return(sum([elves.pop(elves.index(max(elves))) for _ in range(3)]))
    
print("Sum of three elves with most calories:", topThreeElves())