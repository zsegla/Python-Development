# Anya and 1100

t = int(input())
for _ in range(t):
    ls = list(input())
    n = int(input())
    for i in range(n):
        j, v = map(int, input().split())
        ls[j-1] = str(v)
        ns = "".join(ls)
        if "1100" in ns:
            print("YES")
        else:
            print("NO")