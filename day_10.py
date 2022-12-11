input = open("day_10_input.txt","r")
commands = input.read().split("\n")
#Starfruit 1
"""
cycle = 0
x = 1
check = 20
sums = 0
for command in commands:
    if command == "noop":
        cycle += 1
        if cycle == check:
            sum = cycle * x
            print("Signalstrength in cycle " + str(cycle) + "with x "+str(x)+" is : "+ str(sum))
            sums += sum
            check += 40

    elif "addx" in command:
        command = command.split(" ")
        cycle +=1
        if cycle == check:
            sum = cycle * x
            print("Signalstrength in cycle " + str(cycle) + "with x "+str(x)+" is : "+ str(sum))
            sums += sum
            check += 40
        cycle +=1
        if cycle == check:
            sum = cycle * x
            print("Signalstrength in cycle " + str(cycle) + "with x "+str(x)+" is : "+ str(sum))
            sums += sum
            check += 40
        x += int(command[1])

print("Signalstrength is : "+ str(sums))
"""

cycle = 0
x = 1
check = 39
screen = []
line = []
for command in commands:
    if command == "noop":
        if cycle in range(x-1,x+2):
            line.append("#")
        else:
            line.append(".")
        if cycle == check:
            check += 40
            x += 40
            screen.append(line)
            line = []
        cycle += 1

    elif "addx" in command:
        command = command.split(" ")
        if cycle in range(x-1,x+2):
            line.append("#")
        else:
            line.append(".")
        if cycle == check:
            check += 40
            x += 40
            screen.append(line)
            line = []
        cycle += 1
        if cycle in range(x-1,x+2):
            line.append("#")
        else:
            line.append(".")
        if cycle == check:
            check += 40
            x += 40
            screen.append(line)
            line = []


        cycle +=1


        x += int(command[1])
for i in screen:
    print(i)
"""
cycle = 0
x = 1
check = 40
screen = []
line = []
for command in commands:
    if command == "noop":
        cycle += 1
        if cycle in range(x-1,x+2):
            line.append(cycle)
        else:
            line.append(cycle)
        if cycle == check:
            check += 40
            x += 40
            screen.append(line)
            line = []

    elif "addx" in command:
        command = command.split(" ")
        cycle += 1
        if cycle in range(x-1,x+2):
            line.append(cycle)
        else:
            line.append(cycle)
        if cycle == check:
            check += 40
            x += 40
            screen.append(line)
            line = []

        cycle +=1
        if cycle in range(x-1,x+2):
            line.append(cycle)
        else:
            line.append(cycle)
        if cycle == check:
            check += 40
            x += 40
            screen.append(line)
            line = []

        x += int(command[1])
for i in screen:
    print(i)
"""
