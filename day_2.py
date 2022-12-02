# Open file and read the strategy and split them into items in list
input_file = open("day_2_input.txt", "r")
strategy = input_file.read()
# split strategy into rounds
rounds = strategy.split('\n')
# split rounds into opponent and answer
full_strat = []
for round in rounds:
    temp = round.split(' ')
    full_strat.append(temp)

length = len(full_strat)
for i in range(0,length,1):
    if full_strat[i] == ['']:
        del full_strat[i]

# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors
# X > C, Y > A, Z > B
score_1 = 0
for round in full_strat:
    if round[1] == 'X':
        score_1 += 1
        if round[0] == 'A':
            score_1 += 3
        if round[0] == 'C':
            score_1 += 6
    elif round[1] == 'Y':
        score_1 += 2
        if round[0] == 'B':
            score_1 += 3
        if round[0] == 'A':
            score_1 += 6
    elif round[1] == 'Z':
        score_1 += 3
        if round[0] == 'C':
            score_1 += 3
        if round[0] == 'B':
            score_1 += 6

# X = lose, Y = draw, Z = win

score_2 = 0
for round in full_strat:
    # A > Z, B > X, C > Y
    if round[1] == 'X':
        if round[0] == 'A':
            score_2 += 3
        if round[0]== 'B':
            score_2 += 1
        if round[0] == 'C':
            score_2 += 2
    # X = A, Y = B, Z = C
    elif round[1] == 'Y':
        score_2 += 3
        if round[0] == 'A':
            score_2 += 1
        if round[0]== 'B':
            score_2 += 2
        if round[0] == 'C':
            score_2 += 3
    # X > C, Y > A, Z > B
    elif round[1] == 'Z':
        score_2 += 6
        if round[0] == 'A':
            score_2 += 2
        if round[0]== 'B':
            score_2 += 3
        if round[0] == 'C':
            score_2 += 1

print("score for X-Y-Z as Rock-Paper-Scissors : " + str(score_1))
print("-------------------------------------------------")
print("score for X-Y-Z as Lose-Draw-Win : " + str(score_2))
