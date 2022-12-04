qs = int(input())
ans = input()

a = 'ABC'
b = 'BABC'
g = 'CCAABB'

count_a = 0
count_b = 0
count_g = 0

an = 'Adrian'
bn = 'Bruno'
gn = 'Goran'


for i in range(len(ans)):	
	if  ans [i] == a[i%len(a)]:
		count_a = count_a + 1
	if  ans [i] == b[i%len(b)]:
		count_b = count_b + 1
	if  ans [i] == g[i%len(g)]:
		count_g = count_g + 1

top = count_a
if count_b>top:
	top = count_b
if count_b>top:
	top = count_g

print(top)

if count_a == top:
    print(an)
if count_b== top:
    print(bn)
if count_g == top:
    print(gn)
