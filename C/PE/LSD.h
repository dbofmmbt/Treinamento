#include <stdio.h>
#include <stdlib.h>

typedef struct descritor Lista;
typedef struct node Elemento;

void exibe(Lista *l);
Lista *inicializa(void);
void insere_fim(Lista *l, int valor);
void insere_ini(Lista *l, int valor);
void retira(Lista *l, int valor);
void libera(Lista *l);
