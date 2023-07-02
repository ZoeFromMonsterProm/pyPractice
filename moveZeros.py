nums = input()
numList = nums.split(",")

for y in range(len(numList)):
    numList[y] = int(numList[y])

for x in range(len(numList)):
    if numList[x] == 0:
        numList.pop(x)
        numList.append(0)

print(numList)