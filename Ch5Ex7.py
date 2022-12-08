#Works only for limited test cases. Do not yet know how to code for strictly increasing values.
n = int(input())
reads = input().split()

for i in range(n):
    reads[i] = int(reads[i])

count = 0
smol = reads[1]
yuge = reads[-1] 
tot = yuge - smol

for i in range(len(reads)):
    if count < (len(reads)) - 1:
        right = reads[i + 1] - reads[i]
        count = count + 1
    elif count == (len(reads)) - 1:
        break

insort = reads
insort.pop(0)
insort.pop(-1)

sort = 0
if(all(insort[i] <= insort[i + 1] for i in range(len(insort)-1))):
    sort = 1
if sort > 0:
    print(tot)
else:
    print('unknown')
