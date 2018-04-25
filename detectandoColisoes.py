ret1 = [0, 0, 0, 0, 0, 0, 0, 0]
ret2 = [0, 0, 0, 0, 0, 0, 0, 0]
x1 = [0, 0]
x2 = [0, 0]
y1 = [0, 0]
y2 = [0, 0]
resposta = 0

ret1 = list(map(int, input().split()))
ret2 = list(map(int, input().split()))

ret1.append(ret1[0])
ret1.append(ret1[3])
ret1.append(ret1[2])
ret1.append(ret1[1])

ret2.append(ret2[0])
ret2.append(ret2[3])
ret2.append(ret2[2])
ret2.append(ret2[1])

x1[0] = min(ret1[0], ret1[2])
y1[0] = min(ret1[1], ret1[3])
x1[1] = max(ret1[0], ret1[2])
y1[1] = max(ret1[1], ret1[3])

x2[0] = min(ret2[0], ret2[2])
y2[0] = min(ret2[1], ret2[3])
x2[1] = max(ret2[0], ret2[2])
y2[1] = max(ret2[1], ret2[3])

# Para os casos em que há pontos de ret2 dentro de ret1:
for i in range(0,8,2):
	if ret2[i] >= x1[0] and ret2[i] <= x1[1] and ret2[i+1] >= y1[0] and ret2[i+1] <= y1[1]:
		resposta = 1
# Para os casos em que há pontos de ret1 dentro de ret2:
for i in range(0,8,2):
	if ret1[i] >= x2[0] and ret1[i] <= x2[1] and ret1[i+1] >= y2[0] and ret1[i+1] <= y2[1]:
		resposta = 1
# Para os casos em que não há pontos dentro da intersecção:
if  ret1[0] >= x2[0] and ret1[0] <= x2[1]:
	if ret1[1] <= y2[0] and ret1[3] >= y2[1]:
		resposta = 1
	elif ret1[1] >= y2[1] and ret1[3] <= y2[0]:
		resposta = 1
elif ret1[1] >= y2[0] and ret1[1] <= y2[1]:
	if ret1[0] <= x2[0] and ret1[2] >= x2[1]:
		resposta = 1
	elif ret1[0] >= x2[1] and ret1[2] <= x2[0]:
		resposta = 1
print(resposta)
