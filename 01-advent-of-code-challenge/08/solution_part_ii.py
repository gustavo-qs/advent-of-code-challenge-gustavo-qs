with open("sample.in") as file:
    trees = [row.strip() for row in file.readlines()]

num_row = len(trees)
num_col = len(trees[0])

result = []

for row in range(1, num_row - 1):
  for col in range(1, num_col - 1):
    tree_height = int(trees[row][col]) 

    left = [int(trees[row][col - i]) for i in range(1, col + 1)]
    right = [int(trees[row][col + i]) for i in range(1, num_col - col)]
    up = [int(trees[row - i][col]) for i in range(1, row + 1)]
    down = [int(trees[row + i][col]) for i in range(1, num_row - row)]

    score = 1
    for lst in (left, right, up, down):
      tracker = 0
      for i, height in enumerate(lst):
          if height < tree_height:
            tracker = i + 1
          else:
            tracker = i + 1
            break

      score *= tracker

    result.append(score)

print(max(result))
