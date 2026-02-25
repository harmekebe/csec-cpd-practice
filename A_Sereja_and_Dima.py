n = int(input())
cards = list(map(int, input().split()))

sereja_score = 0
dima_score = 0

for i in range(n):
    if not cards:
        break
        
    if cards[0] >= cards[-1]:
        sereja_score += cards[0]
        cards.pop(0)
    else:
        sereja_score += cards[-1]
        cards.pop(-1)

    if not cards:
        break

    if cards[0] >= cards[-1]:
        dima_score += cards[0]
        cards.pop(0)
    else:
        dima_score += cards[-1]
        cards.pop(-1)

print(sereja_score, dima_score)