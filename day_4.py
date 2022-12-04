input_file = open("day_4_input.txt", "r")
all_assignements = input_file.read()
elf_pairs = all_assignements.split("\n")

temp_elf_pair = []
elf_ass_pair = []
for elf_pair in elf_pairs:
     temp_elf_pair = elf_pair.split(",")
     elf_ass_pair.append(temp_elf_pair)

length = len(elf_ass_pair)
for i in range(0,length,1):
    if elf_ass_pair[i] == [""]:
        del elf_ass_pair[i]

full_contained_counter = 0
part_contained_counter = 0
for elf_pair in elf_ass_pair:
    elf_ass1 = elf_pair[0].split("-")
    elf_ass2 = elf_pair[1].split("-")
    # lower bound 1 >= lower bound 2 and upper bound 1 <= upper bound 2
    # and reverse
    if int(elf_ass1[0]) >= int(elf_ass2[0]) and int(elf_ass1[1]) <= int(elf_ass2[1]):
        full_contained_counter += 1
    elif int(elf_ass2[0]) >= int(elf_ass1[0]) and int(elf_ass2[1]) <= int(elf_ass1[1]):
        full_contained_counter += 1

    if int(elf_ass1[0]) in range(int(elf_ass2[0]),int(elf_ass2[1])+1):
        part_contained_counter += 1
    elif int(elf_ass1[1]) in range(int(elf_ass2[0]),int(elf_ass2[1])+1):
        part_contained_counter += 1
    elif int(elf_ass2[0]) in range(int(elf_ass1[0]),int(elf_ass1[1])+1):
        part_contained_counter += 1
    elif int(elf_ass2[1]) in range(int(elf_ass1[0]),int(elf_ass1[1])+1):
        part_contained_counter += 1

print("There are "+ str(full_contained_counter) + " fully contained assignements")
print("There are "+ str(part_contained_counter) + " partly contained assignements")
