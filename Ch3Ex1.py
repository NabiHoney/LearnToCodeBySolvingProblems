pw = input()

good = 0
lc = 0
uc = 0
dg = 0

for char in pw:
	if char.islower() or char.isupper() or char.isdigit():
		good = good + 1
	if char.islower():
		lc = lc + 1
	if char.isupper():
		uc = uc + 1
	if char.isdigit():
		dg = dg + 1
	
if (len(pw) >=8 and len(pw)<=12 and
	lc >=3 and uc >=2 and dg >=1):
		print('Valid')

else:
	print('Invalid')
