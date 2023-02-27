import sys

first = ''
second = ''
third = ''
fourth = ''
count = 0

for line in sys.stdin:
  for char in line:
    if first == '':
      first = char
      count += 1
      continue
    elif second == '':
      second = char
      count += 1
      continue
    elif third == '':
      third = char
      count += 1
      continue
    elif fourth == '':
      fourth = char
      count += 1
      continue

    if(first == second):
      first = ''
      second = ''
      third = ''
      fourth = ''
      count += 1
      continue
    elif(first == third):
      first = ''
      second = ''
      third = ''
      fourth = ''
      count += 1
      continue
    elif(first == fourth):
      first = ''
      second = ''
      third = ''
      fourth = ''
      count += 1
      continue
    elif(second == third):
      first = ''
      second = ''
      third = ''
      fourth = ''
      count += 1
      continue
    elif(second == fourth):
      first = ''
      second = ''
      third = ''
      fourth = ''
      count += 1
      continue
    elif(third == fourth):
      first = ''
      second = ''
      third = ''
      fourth = ''
      count += 1
      continue
    else:
      break

print(count)
