#include "LibsUteis.h"

typedef noAB AB;

AB * inicializa(void);
AB * cria(int raiz, AB * sae, AB * sad);
void libera(AB * a);
AB * busca(AB * a, int el);
AB * v2a(int * vet, int tam);
void insere_abb(AB * a, int el);