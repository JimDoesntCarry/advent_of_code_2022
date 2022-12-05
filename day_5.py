import numpy as np
input = open("day_5_input.txt","r")
input_setup = open("day_5_setup.csv","r")

commands = input.read().split("\n")
start = input_setup.read().split("\n")

setup = []
for i in range(0,len(start),1):
    if start[i] == "":
        del start[i]
    else:
        temp = start[i].split(",")
        setup.append(temp)

setupper = np.array(setup).T.tolist()

setup = []

for array in setupper:
    res = [ele for ele in array if ele != ""]
    setup.append(res)

for i in range(0,len(commands),1):
    if commands[i] == "":
        del commands[i]

moves = []

for command in commands:
    temp_quantity = command[5:].split("from")[0]
    temp_from = command.split("from")[1].split("to")[0]
    temp_to = command.split("to")[1]
    temp_command = [int(temp_quantity),int(temp_from),int(temp_to)]
    moves.append(temp_command)

temp_arr = []
# Crane 9000
"""
try:
    for move in moves:
        for i in range(0,move[0]):
            if move[0] > len(setup):
                for i in range(move[0],len(setup)):
                    setup.append([])
            pop_block = setup[move[1]-1].pop()
            setup[move[2]-1].append(pop_block)
except Exception as e:
    print(e)
    print(move)
    print(i)
    print(len(setup))
    print(setup)
word = []
for i in range(0,len(setup)):
    word.append(setup[i].pop())
print("The upper Cases are:")
print(word)
"""
# Crane 9001
try:
    for move in moves:
        pop_array = []
        for i in range(0,move[0]):
            if move[0] > len(setup):
                for i in range(move[0],len(setup)):
                    setup.append([])
            pop_block = setup[move[1]-1].pop()
            pop_array.append(pop_block)
        for j in range(0,move[0]):
            setup[move[2]-1].append(pop_array.pop())
except Exception as e:
    print(e)
    print(move)
    print(i)
    print(len(setup))
    print(setup)
word = []
for i in range(0,len(setup)):
    word.append(setup[i].pop())
print("The upper Cases are:")
print(word)
