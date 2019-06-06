#include <stdlib.h>

/*

  Árvore B:
    * Definição: Uma árvore B possui as seguintes propriedades:
    
    1) Todo Nó tem os seguintes campos:
      NChaves (NC): int
      chaves (|NC|) ordenadas CH1 < CH2 < ... < CHnc
      Folha: int
      NC+1 ponteiros P/ os filhos. Se folha, Ponteiros Nulos.
    
    2) Se a chave Ki não está no Nó, pode estar em seus filhos:
      K1 < CH1 < K2 < CH2 < ... < K|nc| < CH|nc| < K|nc|+1

    3) Cada folha tema  mesma profundidade de h = Log t (n)

    4) Existem limites inferiores e superiores de N de chaves e filhos,
       baseados no grau mínimo da árvore B, chamado t.
    
      a) Todo nó, exceto a raiz, tem pelo menos t-1 chaves, e t filhos,
        se não for folha.
    
      b) Todo nó pode ter 2t-1 chaves e 2t filhos, se não for folha.
        Assim, um Nó Completo tem 2t-1 chaves.
      
    * Árvore B mais simples (depois da árvore vazia):
    *   t = 2, chamada árvore 2-3-4
    * Na prática, t é muito maior.
    
    * Altura da Árvore B:
    *   log t (n)
*/

/*
  1) Estrutura da Árvore B:
*/

#define T 2

typedef struct arvb
{
    int nc, folha;
    int *ch;
    struct arvb **filho;
} TAB;

static TAB *cria(int t)
{
    TAB *novo = (TAB *)malloc(sizeof(TAB));
    novo->nc = 0;
    novo->folha = 1;
    novo->ch = (int *)malloc(sizeof(int) * (t * 2) - 1);
    novo->filho = (TAB **)malloc(sizeof(TAB *) * 2 * t);
    int i;
    for (i = 0; i < 2 * t; i++)
        novo->filho[i] = NULL;
    return novo;
}

TAB *busca(TAB *a, int k)
{
    if (!a)
        return NULL;
    int i = 0;
    while ((i < a->nc) && (k > a->ch[i]))
        i++;
    if (i < a->nc && a->ch[i] == k)
        return a;
    return busca(a->filho[i], k);
}

/*
  INSERÇÃO E RETIRADA:
    Algoritmos de  ->     Possibilidade de      ->  Acertar Nó Vigente e
    uma passagem   ->  violação de propriedade  ->  depois faz a operação

    Toda vez que um nó está completo no caminho de inserção, divide-se esse Nó.
    Dividir o nó consiste em subir a chave do meio para seu pai e dividir as duas
    metades remanescentes em 2 nós: um intervalo antes do meio, um depois.
*/

void libera(TAB *a)
{
    if (a)
    {
        if (!a->folha)
        {
            for (int i = 0; i <= a->nc; i++)
                libera(a->filho[i]);
        }
        free(a->filho);
        free(a->ch);
        free(a);
    }
}

void imprime(TAB *a)
{
    if (a)
    {
        int i;
        for (i = 0; i < a->nc; i++)
        {
            if (!a->folha)
                imprime(a->filho[i]);
            printf("%d\n", a->ch[i]);
        }
        if (!a->folha)
            imprime(a->filho[i]);
    }
}

TAB *insere(TAB *a, int ch, int t)
{
    if (!a)
    {
        a = cria(t);
        a->ch[0] = ch;
        a->nc++;
        return a;
    }
    if (a->nc == ((2 * t) - 1))
    {
        TAB *novo = cria(t);
        novo->folha = 0;
        novo->filho[0] = a;
        novo = divisao(novo, 1, a, t);
        novo = ins_nao_compl(novo, ch, t);
        return novo;
    }
    a = ins_nao_compl(a, ch, t);
    return a;
}

TAB *divisao(TAB *a, int i, TAB *y, int t)
{
    TAB *z = cria(t);
    z->folha = y->folha;
    z->nc = t - 1;
    int j;
    for (j = 0; j < t - 1; j++)
        z->ch[j] = y->ch[j + t];

    if (!y->folha)
    {
        for (j = 0; j < t; j++)
        {
            z->filho[j] = y->filho[j + t];
            y->filho[j + t] = NULL;
        }
    }
    y->nc = t - 1;

    for (j = a->nc; j >= i; j--)
        a->filho[j + 1] = a->filho[j];
    a->filho[i] = z;

    for (j = a->nc; j >= i; j--)
        a->ch[j] = a->ch[j - 1];
    a->ch[i - 1] = y->ch[t - 1];
    a->nc++;
    return a;
}

TAB *ins_nao_compl(TAB *a, int k, int t)
{
    int i = a->nc - 1;
    if (a->folha)
    {
        while ((i >= 0) && (k < a->ch[i]))
        {
            a->ch[i + 1] = a->ch[i];
            i--;
        }
        a->ch[i + 1] = k;
        a->nc++;
        return a;
    }
    else
    {
        while ((i >= 0) && (k < a->ch[i]))
            i--;
        i++;
        if (a->filho[i]->nc == ((2 * t) - 1))
        {
            a = divisao(a, (i + 1), a->filho[i], t);
            if (k > a->ch[i])
                i++;
        }
        a->filho[i] = ins_nao_compl(a->filho[i], k, t);
    }
    return a;
}

/*
    REMOÇÃO
    * Mais complicada;
    * Empurrar a info para a folha, garantindo
    * o limite mínimo de chaves.
     
    * ALGORITMO:
    
    * 1) Se K está em X e X é folha, retire K de X
    * 
    * 2) Se K está em X e X é Nó Interno:
    *   
    *   2A) Se o filho Y que precede X tem, ao menos,
    *       T chaves, encontre a chave predecessora
    *       K' em Y. Elimine K' de Y e coloque K' no
    *       lugar de K em X:
    * 
    *    2B) Se o filho Z que sucede X tem, ao menos,
    *       T chaves, encontre a chave sucessora
    *       K' em Z. Elimine K' de Z e coloque K' no
    *       lugar de K em X:
    * 
    *    2C) Se Y e Z têm T-1 chaves, faça a junção de
    *       Y, K e Z em Y. Y terá 2T - 1 chaves. Depois,
    *       retire K de Y.
    * 
    * 3) Se K NÃO está em X, descubra o filho F onde K
    *   deve estar. Se F tem T - 1 chaves, ou aplique
    *   (3A) ou aplique (3B):
    * 
    *    3A) Se F tem T - 1 chaves, mas possuir irmão
    *       imediato I com pelo menos T chaves, forneça
    *       uma chave de I ao pai e forneça a chave do
    *       pai para F.
    * 
    *    3B) Se F tem T - 1 chaves e o(s) irmão(s) tem
    *       T - 1 chaves, faça a intercalação de F com
    *       UM de seus irmãos imediatos, pegando uma
    *       chave do pai para o nó intercalado.
*/