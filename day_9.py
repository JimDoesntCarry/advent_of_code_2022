input = open("day_9_input.txt","r")
commands = input.read().split("\n")

temp_commands = []
for i in commands:
    if i != "":
        temp_commands.append(i.split(" "))
commands = temp_commands
#Starfruit 1
"""
H_x=0
H_y=0
T_x=0
T_y=0

visited = [[0,0]]

for command in commands:
    for i in range(int(command[1])):
        if command[0] == "D":
            H_y -= 1
        elif command[0] == "U":
            H_y += 1
        elif command[0] == "L":
            H_x -= 1
        elif command[0] == "R":
            H_x += 1

        if (T_x not in range(H_x-1,H_x+2)) and (T_y not in range(H_y-1,H_y+2)):
            if T_x < H_x:
                T_x +=1
            elif T_x > H_x:
                T_x -=1
            if T_y < H_y:
                T_y +=1
            elif T_y > H_y:
                T_y -=1
        elif T_x not in range(H_x-1,H_x+2):
            if T_x < H_x:
                T_x +=1
            elif T_x > H_x:
                T_x -=1
            if T_y < H_y:
                T_y +=1
            elif T_y > H_y:
                T_y -=1
        elif T_y not in range(H_y-1,H_y+2):
            if T_y < H_y:
                T_y +=1
            elif T_y > H_y:
                T_y -=1
            if T_x < H_x:
                T_x +=1
            elif T_x > H_x:
                T_x -=1

        if [T_x,T_y] not in visited:
            visited.append([T_x,T_y])

print(len(visited))
"""
#Starfruit 2

knots = []
for i in range(10):
    knots.append([0,0])

visited = [[0,0]]

for command in commands:
    for i in range(int(command[1])):
        if command[0] == "D":
            knots[0][1] -= 1
        elif command[0] == "U":
            knots[0][1] += 1
        elif command[0] == "L":
            knots[0][0] -= 1
        elif command[0] == "R":
            knots[0][0] += 1

        for i in range(1,len(knots)):
            if (knots[i][0] not in range(knots[i-1][0]-1,knots[i-1][0]+2)) and (knots[i][1] not in range(knots[i-1][1]-1,knots[i-1][1]+2)):
                if knots[i][0] < knots[i-1][0]:
                    knots[i][0] +=1
                elif knots[i][0] > knots[i-1][0]:
                    knots[i][0] -=1
                if knots[i][1] < knots[i-1][1]:
                    knots[i][1] +=1
                elif knots[i][1] > knots[i-1][1]:
                    knots[i][1] -=1
            elif knots[i][0] not in range(knots[i-1][0]-1,knots[i-1][0]+2):
                if knots[i][0] < knots[i-1][0]:
                    knots[i][0] +=1
                elif knots[i][0] > knots[i-1][0]:
                    knots[i][0] -=1
                if knots[i][1] < knots[i-1][1]:
                    knots[i][1] +=1
                elif knots[i][1] > knots[i-1][1]:
                    knots[i][1] -=1
            elif knots[i][1] not in range(knots[i-1][1]-1,knots[i-1][1]+2):
                if knots[i][0] < knots[i-1][0]:
                    knots[i][0] +=1
                elif knots[i][0] > knots[i-1][0]:
                    knots[i][0] -=1
                if knots[i][1] < knots[i-1][1]:
                    knots[i][1] +=1
                elif knots[i][1] > knots[i-1][1]:
                    knots[i][1] -=1


            if [knots[9][0],knots[9][1]] not in visited:
                visited.append([knots[9][0],knots[9][1]])

print(len(visited))
