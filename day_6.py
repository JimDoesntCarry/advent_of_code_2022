input = open("day_6_input.txt","r")
stream = input.read().split("\n")

stream = stream[0]
""" 4 chars
counter = 0
breaker = 0
for i in range(len(stream)-3):
    counter += 1
    marker = [stream[i],stream[i+1],stream[i+2],stream[i+3]]
    temp_marker = marker
    for i in range(4):
        if temp_marker.pop() in temp_marker:
            break
        if temp_marker == []:
            breaker = 1
            break
    if breaker == 1:
        break
print(counter+3)
"""

counter = 0
breaker = 0
for i in range(len(stream)-13):
    counter += 1
    marker = [stream[i],stream[i+1],stream[i+2],stream[i+3],stream[i+4],stream[i+5],stream[i+6],stream[i+7],stream[i+8],stream[i+9],stream[i+10],stream[i+11],stream[i+12],stream[i+13]]
    temp_marker = marker
    for i in range(14):
        if temp_marker.pop() in temp_marker:
            break
        if temp_marker == []:
            breaker = 1
            break
    if breaker == 1:
        break
print(counter+13)
