typedef struct noPilha NoPilha;
typedef struct pilha Pilha;

void push(Pilha * p, int el);
int pop(Pilha * p);
int vazio(Pilha * p);
Pilha * cria(void);
void imprime(Pilha * p);
void libera(Pilha * p);