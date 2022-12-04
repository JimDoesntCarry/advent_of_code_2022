def exactly_one_fail(part1, part2):
    for i in part1:
        for j in part2:
            if i == j:
                return i

def exactly_one_in_three(part1, part2, part3):
    for x in part1:
        for y in part2:
            if x == y:
                for z in part3:
                    if x == y and y == z:
                        return x

# Open file and read the strategy and split them into items in list
input_file = open("day_3_input.txt", "r")
all_items = input_file.read()
# split all items into rucksaecke
rucksaecke = all_items.split('\n')

length = len(rucksaecke)
for i in range(0,length,1):
    if rucksaecke[i] == "":
        del rucksaecke[i]

priority_score = 0
for rucksack in rucksaecke:
    rucksack_len = len(rucksack)
    compartment_len = rucksack_len // 2
    compartment_1 = rucksack[:compartment_len]
    compartment_2 = rucksack[compartment_len:]
    character = exactly_one_fail(compartment_1, compartment_2)
    ascii = ord(character)
    if ascii >= 65 and ascii <= 90:
        ascii -= 64
        ascii += 26
    if ascii >= 97 and ascii <= 122:
        ascii -= 96
    priority_score += ascii

print("Der Priority-Score liegt bei: " + str(priority_score))

counter = 0
temp_group = []
groups = []
for rucksack in rucksaecke:
    if counter % 3 == 0 and counter != 0:
        groups.append(temp_group)
        temp_group = []
    temp_group.append(rucksack)
    counter += 1
groups.append(temp_group)

badge_score = 0
for group in groups:
    badge = exactly_one_in_three(group[0],group[1],group[2])
    ascii = ord(badge)
    if ascii >= 65 and ascii <= 90:
        ascii -= 64
        ascii += 26
    if ascii >= 97 and ascii <= 122:
        ascii -= 96
    badge_score += ascii
    print(badge)

print("Der Badge-Score liegt bei: " + str(badge_score))
