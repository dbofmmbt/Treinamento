#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    char vermelho[13] = "\033[05;31;40m";
    printf("%sEssa frase é vermelha!\n", vermelho);
    return 0;
}
