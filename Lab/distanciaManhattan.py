def modulo(n):
    if n < 0:
        return n*(-1)
    return n

x1, y1, x2, y2 = map(int, input().split())

xf = x1 - x2
yf = y1 - y2

resultado = modulo(xf) + modulo(yf)
print(resultado)
