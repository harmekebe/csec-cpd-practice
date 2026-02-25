s = input()

current = 0
total = 0

for ch in s:
    target = ord(ch)-ord('a')
    d = abs(target - current)
    total +=min(d, 26-d)
    current=target

print(total) 