#include <stdio.h>

int main(void){
    int resposta = 1;
    int bit = 3;
    int n;
    int i;
    scanf("%d", &n);
    int vetor[n];

    for(i=0; i<n; i++){
        scanf("%d", vetor+i);
    }
    for(i=1; i<n; i++){
        if(vetor[i]>vetor[i-1]){
            if(bit == 1){
                resposta = 0;
            }
            else{
                bit = 1;
            }
        }
        else if(vetor[i]<vetor[i-1]){
            if(bit == 0){
                resposta = 0;
            }
            else{
                bit = 0;
            }
        }
        else{
            resposta = 0;
        }
    }
    printf("%d\n", resposta);
    return 0;
}
