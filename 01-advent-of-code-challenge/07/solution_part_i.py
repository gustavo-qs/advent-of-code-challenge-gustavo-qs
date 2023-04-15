import sys

directories = {"/": 0}
current_path = "/"

for command in sys.stdin:
  if command[0] == "$":
    if command[2:4] == "ls":
      pass
    elif command[2:4] == "cd":
      if command[5:6] == "/":
        current_path = "/"
      elif command[5:7] == "..":
        current_path = current_path[0:current_path.rfind("/")]
      else:
        dir_name = command[5:]
        current_path = current_path + "/" + dir_name
        directories.update({current_path: 0})
  elif command[0:3] == "dir":
    pass
  else:
    file_size = int(command[:command.find(" ")])
    dir = current_path
    for _ in range(current_path.count("/")):
      directories[dir] += file_size
      dir = dir[:dir.rfind("/")]

total = 0

for dir in directories:
  if directories[dir] < 100000:
    total += directories[dir]

print(total)