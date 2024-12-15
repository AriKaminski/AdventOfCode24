# Open the file in read mode
with open("Day1/Problem1input.txt", "r") as file:
    l1 = []
    l2 = []
    for line in file:
        columns = line.split()
        if columns:
            l1.append(columns[0])
            l2.append(columns[1])

l1.sort()
l2.sort()

print(type(l1[0]))
l1 = [int(x) for x in l1]
l2 = [int(x) for x in l2]
count = 0
sum1 = 0
sum2 = 0

for i in range(0, len(l1)):
    diff = 0
    if l1[i] > l2[i]:
        diff = l1[i] - l2[i]
    elif l1[i] < l2[i]:
        diff = l2[i] - l1[i]
    else:
        diff = 0
    sum1 += diff

for x in l1:
    for y in l2:
        count = 0
        if x == y:
            count += 1
            sum2 += x * count

print(sum1)
print(sum2)
