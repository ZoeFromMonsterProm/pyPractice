s = input("Enter sting: ")
ans = 0

for x in range(len(s)):
    check = ""
    for y in range(x,len(s)):
        if check.find(s[y]) != -1:
            break
        check = check + s[y]
    if len(check) > ans:
        ans = len(check)
print(ans)
        
