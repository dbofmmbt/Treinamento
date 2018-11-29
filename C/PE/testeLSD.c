#include "LSD.h"

int main(void){
    int n, input;
    Lista *lista = inicializa();
    printf("Quantos números você quer inserir? ");
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d", &input);
        insere_fim(lista, input);
    }
    exibe(lista);
    retira(lista, input-1);
    exibe(lista);
    libera(lista);
    return 0;
}