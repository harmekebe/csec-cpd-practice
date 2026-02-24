x, y = input().split()

x = int(x)
y = int(y)

a=0

while x <= y:
    x*=3
    y*=2
    a+=1

print(a)