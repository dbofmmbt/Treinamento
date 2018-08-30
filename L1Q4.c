#include <stdio.h>

int main(void){
	int qtdNums;

	do{	// Enquanto qtdNums for maior que zero.

		scanf("%d", &qtdNums);
		if (qtdNums <= 0) return 0;

		int vetor[qtdNums];

		for (int i=0; i<qtdNums; i++) scanf("%d", &vetor[i]);

		int eSequencia, maxCompr = 1, tmpCompr=1;
		for (int i=0; i<qtdNums-1; i++){

			if (vetor[i]<vetor[i+1]) tmpCompr++;
			else if(tmpCompr>maxCompr) {
				maxCompr = tmpCompr;
				tmpCompr = 1;
			}
		}
		maxCompr = maxCompr>tmpCompr? maxCompr : tmpCompr;
		printf("\e[32m%d\n\e[m", maxCompr);

	}while (1);

	return 0;
}