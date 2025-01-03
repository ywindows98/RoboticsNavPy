# f = open("map.txt", "r")
#
# maze = []
# for i in range(10):
#     maze.append(f.readline())
#     maze[i] = maze[i].replace("\n", "")
#     maze[i] = maze[i].replace("K", "0")
#     maze[i] = maze[i].replace("S", "#")
#
# print("\n".join(maze))

f = open("map.txt", "r")

maze = []
for i in range(10):
    maze.append(f.readline())
    maze[i] = maze[i].replace("\n", "")
    maze[i] = maze[i].replace("F", chr(35)) # Finish
    maze[i] = maze[i].replace("S", chr(36)) # Start

maze2 = []
for i in range(10):
    maze2.append([' ' for x in range(10)])
    for j in range(10):
        maze2[i][j] = maze[i][j]

print(maze2)
for i in range(10):
    print("".join(maze2[i]))
