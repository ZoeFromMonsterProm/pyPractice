def combi(*num):
    ans = 1
    for x in num:
        ans = ans*x
    return(ans)

print(combi(3,7,4))