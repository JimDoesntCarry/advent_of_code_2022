# Open file and read the calories and split them into items in list
input_file = open("day_1_input.txt", "r")
calories = input_file.read()
splitted_calories = calories.split('\n')

# temp_elf is list of his calories
temp_elf = []
# all_elves is list of all temp_elves
all_elves = []

len_splitted_calories = len(splitted_calories)

for i in splitted_calories:
    temp_elf.append(i)
    # each elf goes till the empty object
    if i == "":
        temp_elf.pop()
        all_elves.append(temp_elf)
        temp_elf = []
    # or till the last element
    elif i == splitted_calories[len_splitted_calories-1]:
        all_elves.append(temp_elf)
        temp_elf = []

# now change the list to integers of the elves
temp_elf_calories = 0
all_elf_calories = []
for elf in all_elves:
    for i in elf:
        temp_elf_calories+=int(i)
    all_elf_calories.append(temp_elf_calories)
    temp_elf_calories = 0
# sort the calories
all_elf_calories.sort()
len_all_calories = len(all_elf_calories)
print('Highest calories are: ' + str(all_elf_calories[len_all_calories-1]))
print('Second highest calories are: ' + str(all_elf_calories[len_all_calories-2]))
print('Third highest calories are: ' + str(all_elf_calories[len_all_calories-3]))
print('-------------------------------------------')
# add the top 3
sum_top_3 = all_elf_calories[len_all_calories-3] + all_elf_calories[len_all_calories-2] + all_elf_calories[len_all_calories-1]
print("Sum of the top calories: "+ str(sum_top_3))
