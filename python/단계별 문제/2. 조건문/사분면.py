x = int(input())
y = int(input())
if x > 0:
    if y>0:
        graph = 1
    elif y <0:
        graph = 4
elif x < 0:
    if y > 0:
        graph = 2
    elif y < 0:
        graph = 3
print(graph)