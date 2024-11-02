vg = int(input())
a = False
def vc(vg):
    if vg % 100 != 0 or vg % 400 == 0 and vg % 4 == 0:
        print('весокосный год')
    else:
        print('обычный год')
    return vg