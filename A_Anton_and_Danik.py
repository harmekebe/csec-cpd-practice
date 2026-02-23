n = int(input())
s = input()

countA=0
countD=0

for ch in s:
    if ch == 'A':
        countA += 1
    elif ch == 'D':
        countD += 1

if countA > countD:
    print("Anton")
elif countD > countA:
    print("Danik")
else:
    print("Friendship")

