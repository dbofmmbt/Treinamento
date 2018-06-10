#include <stdio.h>
#include <stdlib.h>

void adicionar();
void printar_lista(void);
int menu_opcoes(void);

//  Definição da lista:
typedef struct node{
    int id;
    struct node *next;
} Node;

//  declarando nó-cabeça:
Node *raiz;
int id_counter = 0;

int main(void){

    //  iniciando nó-cabeça:
    raiz = malloc(sizeof(Node));

    //  Inicio, de fato, do programa:
    int escolha = 1; // Iniciado com valor arbitrário.
    while(escolha){
        escolha = menu_opcoes();
        switch(escolha){
            case 1:
                adicionar();
                printf("Elemento adicionado.\n");
                break;
            case 3:
                printf("\n");
                printf("Sequencia de elementos:\n");
                printar_lista();
                printf("\n");
                break;
        }
        printf("\n");   // Formatação Rudimentar nesse trecho!
        int div = 0;
        for(div=0; div<27; div++)
            printf("-");
        printf("\n\n");
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
    Node *atual  = raiz->next;
    while(atual != NULL){
        printf("%d ", atual->id);
        atual = atual->next;
    }
    return;
}
