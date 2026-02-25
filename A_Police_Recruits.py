n = int(input())

nums = [int(x) for x in input().split()]

ans = 0
current = 0

for num in nums:
    if num >= 0:
        if current < 0:
            ans += current
            current = 0
        
    current += num

if current < 0:
    ans += current

print(ans*-1)    