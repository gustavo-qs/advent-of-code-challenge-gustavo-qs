import sys

def message_start(datastream):
    buffer = ''
    for i, char in enumerate(datastream):
        buffer += char
        if len(buffer) > 14:
            buffer = buffer[1:]
        if len(buffer) == 14 and len(set(buffer)) == 14:
            return i + 1
    return -1  

stream = sys.stdin.readlines()

start = message_start(stream[0])
print(start)
