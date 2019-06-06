#include <stdio.h>
#include <stdlib.h>

void printa_algo_em_volta(void (*printa_coisa)(void)){
    printf("MAOE\n");
    printa_coisa();
    printf("Cabô\n");
}

void printa(void){
    printf("Te amo <3\n");
}

int main(void){
    printa();
    printa_algo_em_volta(printa);
}