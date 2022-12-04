n = int(input())
m = []

for i in range(n):
    m.append(int(input()))

end = False

while not end:
    s = int(input())
    if s == 77:
        end = True
    if s == 99:
        split=int(input()) - 1
        flow = int(input())
        left =  m[split] * flow / 100
        right = m[split] - left
        m = m[:split] + [left,right] + m[split+1:] 
    elif s == 88:
        split=int(input()) - 1
        left =  m[split]
        right = m[split + 1]
        m = m[:split] + [left + right] + m[split + 2:]

for i in range(len(m)):
    m[i] = str(round(m[i]))

print(*m,sep=' ')
