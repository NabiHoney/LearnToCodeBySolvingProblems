def distance_between(lst, i, j):    #Functions come first, order irrev/calls rev 
 
    if i < j:
        city1 = i
        city2 = j                   #sort larger number first for calc.
    else:                   
        city1 = j                   #remember, scope of var.
        city2 = i           
    total = 0
    for k in range(city1, city2):
        total = total + lst[k]      #calc dist between cits, note two (args?) temp var [k] 
    return total                       

                                    #order matters starting here for calls/top down design?

lst = input().split()               #takes user input, splits into indiv list str
for i in range(len(lst)):
    lst[i] = int(lst[i])            #type casting into ints.

for i in range(len(lst) + 1):       #remember +1 to incl all elems. OUTER loop runs last
    distances = []                  #container for calcd dists.
    for j in range(len(lst) + 1):   #inner loop to iterate(below)first
        distances.append(str(distance_between(lst, i, j)))
    print(' '.join(distances))      #prints output with spaces, no com/brackets
