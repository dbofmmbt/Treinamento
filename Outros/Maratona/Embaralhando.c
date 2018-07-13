#include <stdio.h>

long long fatorial(long long x, long long resposta){
    if(x != 1){
        resposta = resposta * x;
        return fatorial(x-1, resposta);
    }
    else return resposta;
}
int main(void){

    char letra;
    int checagem = scanf("%c", &letra);
    while(letra!='0' && letra != EOF && checagem > 0){
        int tamanho = 0;
        while(letra!='\n'){
            if(letra!=' '){
                tamanho++;
            }
            scanf("%c", &letra);
        }
        long long resposta = fatorial(tamanho, 1);
        printf("%llu\n", resposta);
        scanf("%c", &letra);
    }
    return 0;
}
