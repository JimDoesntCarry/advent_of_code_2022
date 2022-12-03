# Open file and read the strategy and split them into items in list
input_file = open("day_3_input.txt", "r")
all_items = input_file.read()
# split all items into rucksaecke
rucksaecke = all_items.split('\n')

shared_item = []
for rucksack in rucksaecke:
    rucksack_len = len(rucksack)
    compartment_len = rucksack_len // 2
    compartment_1 = rucksack[:compartment_len]
    compartment_2 = rucksack[compartment_len:]
    for i in compartment_1:
        for j in compartment_2:
            if i == j:
                shared_item.append(i)
