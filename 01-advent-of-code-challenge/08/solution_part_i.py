with open("sample.in") as file:
    data = [row.strip() for row in file.readlines()]

num_rows = len(data)
num_columns = len(data[0])

edges = (num_rows * 2) + ((num_columns - 2) * 2)
total = edges

for row in range(1, num_rows - 1):
  for col in range(1, num_columns - 1):
    tree_height = int(data[row][col]) 

    left = [int(data[row][col - i]) for i in range(1, col + 1)]
    right = [int(data[row][col + i]) for i in range(1, num_columns - col)]
    up = [int(data[row - i][col]) for i in range(1, row + 1)]
    down = [int(data[row + i][col]) for i in range(1, num_rows - row)]

    if max(left) < tree_height or max(right) < tree_height or max(up) < tree_height or max(down) < tree_height:
      total += 1

print(total)