w = int(input())
p = int(input())

a = 'absolutely'
f = 'fairly'
v = 'very'

if (w == 3) and (p >= 95):
	print ('C.C. is', a, 'satisfied with her pizza.')
elif (w == 1) and (p <= 50):
	print ('C.C. is', f, 'satisfied with her pizza.')
else:
	print ('C.C. is', v, 'satisfied with her pizza.')
