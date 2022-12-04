word_list = []
end = False
while not end:
	w = input()
	if len(w) > 64:
		print('Enter maximum of 64 characters')
		continue
	lm = len(w)
	if w == 'quit!':
		end = True
	elif len(w) > 4 and w != (w[-3] in 'aeiouy')  and w[-2:] == 'or' and 'oor' not in w: 
		altw = (w.replace('or', 'our'))
		word_list.append(altw)
	else: 
		word_list.append(w)
for i in word_list:
	print(i)
