n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
stones_to_remove = 0

for i in range(n):
    if sum(matrix[i]) >= 2:
        stones_to_remove += 1

print(stones_to_remove)