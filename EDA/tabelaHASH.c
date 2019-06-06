/*  TABELAS HASH  */

/*
    * Estrutura de Dados que tenta buscar elementos em O(1)
    * 
    * Preço: mais memória (dobro de gasto)
    * 
    * Suposição: ID's únicos
    * 
    * 
    * typedef struct aluno 
    * {
    *   int mat;
    *   float cr;
    * } TA;
    * 
    * 118 031 003
    * 
    * Intervalo de 1 bilhão de ID's, grande demais.
    * 
    * Solução: Tabelas Hash.
    * 
    * 
    * 1) IDEIA CENTRAL
    *   118 031 (003) -> Posição do ENEM
    * 
    *  Ciência da Computação ~= 550 Alunos
    * 
    *   #define MAX_TAM 1051
    * 
    *   TA *aluno[MAX_TAM];
    * 
    *   Usar uma Função Hash para calcular a posição do elemento.
    * 
    * PROBLEMA: Tratamento de Colisão
    * 
    * FUNÇÃO DE HASH?
    *   
    *   FH(mat) -> índice
    *   
    *   DETERMINISTICA
    *   FACILMENTE COMPUTÁVEL
    *   SER UNIFORME:
    *       P = 1/MAX_TAM
    * 
    *   MAX_TAM: É interessante ser primo.
    * 
    * 
    * int hash(int mat, int N)
    * {
    *   return mat % N;    
    * }
    * 
    * 2) TRATAMENTO DE COLISÃO
    * 
    *   TIPOS:
    *   
    *       -> Só MP:
    *           Endereçamento Aberto (sem memória adicional na estrutura);
    * 
    *       -> Em MP e MS:
    *           - Encadeamento Interior
    *           - Encadeamento Exterior
    * 
    *   2.1) Endereçamento Aberto
    * 
    *   Colisão:
    * 
    *       TENTATIVA LATERAL:
    * 
    *   int tent_lat(int mat, int k, int N)
    *   {
    *       return (hash(mat, N) + k) % N;
    *   }
    * 
    *       TENTATIVA QUADRÁTICA:
    * 
    *   int tent_quad(int mat, int k, int N, int c1, int c2)
    *   {
    *       return (hash(mat, N) + c1 * k + c2 * k * k) % N;
    *   }
    *       c1 e c2 são diferentes de zero!
    * 
    *       TENTATIVA POR MEIO DE DISPERSÃO DUPLA:
    * 
    *           Dois Hash's:
    *           
    *               T_dp(x, k, N) = (hash(x, N) + k * hash2(x, N)) % N;
    * 
    *   int tent_dp(int mat, int k, int N)
    *   {
    *       return (hash(mat, N) + K * hash2(mat, N)) % N;
    *   }
    * 
*/

/*
    * 
    *   2.1.1) Implementação de Endereçamento Aberto
*/
#include <stdlib.h>

typedef struct aluno
{
    int mat;
    float cr;
} TA;

#define N 1051

typedef TA *TabHash[N];

void inicializa(TabHash tab, int n)
{
    for (int i = 0; i < n; i++)
        tab[i] = NULL;
}

TA * aloca(int mat, float cr)
{
    TA * novo = (TA *) malloc(sizeof(TA));
    /* ... */
}