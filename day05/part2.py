from os import getcwd

with open(f'{getcwd()}\day05\input.txt', 'r') as file:
    stack = file.read()

stack, moves = stack.split('\n\n')
stack = stack.splitlines()