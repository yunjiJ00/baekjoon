year = int(input())
sol = False
con1 = year%4
con2 = year%100
con3 = year%400
if con1 == 0:
    if con2 != 0 or con3 == 0:
        sol = True
if sol == True:
    print(1)
else:
    print(0)