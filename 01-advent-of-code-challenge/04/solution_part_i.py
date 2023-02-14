import sys

pairs = 0
for line in sys.stdin:
    left_elf = line.split(',')[0].split('-')
    right_elf = line.split(',')[1].split('-')

    if(left_elf[0] <= right_elf[0] and left_elf[1] >= right_elf[0]):
        pairs += 1
    elif(right_elf[0] <= left_elf[0]  and right_elf[1] >= left_elf[0]):
        pairs += 1

print(pairs)