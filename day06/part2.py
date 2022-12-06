from os import getcwd

with open(f'{getcwd()}\day06\input.txt', 'r') as file:
    buffer = file.read()

def findMarker(buffer):
    left, right = 0, 14

    while(right<=len(buffer)):
        if (len(set(buffer[left:right])) == 14):
            return right
        else:
            left+=1
            right+=1

print(findMarker(buffer))