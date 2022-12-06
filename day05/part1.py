from os import getcwd

with open(f'{getcwd()}\day05\input.txt', 'r') as file:
    stack = file.read()

stack, moves = stack.split('\n\n')
stack = stack.splitlines()

# [M]                     [N] [Z]    
# [F]             [R] [Z] [C] [C]    
# [C]     [V]     [L] [N] [G] [V]    
# [W]     [L]     [T] [H] [V] [F] [H]
# [T]     [T] [W] [F] [B] [P] [J] [L]
# [D] [L] [H] [J] [C] [G] [S] [R] [M]
# [L] [B] [C] [P] [S] [D] [M] [Q] [P]
# [B] [N] [J] [S] [Z] [W] [F] [W] [R]
#  1   2   3   4   5   6   7   8   9 

def parse_stack(stack):
     pass
