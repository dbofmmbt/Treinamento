#Resolução do problema "Dama", do URI:
def noLugar(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return True
    return False

x1, y1, x2, y2 = map(int, input().split())
while x1 != 0 and x2 != 0 and y1 != 0 and y2 != 0:
    if noLugar(x1, y1, x2, y2):
        print("0")
    elif x1 == x2 or y1 == y2:
        print("1")
    elif (x2 - x1 == y2 - y1) or ((x2 - x1)*(-1) == y2 - y1 ):
        print("1")
    else:
        print("2")
    x1, y1, x2, y2 = map(int, input().split())