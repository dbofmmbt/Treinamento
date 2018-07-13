def fib(n, v, c):
    if n >= 0:
        c += 1
        v += fib(n-1, v, c)
        return v, c
    else:
        return n

valor = contador = 0
n = int(input())
valor, contador = fib(n, valor, contador)
print(valor)
print(contador)
