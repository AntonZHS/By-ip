n = int(input())
m = []
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        m.append(i)    
print(len(m))        