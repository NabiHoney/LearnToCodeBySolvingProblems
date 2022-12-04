t = []
tx = []
bt = []
bx = []

a = int(input())
for i in range(a):
    t.append(int(input()))
tx = [i for i in t if i <= 1440]


b = int(input())
for i in range(b):
    bt.append(int(input()))
bx = [i for i in bt if i <= 1440]

print (len(tx) + len(bx))

comb = []
i=0
x=0

while i<len(tx)and x<len(bx):
    if tx[i]<bx[x]:
        comb.append('a')
        i=i+1
    else:
        comb.append('b')
        x=x+1          

for il in tx[i:]:
    comb.append('a')

for xl in bx[i:]:
    comb.append('b')

combs=''.join(comb)
if len(combs) == 4:
    if combs != 'aaaa' or 'bbbb':
        total = 1
        print(total)
    else:
        tota = 0
        print(tota)
elif len(combs) > 4:
    diff = combs.count('ab')
    dif = combs.count('ba')
    to = diff + dif
    print(to)
