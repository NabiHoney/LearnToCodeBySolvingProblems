start_year = int(input()) #g, post def.

year = start_year + 1 #g, post def.

def find_dups(year):
    """
    I don't like docstrings, but
    I will learn to use them anyway.
    """
    sy = str(year)
    x = [] #g
    for char in sy: #g, used counter orig.
        if char in x:
            return False
        x.append(char)
    return True

while not find_dups(year):
    year = year + 1

print(year)
