n = int(input())

teams = []
for _ in range(n):
    teams.append(list(map(int, input().split())))


count = 0
for i in range(n):
    for j in range(n):
        if teams[i][0] == teams[j][1]:
            count += 1

print(count)    