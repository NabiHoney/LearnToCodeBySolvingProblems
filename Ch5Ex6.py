for dataset in range(10): #g
    lst = input().split() #g
    n = int(lst[0]) #clean t#g
    m = int(lst[1]) #num events coming up#g
    d = int(lst[2]) #num days, respv.#g

    event_day = input().split() #g,wp
    for i in range(m):
        event_day[i] = int(event_day[i])

    event_day.sort() #g,wp

    shirt = n #g
    wash = 0 #g
    ecount = 0

    for day in range(1, d + 1):
        if shirt == 0:
            wash = wash + 1
            shirt = n
        shirt = shirt - 1
        while ecount < len(event_day) and event_day[ecount] == day:
            shirt = shirt + 1
            n = n + 1
            ecount = ecount + 1

    print(wash)
