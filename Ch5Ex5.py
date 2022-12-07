#did not work on DMOJ, same everything except var. names. No idea why.
for set in range(10):
    num = input().split()
    t = int(num[0])
    n = int(num[1])

    time = 0
    
    for i in range(n):
        day = input()
        if day =='b':
            time=time + t - 1
        else: 
            if time > 0:
                time = time - 1
    print(time)
