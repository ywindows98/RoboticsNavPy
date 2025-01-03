import time
import random

f = open("map.txt", "r")

maze = []
for i in range(10):
    maze.append(f.readline())
    maze[i] = maze[i].replace("\n", "")
    maze[i] = maze[i].replace("X", chr(38))  # Finish
    maze[i] = maze[i].replace("F", chr(35)) # Finish
    maze[i] = maze[i].replace("S", chr(36)) # Start

maze_matrix = []
for i in range(10):
    maze_matrix.append([' ' for x in range(10)])
    for j in range(10):
        maze_matrix[i][j] = maze[i][j]

# print(maze2)
for i in range(10):
    print("".join(maze_matrix[i]))

start_pos = [0,0]
finish_pos = [0,0]

for i in range(len(maze_matrix)):
    for j in range(len(maze_matrix[0])):
        if maze_matrix[i][j] == chr(36):
            start_pos = [i,j]
        if maze_matrix[i][j] == chr(35):
            finish_pos = [i,j]

print(f"Start: {start_pos}")
print(f"Finish: {finish_pos}")

n_ants = 1
path = 0
ants_pos = [start_pos.copy() for ant in range(n_ants)]

for i in range(5):
    for j in range(n_ants):
        last_pos = ants_pos[j]
        # for k in range(10):
        while ants_pos[j] != finish_pos:
            paths = [0, 0, 0, 0]  # 0 - filled, 1 - free # left, up, right, down
            # up
            try:
                active_char = maze_matrix[ants_pos[j][0]-1][ants_pos[j][1]]
                print(active_char)
                if active_char != '&':
                    if active_char == '$':
                        paths[1] = 0.1
                    elif active_char == ' ':
                        paths[1] = 1
                    else:
                        if ants_pos[j][0]-1 == last_pos[0] and ants_pos[j][1] == last_pos[1]:
                            paths[1] = (ord(active_char)-47) / 10
                        else:
                            paths[1] = ord(active_char) - 47
            except IndexError: print()
            # down
            try:
                active_char = maze_matrix[ants_pos[j][0]+1][ants_pos[j][1]]
                if active_char != '&':
                    if active_char == '$':
                        paths[3] = 0.1
                    elif active_char == ' ':
                        paths[3] = 1
                    else:
                        if ants_pos[j][0]+1 == last_pos[0] and ants_pos[j][1] == last_pos[1]:
                            paths[3] = (ord(active_char)-47) / 10
                        else:
                            paths[3] = ord(active_char) - 47
            except IndexError: print()
            # left
            try:
                active_char = maze_matrix[ants_pos[j][0]][ants_pos[j][1]-1]
                if active_char != '&':
                    if active_char == '$':
                        paths[0] = 0.1
                    elif active_char == ' ':
                        paths[0] = 1
                    else:
                        if ants_pos[j][0] == last_pos[0] and ants_pos[j][1]-1 == last_pos[1]:
                            paths[0] = (ord(active_char)-47) / 10
                        else:
                            paths[0] = ord(active_char)-47

            except IndexError: print()
            # right
            try:
                active_char = maze_matrix[ants_pos[j][0]][ants_pos[j][1]+1]
                if active_char != '&':
                    if active_char == '$':
                        paths[2] = 0.1
                    elif active_char == ' ':
                        paths[2] = 1
                    else:
                        if ants_pos[j][0] == last_pos[0] and ants_pos[j][1]+1 == last_pos[1]:
                            paths[2] = (ord(active_char)-47) / 10
                        else:
                            paths[2] = ord(active_char)-47

            except IndexError: print()
            paths = [float(i) / sum(paths) for i in paths]
            print("Paths: ",  paths)
            probs = [paths[0], sum(paths[0:2]), sum(paths[0:3]), 1]
            print("Probs: ", probs)
            dice = random.random()
            print("Dice: ", dice)
            choice = 0
            if dice< probs[0]:
                choice = [0, -1] # left
            if dice>probs[0] and dice<probs[1]:
                choice = [-1, 0] # up
            if dice>probs[1] and dice<probs[2]:
                choice = [0, 1] # right
            if dice>probs[2]:
                choice = [1, 0] # down
            # print("Choice: ", choice)

            active_char = maze_matrix[ants_pos[j][0]][ants_pos[j][1]]
            if active_char != '$':
                if active_char == ' ':
                    maze_matrix[ants_pos[j][0]][ants_pos[j][1]] = '1'
                else:
                    maze_matrix[ants_pos[j][0]][ants_pos[j][1]] = chr(ord(maze_matrix[ants_pos[j][0]][ants_pos[j][1]])+1)
            last_pos = ants_pos[j].copy()
            ants_pos[j] = [ants_pos[j][0] + choice[0], ants_pos[j][1] + choice[1]]
            print(ants_pos[j])
            for i in range(10):
                print("".join(maze_matrix[i]))

#
# while path == 0:
#     for i in range(10):
#         for j in range(10):
#             if maze[i][j] == chr(48+k):
#                 # left
#                 try:
#                     if maze[i-1][j] == "#":
#                         path = k
#                     if maze[i-1][j] == " ":
#                         maze[i-1] = maze[i-1][:j] + chr(49+k) + maze[i-1][j+1:]
#                 except IndexError: print()
#
#                 # right
#                 try:
#                     if maze[i+1][j] == "#":
#                         path = k
#                     if maze[i+1][j] == " ":
#                         maze[i+1] = maze[i+1][:j] + chr(49+k) + maze[i+1][j+1:]
#                 except IndexError: print()
#
#                 # up
#                 try:
#                     if maze[i][j-1] == "#":
#                         path = k
#                     if maze[i][j-1] == " ":
#                         maze[i] = maze[i][:j-1] + chr(49+k) + maze[i][j:]
#                 except IndexError: print()
#
#                 # down
#                 try:
#                     if maze[i][j+1] == "#":
#                         path = k
#                     if maze[i][j+1] == " ":
#                         maze[i] = maze[i][:j+1] + chr(49+k) + maze[i][j+2:]
#                 except IndexError: print()
#
#     for l in range(7): print()
#     print("\n".join(maze))
#     for l in range(7): print()
#     # time.sleep(0.5)
#     k+=1
#
# print(path)
#
# # robot movement
# x=0
# y=0
#
# for i in range(10):
#     for j in range(10):
#         if maze[i][j] == '#':
#             x=i
#             y=j
#
# for k in range(path+1):
#     # left or up
#     try:
#         if maze[x-1][y] == chr(48+path-k):
#             maze[x-1] = maze[x-1][:y] + "#" + maze[x-1][y+1:]
#             x=x-1
#             y=y
#     except IndexError: print()
#
#     # right or down
#     try:
#         if maze[x+1][y] == chr(48+path-k):
#             maze[x+1] = maze[x+1][:y] + "#" + maze[x+1][y+1:]
#             x=x+1
#             y=y
#     except IndexError: print()
#
#     # up
#     try:
#         if maze[x][y-1] == chr(48+path-k):
#             maze[x] = maze[x][:y-1] + "#" + maze[x][y:]
#             x=x
#             y=y-1
#     except IndexError: print()
#
#     # down
#     try:
#         if maze[x][y+1] == chr(48+path-k):
#             maze[x] = maze[x][:y+1] + "#" + maze[x+1][y+2:]
#             x=x
#             y=y+1
#     except IndexError: print()
#
#     for l in range(5): print()
#     print("\n".join(maze))
#     for l in range(5): print()
#     time.sleep(0.5)
#
#
# # HAS SOME BUG