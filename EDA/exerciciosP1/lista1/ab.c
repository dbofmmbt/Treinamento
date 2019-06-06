#include "../../LibsUteis.h"

typedef struct ab{
  int info;
  struct ab *esq, *dir;
} TAB;

TAB * cria(int info, TAB * esq, TAB * dir){
  TAB * novo = (TAB *) malloc(sizeof(TAB));
  novo->info = info;
  novo->esq = esq;
  novo->dir = dir;
  return novo;
}

TAB * copia(TAB * a){
  if (!a) return a;
  TAB * novo = cria(a->info, NULL, NULL);
  novo->esq = copia(a->esq);
  novo->dir = copia(a->dir);
  return novo;
}

TAB * espelho(TAB * a){
  if (!a) return a;
  TAB * novo = cria(a->info, NULL, NULL);
  novo->esq = espelho(a->dir);
  novo->dir = espelho(a->esq);
  return novo;
}

void imprime(TAB * a){
  if (!a) return;
  imprime(a->esq);
  printf("%d", a->info);
  imprime(a->dir);
}

TAB * maior(TAB * a){
  if (!a) return a;
  TAB * esq = maior(a->esq);
  TAB * dir = maior(a->dir);
  TAB * maior;
  if (esq && dir)
    maior = esq->info > dir->info ? esq : dir;
  else if (esq) maior = esq;
  else if (dir) maior = dir;
  else return a;
  maior = a->info > maior->info ? a : maior;
  return maior;
}

int igual (TAB* a1, TAB* a2){
  if(!a1 && !a2) return 1;
  if ((!a1 || !a2) && (a1 || a2)) return 0;
  if (a1->info != a2->info) return 0;
  int esq = igual(a1->esq, a2->esq);
  int dir = igual(a1->dir, a2->dir);
  if (esq+dir == 2) return 1;
  else return 0;
  ;
}

int main(void){
  TAB * arv_esq = cria(25, NULL, NULL);
  TAB * arv_dir = cria(8, NULL, NULL);
  TAB * arv = cria(15, arv_esq, arv_dir);
  imprime(arv);
  printf("\n");
  TAB * esp = copia(arv);
  printf("%d\n", igual(arv, esp));
  esp->dir->info = 3;
}