#include "LSD.h"

// Estruturas
struct node{
    int info;
    struct node *prox;
};

struct descritor{
    Elemento *inicio, *fim;
    int tam;
};

// Funções de Uso Interno
Elemento *cria_elemento(int valor);

// Implementação das Funções da Biblioteca
void exibe(Lista *l){
    Elemento *p;
    printf("Sua lista é: ");
    for(p=l->inicio; p; p=p->prox)
        printf("%d ", p->info);
    printf("\n");
}

Lista *inicializa(void){
    Lista *novo = (Lista *) malloc(sizeof(Lista));
    novo->tam = 0;
    novo->inicio = NULL;
    novo->fim = NULL;
    return novo;
}

void insere_fim(Lista *l, int valor){
    Elemento *p = cria_elemento(valor);
    if(!l->tam) l->inicio = p;
    else l->fim->prox = p;
    l->fim = p;
    l->tam++;
}

void insere_ini(Lista *l, int valor){
    Elemento *p = cria_elemento(valor);
    if(!l->tam) l->fim = p;
    p->prox = l->inicio;
    l->inicio = p;
    l->tam++;
}

void retira(Lista *l, int valor){
    Elemento *ant, *p = l->inicio;
    while(p && p->info != valor){
        ant = p;
        p=p->prox;
    }
    if(!p) return;
    else {
        ant->prox = p->prox;
        free(p);
    }
}

void libera(Lista *l){
    Elemento *p, *aux;
    while(p) {
        aux = p->prox;
        free(p);
        p = aux;
    }
}

// Funções de Uso Interno
Elemento *cria_elemento(int valor){
    Elemento *resp = (Elemento *) malloc(sizeof(Elemento));
    resp->prox = NULL;
    resp->info = valor;
    return resp;
}