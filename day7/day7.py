def triangle(x, m):
    y = abs(x - m)
    return (y * (y + 1))//2

def crab_fuel(crabs,m):
    return sum([triangle(x,m) for x in crabs])


with open('day7.txt', 'r') as fp:
    crabs = [int(x) for x in fp.readline().split(",")]

L = min(crabs)
R = max(crabs)
last = float("inf")

for i in range(L, R+1):
    print(i, crab_fuel(crabs,i))

while L != R:

    M = int((L + R) / 2)
    
    l = crab_fuel(crabs,M-1)
    m = crab_fuel(crabs,M)
    r = crab_fuel(crabs,M+1)
    print(crabs, L, M, R, l, m, r)

    if l < m:
        R = M - 1
    elif r < m:
        L = M + 1
    else:
        break

print(min(l,m,r))