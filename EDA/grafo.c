#include "LibsUteis.h"
#include "grafo.h"

struct viz {
  int id;
  struct viz * prox_viz;
};

struct grafo {
  int id;
  TVIZ * lista_viz;
  struct grafo * prox_no;
};

TG * inicializa(void){
  return NULL;
}

TG * busca_no(TG * g, int x){
  TG * p = g;
  while ((p) && (p->id != x))
    p = p->prox_no;
  return p;
}

TVIZ * busca_aresta(TG * g, int no1, int no2){
  TG * p = g;

  while ((p) && (p->id != no1) && (p->id != no2))
    p = p->prox_no;

  if (!p) return NULL;

  int x;
  if (p->id == no1) x = no2;
  else x = no1;
  TVIZ * resp = p->lista_viz;

  while ((resp) && (resp->id != x))
    resp = resp->prox_viz;

  return resp;
}

void imp_viz(TVIZ * viz){
  if(viz){
    printf("%d", viz->id);
    imp_viz(viz->prox_viz);
  }
}

void imprime(TG * g){
  if(g){
    printf("%d:", g->id);
    imp_viz(g->lista_viz);
    printf("\n");
    imprime(g->prox_no);
  }
}