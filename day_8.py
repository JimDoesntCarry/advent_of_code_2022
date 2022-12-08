input = open("day_8_input.txt","r")
forest_lines = input.read().split("\n")

for i in range(len(forest_lines)):
    if forest_lines[i] == "":
        del forest_lines[i]
""" Starfruit 1
visible_trees = 0
for y in range(1,len(forest_lines)-1):
    for x in range(1,len(forest_lines[y])-1):
        top = []
        bottom = []
        left = []
        right = []
        for y_tb in range(len(forest_lines)):
            if y_tb < y:
                top.append(int(forest_lines[y_tb][x]))
            elif y_tb > y:
                bottom.append(int(forest_lines[y_tb][x]))
        for x_lr in range(len(forest_lines[y])):
            if x_lr < x:
                left.append(int(forest_lines[y][x_lr]))
            elif x_lr > x:
                right.append(int(forest_lines[y][x_lr]))
        if max(top) < int(forest_lines[y][x]):
            visible_trees += 1
        elif max(bottom) < int(forest_lines[y][x]):
            visible_trees += 1
        elif max(left) < int(forest_lines[y][x]):
            visible_trees += 1
        elif max(right) < int(forest_lines[y][x]):
            visible_trees += 1
visible_trees = visible_trees + 2 * (len(forest_lines)) + 2 * (len(forest_lines[0])) - 4
print(visible_trees)
"""
# Starfruit 2
#--------------------- WARNING --------------------------------
#YOU DONT HAVE TO LOOK AT THE TREES ON THE OUTER GRID BECAUSE THEIR SCORE IS 0 ANYWAYS ...
# I realised it too late
scenic_scores = []
for y in range(len(forest_lines)):
    for x in range(len(forest_lines[y])):
        top = []
        bottom = []
        left = []
        right = []
        sc_t = 0
        sc_b = 0
        sc_l = 0
        sc_r = 0
        for y_tb in range(len(forest_lines)):
            if y_tb < y:
                top.append(int(forest_lines[y_tb][x]))
            elif y_tb > y:
                bottom.append(int(forest_lines[y_tb][x]))
        for x_lr in range(len(forest_lines[y])):
            if x_lr < x:
                left.append(int(forest_lines[y][x_lr]))
            elif x_lr > x:
                right.append(int(forest_lines[y][x_lr]))
        if top == []:
            sc_t = 0
        else:
            for t in range(len(top)-1,-1,-1):
                if top[t] < int(forest_lines[y][x]):
                    sc_t += 1
                else:
                    sc_t += 1
                    break
        if bottom == []:
            sc_b = 0
        else:
            for t in range(len(bottom)):
                if bottom[t] < int(forest_lines[y][x]):
                    sc_b += 1
                else:
                    sc_b += 1
                    break
        if left == []:
            sc_l = 0
        else:
            for t in range(len(left)-1,-1,-1):
                if left[t] < int(forest_lines[y][x]):
                    sc_l += 1
                else:
                    sc_l += 1
                    break
        if right == []:
            sc_r = 0
        else:
            for t in range(len(right)):
                if right[t] < int(forest_lines[y][x]):
                    sc_r += 1
                else:
                    sc_r += 1
                    break
        scenic_score = sc_t * sc_b * sc_l * sc_r
        scenic_scores.append(scenic_score)
scenic_scores.sort()
print(scenic_scores)
