#include <stdio.h>
#include <stdlib.h>

void adicionar();
void menu_opcoes(void);

//  Definição da lista:
typedef struct node{
    int id;
    struct node *next;
} Node;

//  Iniciando nó-cabeça:
extern Node *raiz = malloc(sizeof(Node));
int id_counter = 0;

int main(void){

    //  Inicio, de fato, do programa:
    int escolha = 1; // Iniciado com valor arbitrário.
    while(escolha){
        escolha  = menu_opcoes();
        switch(escolha){
            case 1:
                adicionar()
                printf("Elemento adicionado.\n");

            case 3:
                printf("Sequencia de elementos:\n");
                printar_lista();
        }
    }
    return 0;
}

void adicionar(){
        Node *atual = raiz;
        while(atual->next != NULL)
            atual = atual->next;
        atual->next = malloc(sizeof(Node));
        atual = atual->next;
        atual->id = id_counter;
        id_counter++;
        return;
}

int menu_opcoes(void){
    int opcao;
    printf("Olá, o que gostaria de fazer com sua lista?\n");
    printf("    1 - Adicionar um elemento.\n");
    printf("    2 - Remover um elemento.\n");
    printf("    3 - Listar os elementos.\n");
    printf("    0 - Encerrar o programa.\n");
    scanf("%d", &opcao);
    return opcao;
}

void printar_lista(void){
    Node *atual  = raiz;
    while(atual != NULL){
        printf("%d", atual->id);
        atual = atual->next;
    }
    return;
}
