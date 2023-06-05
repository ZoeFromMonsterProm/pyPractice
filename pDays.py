def progress_days(a):
    count = 0
    for x in range(1,len(a)):
        if a[x-1] < a[x]:
            count = count + 1
    return(count)

print(progress_days([10,10]))


print("Hello Na")
