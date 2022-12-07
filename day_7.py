from anytree import Node, RenderTree, findall, PreOrderIter, LevelOrderIter
input = open("day_7_input.txt","r")
commands = input.read().split("\n")

for i in range(len(commands)):
    if commands[i] == "":
        del commands[i]

filesystem = Node("/")
cd = filesystem

for i in commands:
    if "$ cd" in i[:4]:
        if "/" not in i[5:]:
            if ".." not in i[5:]:
                parent = cd
                cd = Node(i[5:], parent = parent)
            else:
                cd = parent
                parent = cd.parent
    elif "$" not in i[:2]:
        if "dir" not in i[:3]:
            file = i.split(" ")
            filename = file[0]
            Node(filename, parent = cd)

print(RenderTree(filesystem))
dirs = filesystem.descendants
used_space = 0
scores = 0
for dir in dirs:
    score = 0
    if dir.is_leaf == False:
        for leaf in dir.leaves:
            score += int(leaf.name)
        if score <= 100000:
            scores += score

for leaf in filesystem.leaves:
    used_space += int(leaf.name)

filesystem_size = 70000000
needed_size = 30000000
free_space = filesystem_size-used_space
needed_space = needed_size-free_space
spaces = []
for dir in dirs:
    score = 0
    if dir.is_leaf == False:
        for leaf in dir.leaves:
            score += int(leaf.name)
        if score >= needed_space:
            spaces.append(score)

spaces.sort()
print(needed_space)
print(spaces)
#print(scores)
