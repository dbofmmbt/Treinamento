andar = [0, 0, 0]
funcionarios = []
funcionarios.append(int(input()))
funcionarios.append(int(input()))
funcionarios.append(int(input())) 

andar[0] = funcionarios[1] * 2 + funcionarios[2] * 4
andar[1] = funcionarios[0] * 2 + funcionarios[2] * 2
andar[2] = funcionarios[1] * 2 + funcionarios[0] * 4

print(min(andar))
