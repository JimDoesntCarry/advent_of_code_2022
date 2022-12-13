input = open("day_12_input.txt","r")
lines = input.read().split("\n")

matrix = []
empty_matrix = []
for i in lines:
    line = []
    empty = []
    for j in i:
        empty.append("")
        ascii = ord(j)
        if ascii >= 97 and ascii <= 122:
            ascii -= 96
            line.append(ascii)
        elif ascii == 83:
            line.append(100)
        elif ascii == 69:
            line.append(200)
    matrix.append(line)
    empty_matrix.append(empty)

start_x = 0
start_y = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 100:
            start_x = j
            start_y = i
        if matrix[i][j] == 200:
            end_x = j
            end_y = i

open_list = []
closed_list = []
start = (start_y, start_x)
current = (start_y, start_x)
open_list.append(start)
print(empty_matrix)
