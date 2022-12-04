comp = input()

am = 0
cm = 0

for i in range(len(comp)):
	if i == 0 or comp[i-1] == "|":
		if comp[i] in 'ADE':
			am = am +1
		if comp[i] in 'CFG':
			cm = cm + 1
if am == cm:
	if comp[-1] == 'A':
		am=am+1
	else:
		cm=cm+1

if am > cm:
	print('A-mol')
else:
	print('C-dur')
