import time

f = open("map.txt", "r")

maze = []
for i in range(10):
    maze.append(f.readline())
    maze[i] = maze[i].replace("\n", "")
    maze[i] = maze[i].replace("K", "0")
    maze[i] = maze[i].replace("S", "#")
    # maze[i] = list(maze[i])

print("\n".join(maze))

path = 0
k = 0

while path == 0:
    for i in range(10):
        for j in range(10):
            if maze[i][j] == chr(48+k):
                # left
                try:
                    if maze[i-1][j] == "#":
                        path = k
                    if maze[i-1][j] == " ":
                        maze[i-1] = maze[i-1][:j] + chr(49+k) + maze[i-1][j+1:]
                except IndexError: print()

                # right
                try:
                    if maze[i+1][j] == "#":
                        path = k
                    if maze[i+1][j] == " ":
                        maze[i+1] = maze[i+1][:j] + chr(49+k) + maze[i+1][j+1:]
                except IndexError: print()

                # up
                try:
                    if maze[i][j-1] == "#":
                        path = k
                    if maze[i][j-1] == " ":
                        maze[i] = maze[i][:j-1] + chr(49+k) + maze[i][j:]
                except IndexError: print()

                # down
                try:
                    if maze[i][j+1] == "#":
                        path = k
                    if maze[i][j+1] == " ":
                        maze[i] = maze[i][:j+1] + chr(49+k) + maze[i][j+2:]
                except IndexError: print()

    for l in range(7): print()
    print("\n".join(maze))
    for l in range(7): print()
    # time.sleep(0.5)
    k+=1

print(path)

# robot movement
x=0
y=0

for i in range(10):
    for j in range(10):
        if maze[i][j] == '#':
            x=i
            y=j

for k in range(path+1):
    # left or up
    try:
        if maze[x-1][y] == chr(48+path-k):
            maze[x-1] = maze[x-1][:y] + "#" + maze[x-1][y+1:]
            x=x-1
            y=y
    except IndexError: print()

    # right or down
    try:
        if maze[x+1][y] == chr(48+path-k):
            maze[x+1] = maze[x+1][:y] + "#" + maze[x+1][y+1:]
            x=x+1
            y=y
    except IndexError: print()

    # up
    try:
        if maze[x][y-1] == chr(48+path-k):
            maze[x] = maze[x][:y-1] + "#" + maze[x][y:]
            x=x
            y=y-1
    except IndexError: print()

    # down
    try:
        if maze[x][y+1] == chr(48+path-k):
            maze[x] = maze[x][:y+1] + "#" + maze[x+1][y+2:]
            x=x
            y=y+1
    except IndexError: print()

    for l in range(5): print()
    print("\n".join(maze))
    for l in range(5): print()
    time.sleep(0.5)


# HAS SOME BUG