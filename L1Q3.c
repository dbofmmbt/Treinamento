#include <stdio.h>

int main(void){
	long long n, m, varPotencia;

	do{	// Enquanto N e M > 1

		scanf("%lld %lld", &n, &m);
		if (n <= 1 || m <= 1) return 0;

		varPotencia = m;
		printf("1 ");  // 1 é sempre potência de qualquer N^0.
		while (varPotencia < n){
			printf("%lld ", varPotencia);
			varPotencia *= m;
		}
		printf("\n");



	}while(1);

	return 0;
}