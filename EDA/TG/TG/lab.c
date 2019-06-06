#include "TG.h"

int testek(TG * g, int k){
  int aux = 0;
  TVIZ * p = g->prim_viz;
  while(p){
    aux++;
    p = p->prox_viz;
  }
  if (aux != k) return 0;
  else if (!g->prox_no) return 1;
  else return testek(g->prox_no, k);
}

int ig(TG * g1, TG * g2){
  // Checar se g1 está contido em g2
  for( TG * p1 = g1; p1; p1 = p1->prox_no){
    if (!busca_no(g2, p1->id_no)) return 0;
    for(TVIZ * v = p1->prim_viz; v; v = v->prox_viz)
      if (!busca_aresta(g2, p1->id_no, v->id_viz)) return 0;
  }

  // Checar se g2 está contido em g1
  for( TG * p2 = g2; p2; p2 = p2->prox_no){
    if (!busca_no(g1, p2->id_no)) return 0;
    for(TVIZ * v = p2->prim_viz; v; v = v->prox_viz)
      if (!busca_aresta(g1, p2->id_no, v->id_viz)) return 0;
  }
  return 1;
}