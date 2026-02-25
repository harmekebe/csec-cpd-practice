n = int(input())

ans = 0
prev = ''

for i in range(n):
    s = input()
    if i == 0:
        ans += 1
    else:
        if s[0] != prev:
            ans += 1
    prev = s[0]

print(ans)