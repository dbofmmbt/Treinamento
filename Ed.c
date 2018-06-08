#include <stdio.h>
#include <stdlib.h>

void adicionar(Node *novo);
void menu_opcoes(void);

int main(void) {
    //  Definição da lista:
    typedef struct node {
        int id = 0;
        struct node next = NULL;
    }Node;

    //  Iniciando nó-cabeça:
    extern Node *raiz = malloc(sizeof(Node));
    extern id_counter = 0;
    adicionar(raiz);

    //  Inicio, de fato, do programa:


    return 0;
}

void adicionar(Node *novo) {
        Node *atual = raiz;

        while(atual->next != NULL) atual = atual->next;

        atual->next = malloc(sizeof(Node));
        atual = atual->next;
        atual->id = id_counter;
        id_counter++;
        return;
}
void menu_opcoes(void) {
    printf("Olá, o que gostaria de fazer com sua pilha?\n");
    printf("    1 - Adicionar um elemento.\n");
    printf("    2 - Remover um elemento.\n");
    printf("    0 - Encerrar o programa.\n");

    return;
}
