str1 = input("Enter string: ")
str2 = input("Enter string: ")
factors = []
ans = ""

if str1 >= str2:
    lim = str2
    ot = str1
else:
    lim = str1
    ot = str2

for x in range(1,len(lim)+1):
    for y in range(len(lim)+1-x):
        factors.append(lim[y:x+y])

for z in range(1,len(factors)):
    check = True
    interest = factors[-z]
    if len(ot)//len(interest) != len(ot)/len(interest):
        continue
    period = len(ot)//len(interest)
    for a in range(period):
        if ot[a*len(interest):a*len(interest) + len(interest)] != interest:
            check = False
            break
    if check == True:
        ans = interest
        break

print(ans)