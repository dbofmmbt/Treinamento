''' Arquivo Fonte das Funções solicitadas pelo Profº Kowada em Laboratório. '''

def SegEquip(S1, S2):
    'Indica se os segmentos informados são equipolentes.'
    RESPOSTA = True
    S1 = SegPadrao(S1)
    S2 = SegPadrao(S2)
    for i in range(3):
        if S1[i] != S2[i]:
            RESPOSTA = False
    return RESPOSTA

def SegPadrao(S):
    'Retorna o Segmento informado em sua forma padronizada.'
    PADRAO = []
    for i in range(3):
        PADRAO.append( S[1][i] - S[0][i] )
    return PADRAO

def ModVetor(v):
    'Retorna o módulo do Vetor informado.'
    MODULO = (v[0]**2 + v[1]**2 + v[2]**2)**0.5
    return MODULO

def ProdEscalar(v1, v2):
    'Realiza o cálculo do Produto Escalar entre dois Vetores informados.'
    ESCALAR = 0
    for i in range(3):
        ESCALAR += v1[i]*v2[i]
    return ESCALAR

def MultPorEscalar(c, v):
    'Retorna a multiplicação de uma Constante por um Vetor informado.'
    for i in range(3):
        v[i] = c * v[i]
    return v

def SomaVet(v1, v2):
    'Calcula a soma entre dois Vetores.'
    SOMA = [0, 0, 0]
    for i in range(3):
        SOMA[i] = v1[i] + v2[i]
    return SOMA

def VetOposto(v):
    'Retorna o Vetor Oposto ao Vetor Informado.'
    OPOSTO = [0, 0, 0]
    for i in range(3):
        OPOSTO[i] = -v[i]
    return OPOSTO

def ProdVetorial(v1, v2):
    'Retorna o Vetor "Produto Vetorial" entre dois Vetores.'
    VETORIAL = [0, 0, 0]
    VETORIAL[0] = (v1[1]*v2[2]) - (v1[2]*v2[1])
    VETORIAL[1] = (v1[2]*v2[0]) - (v1[0]*v2[2])
    VETORIAL[2] = (v1[0]*v2[1]) - (v1[1]*v2[0])
    return VETORIAL

def VetParalelos(v1, v2):
    'Indica se os Vetores informados são Paralelos.'
    RESPOSTA = False
    if v1[0]/v2[0] == v1[1]/v2[1] == v1[2]/v2[2]:
        RESPOSTA = True
    return RESPOSTA

def PontoInReta(P, r):
    'Indica se o Ponto está contido na reta.'
    RESPOSTA = True
    for i in range(3):
        v[i] = P[i] - r[0][i]
    RESPOSTA = VetParalelos(v, r[1])
    return RESPOSTA

def PosRelRetas(r1, r2):
    'Determina a posição relativa entre retas: o primeiro booleano\
    indica se são paralelas, enquanto o segundo booleano informa se\
    a interseção entre as duas retas é vazia.'
    PARALELOS = VetParalelos(r1[1], r2[1])
    if PARALELOS:
        if r1[0] == r2[0]:
            INTERSECAO = True
        else:
            INTERSECAO = False
    else:
        v = [r1[0], r2[0]]
        v = SegPadrao(v)
        if ProdEscalar(ProdVetorial(r1[1], r2[1]), v) == 0:
            INTERSECAO = True
        else:
            INTERSECAO = False
    return PARALELOS, INTERSECAO

def PontoInPlano(P, a):
    'Indica se o Ponto está no Plano fornecido.'
    RESPOSTA = False
    v = [P, a[0]]
    if ProdEscalar(v, a[1]) == 0:
        RESPOSTA = True
    return RESPOSTA

def DistPontoReta(P, r):
    'Determina a distancia entre um Ponto e uma Reta dados.'
    v = [P, r[0]]
    DISTANCIA = ModVetor(ProdVetorial(v, r[1]))/ModVetor(r[1])
    return DISTANCIA

def DistRetaReta(r1, r2):
    'Determina a distancia entre duas Retas informadas.'
    if not VetParalelos(r1[1], r2[1]):
        DISTANCIA = 0
    else:
        DISTANCIA = DistPontoReta(r1[0], r2)
    return DISTANCIA

def DistPontoPlano(P, a):
    'Determina a distancia entre um Ponto P e um Plano a.'