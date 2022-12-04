n = int(input())

si = ''
ca = ''
co = 0

for i in range(n):
	si = si + input()
	ca = ''
for i in range(n):
	ca = ca + input()
for i in range(n):
	if si[i] == ca[i]:
		co = co + 1
print(co)
