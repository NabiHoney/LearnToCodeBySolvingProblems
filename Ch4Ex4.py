n = int(input()) 	
take = 0
serve = 0
eof = False

while not eof:
	w = input()
	if w == 'EOF':
		eof = True
	elif w == 'TAKE':
		take = take + 1
		n = n + 1
		if n == 1000:
			n = 1
	elif w == 'SERVE':
		serve = serve + 1
	elif w == 'CLOSE':
		totn = take - serve
		print(take, totn, n)
		take = 0
		serve = 0
