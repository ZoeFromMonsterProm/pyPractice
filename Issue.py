

triangle = []
total = 0
while True:
    layer = list((input()))
    while "," in layer:
        layer.remove(",")
    while " " in layer:
        layer.remove(" ")
    if len(layer) == 0:
        break
    triangle.append(layer)



for x in range (len(triangle)):
    current = 201
    curlist = triangle[x]
    for y in range(x+1):
        interest = int(curlist[y])
        if interest < current:
            current = interest
    total = total + current

print(total)

    