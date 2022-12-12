input = open("day_11_input.txt","r")
input_lines = input.read().split("\n")

monkeys = []
for i in range(len(input_lines)):
    if "Monkey" in input_lines[i]:
        monkey = []
    if "Starting items" in input_lines[i]:
        monkey.append(input_lines[i].replace("  Starting items: ", "").split(", "))
    if "Operation" in input_lines[i]:
        function = input_lines[i].replace("  Operation: new = ", "")
        #function.append(lambda old: eval(input_lines[i].replace("  Operation: new = ", "")))
        monkey.append(function)
    if "Test" in input_lines[i]:
        div = input_lines[i].replace("  Test: divisible by ","")
        monkey.append(div)
    if "true" in input_lines[i]:
        if_list = []
        t_monk = input_lines[i].replace("    If true: throw to monkey ","")
        if_list.append(t_monk)
    if "false" in input_lines[i]:
        f_monk = input_lines[i].replace("    If false: throw to monkey ","")
        if_list.append(f_monk)
        monkey.append(if_list)
    if "" == input_lines[i]:
        monkeys.append(monkey)

throws = []
for m in monkeys:
    throws.append(0)
throw_index = 0
for c in range(10000):
    for monkey in monkeys:
        print(monkey)
        throws[throw_index] += len(monkey[0])
        if throw_index < len(monkeys)-1:
            throw_index += 1
        else:
            throw_index = 0

        for i in range(len(monkey[0])):
            item = monkey[0].pop(0)
            func = lambda old: eval(monkey[1])
            new_item = func(int(item))
            #Starfruit 1
            """
            new_item = new_item / 3
            new_item = int(new_item)

            if new_item % int(monkey[2]) == 0:
                monkeys[int(monkey[3][0])][0].append(int(new_item))
            else:
                monkeys[int(monkey[3][1])][0].append(int(new_item))
            """
            #Starfruit 2
            if new_item % int(monkey[2]) == 0:
                monkeys[int(monkey[3][0])][0].append(int(new_item)%100)
            else:
                monkeys[int(monkey[3][1])][0].append(int(new_item)%100)

print(throws)
