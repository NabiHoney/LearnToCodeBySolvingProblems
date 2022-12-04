for colors in range(10):
	rcount = 0
	ycount= 0
	ocount= 0
	gcount= 0
	bcount= 0
	vcount= 0
	brcount= 0
	pcount= 0
	
	eob = False

	while not eob:
		w = input()
		if w == 'end of box':
			eob = True		
		elif w == 'yellow':
			ycount = ycount + 1
		elif w == 'orange':
			ocount = ocount + 1
		elif w == 'green':
			gcount = gcount + 1	
		elif w == 'blue':
			bcount = bcount + 1
		elif w == 'violet':
			vcount = vcount + 1
		elif w == 'brown':
			brcount = brcount + 1
		elif w == 'pink':
			pcount = pcount + 1
		elif w == 'red':
			rcount = rcount + 1
	handfuls = (ycount + 6) // 7 + (ocount + 6) // 7 + (gcount + 6) // 7 + (bcount + 6) // 7 +(vcount + 6) // 7 + (brcount + 6) // 7 + (pcount + 6) // 7
	print(handfuls*13 + rcount*16)
