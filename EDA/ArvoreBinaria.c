#include "ArvoreBinaria.h"

struct noAB{
    int info;
    struct noAB * esq;
    struct noAB * dir;
};

AB * retira_abb(AB * a, int el){
    if (!a) return a;
    if (el > a->info)
        a->dir = retira_abb(a->dir, el);
    else if ( el < a->info)
        a->esq = retira_abb(a->esq, el);
    else{  // Achei EL
        if ((!a->esq) && (!a->dir)){
            free(a);
            return NULL;
        } else if ((!a->esq) || (!a->dir)){
            AB * f;
            if (!a->dir) f = a->esq;
            else f = a->dir;
            free(a);
            return f;
        } else {
            AB * f = a->esq;
            while(f->dir) f = f->dir;
            a->info = f->info;
            f->info = el;
            a->esq = retira_abb(a->esq, el);
        }
    }
    return a;
}

AB * busca(AB * a, int x){
    if (!a || a->info == x) return a;
    if (a->info < x)
        return busca(a->esq, x);
    else return busca(a->dir, x);
}

AB * insere(AB * a, int el){
    if (!a) return cria_no(el, NULL, NULL);
    if (a->info == el) return a;
    else if (a->info > el)
        a->esq = insere(a->esq, el);
    else a->dir = insere(a->dir, el);
}

AB * cria_no(int info, AB * esq, AB * dir){
    AB * novo = (AB *) malloc(sizeof(AB));
    novo->info = info;
    novo->esq = esq;
    novo->dir = dir;
    return novo;
}