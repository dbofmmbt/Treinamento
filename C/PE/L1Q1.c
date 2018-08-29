#include <stdio.h>

int main(void){
    int n;

    do{  // Enquanto n for maior que Zero.
        scanf("%d", &n);
        if (n<=0) return 0;

        int primo, i=0, j;
        primo = n;

        // Começar já com N sendo o primeiro impar após o número dado:
        if (primo%2) primo+=2;
        else primo++;

        // Lidando com casos "chatos":
        if (n==1) {
            printf("%d\n", 2);
            continue;
        }

        if (n==2) {
            printf("%d %d\n", 3, 5);
            continue;
        }

        while(i<n){
            int isPrimo = 1; // Flag para impressão do número.
            for(j=3; j<=(primo/2); j+=2){ // Teste de Primo.
                if (!(primo%j)){
                    isPrimo = 0;
                    break;
                }
            }
            if (isPrimo){
                printf("%d ", primo);
                i++;
            }
            primo+=2;
        }
        printf("\n");

    } while(1);

    return 0;
}