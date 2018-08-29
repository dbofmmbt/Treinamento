#include <stdio.h>

int main(void){
    int n, m;
    do { // Enquanto as entradas forem maiores que 1.
        scanf("%d %d", &n, &m);
        if (n <=1 || m <= 1) return 0;

        int menor, maior, i;

        menor = n<m? n : m;
        maior = m>n? m : n;

        if (!(menor%2)) menor++;
        else menor+=2;

        for (i=menor; i<maior; i+=2){
            int j;
            for (j=3; j<=i/2; j+=2) if (!(i%j)) break;
            if (j>i/2) printf("\e[32m%d ", i);
        }
        printf("\n\e[m");
    } while(1);

    return 0;
}