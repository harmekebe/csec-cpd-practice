a1, a2, a3, a4 = map(int, input().split())
s = input()

ans = 0

for c in s:
    if c == '1':
        ans += a1
    elif c == '2':
        ans += a2
    elif c == '3':
        ans += a3
    elif c == '4':
        ans += a4

print(ans)