typedef struct noFila NoFila;
typedef struct fila Fila;

void insere(Fila * f, int el);
int retira(Fila * f);
int vazia(Fila * f);
void libera(Fila * f);
void imprime(Fila * f);