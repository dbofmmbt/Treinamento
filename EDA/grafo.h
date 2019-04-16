/*

# GRAFOS

G = (V, E)

> Grafo Conectado vs Grafo Não-Conectado

O-----O                 O----O----O
 \   /                   \   |
  \ /                      - O      O
   O

> Grafo Orientado vs Não-Orientado

O<-------O---->O          O-----O-----O

> Vizinhos? Vértices Adjacentes

> Grau?

  Não orientado: Somatório de todos os vizinhos

  Orientado: Somatório dos que saem + Somatórios dos que chegam

> Ciclos?

O---O
|   |
O---O

> Componentes Conexos (CC):

  Quantidade de grupos de vértices interconectados.


## Lista de Adjacências

  É uma boa maneira de representação de grafos por ser bem flexível
  quanto a adição e remoção de vértices e arestas do grafo.

  Utiliza-se uma lista para registrar cada vértice do grafo. Além disso,
  Cada nó possui uma lista de arestas associado a ele, indicando com quais
  outros vértices um determinado elemento está associado.

*/

typedef struct viz TVIZ;

typedef struct grafo TG;

TG * inicializa(void);
TG * busca_no(TG * g, int x);
TVIZ * busca_aresta(TG * g, int no1, int no2);
void imp_viz(TVIZ * viz);
void imprime(TG * g);
