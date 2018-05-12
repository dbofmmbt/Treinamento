n = int(input())

for i in range(n):
    bonus = int(input())
    AD, DD, LD = map(int, input().split())
    AG, DG, LG = map(int, input().split())

    if LD%2 == 0:
        D = (AD+DD)/2 + bonus
    else:
        D = (AD+DD)/2

    if LG%2 == 0:
        G = (AG+DG)/2 + bonus
    else:
        G = (AG+DG)/2

    if D > G:
        print("Dabriel")
    elif G > D:
        print("Guarte")
    else:
        print("Empate")
