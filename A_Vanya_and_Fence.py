n, h = input().split()
n = int(n)
h = int(h)

a = input().split()
a = list(map(int, a))

count = 0

for i in range(n):
    if a[i] > h:
        count += 2
    else:
        count += 1

print(count)
