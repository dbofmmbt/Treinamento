#Resolução do problema "Alarme Despertador", do URI:

resultado = 0
H1, M1, H2, M2 = list(map(int, input().split()))
while H1 != 0 or M1 != 0 or H2 != 0 or M2 != 0:
    if H2 < H1 or (H2 == H1 and M2 < M1):
        H2 += 24
    if M1 > M2:
        resultado -= 60
        M2 += 60
    resultado += (H2-H1)*60 + M2-M1
    print(resultado)
    resultado = 0
    H1, M1, H2, M2 = list(map(int, input().split()))
