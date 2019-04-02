#include "Pilha.h"

struct noPilha {
    int info;
    struct noPilha * prox;
};

struct pilha {
    NoPilha * topo;
};