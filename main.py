vg = int(input())
a = False
b = False

if vg % 4 == 0:
    a = True
if vg % 100 != 0 or vg % 400 == 0:
    b = True

if b and a:
    print('весокосный год')
else:
    print('обычный год')