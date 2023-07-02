words1 = []
words2 = []
universal = []

while True:
    enter = input("Enter Word: ")
    if enter == "":
        break
    words1.append(enter)

while True:
    enter = input("Enter Check: ")
    if enter == "":
        break
    words2.append(enter)

for x in range(len(words1)):
    check = 0
    for y in range(len(words2)):
        if words1[x].find(words2[y]) > -1:
            check = check + 1
        else:
            break
    if check == len(words2):
        universal.append(words1[x])

print(universal)