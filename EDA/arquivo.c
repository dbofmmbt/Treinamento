/*
*Operações:
    - Abertura
    - Leitura e/ou escrita
    - Fechamento

        | Texto        | Binário
----------------------------------------------
Acesso? | Sequencial   | Direto
----------------------------------------------
Info?   | Legibilidade | Linguagem de máquina

*stdio.h: ponteiro p/ arquivo => FILE *fp;
Até 25 arquivos abertos simultaneamente.

*Abertura
FILE *fopen(char *nome, char *modo);
    -> not NULL, OK
    -> NULL, ERROR

modo?
    - b ou t (binário ou texto)
    - r(somente leitura), w(somente escrita), a(concatena) (+)

    r+b    rb+ (leitura em arquivo binário com possíveis modificações)
    w+b ou wb+ (sentido? kd?)
    a+b    ab+ (append em arquivo binário)

FILE *fp = fopen("entrada", "rb+");
if(!fp) exit(1); (fecha todos os arquivos abertos no programa)

int fclose(FILE *fp);
    ->0, OK
    ->EOF, ERROR

fclose(fp);

(1) Arquivos texto
    *leitura
    int fscanf(FILE *fp, char * modo, <END_VAR>); (retorna o número de variáveis lidas com sucesso)
    *escrita
    int fprintf(FILE *fp, char *modo, <LISTA_VAR>); (retorna o número de bytes (ou caracteres) escritos com sucesso)
*/

#include <stdio.h>
#include <stdlib.h>

void merge(char *na1, char *na2, char *resp){
    FILE *fp1, *fp2, *out;
    fp1 = fopen(na1, "rt");
    if (!fp1) exit(1);
    fp2 = fopen(na2, "rt");
    if (!fp2) exit(1);
    out = fopen(resp, "w");
    if (!out) exit(1);
    int r1, r2, n1, n2;

    r1 = fscanf(fp1, "%d", &n1);
    r2 = fscanf(fp2, "%d", &n2);

    while ((r1 == 1) && (r2 == 1)) {
        if((n1 <= n2) || ((r1 == 1) && (r2 != 1))) {
            fprintf(out, "%d\n", n1);
            r1 = fscanf(fp1, "%d", &n1);
        }
        else {
            fprintf(out, "%d\n", n2);
            r2 = fscanf(fp2, "%d", &n2);
        }
    }
    fclose(fp1);
    fclose(fp2);
    fclose(out);
    
}

/*
    2) Arquivos Binários
    
    int fread(void * pelem, int tam, int nelem, FILE * fp);

    fread => nelem, OK.
          => < nelem, ERRO.
    
    int fwrite(void * pelem, int tam, int nelem, FILE * fp);

    fwrite => nelem, OK.
           => < nelem, ERRO.

    OPERAÇÕES ADICIONAIS E IMPORTANTES PARA ARQUIVOS BINÁRIOS

    A) int fseek(FILE * fp, long int offset, int ORIGEM);

            => SEEK_CUR
    ORIGEM  => SEEK_SET
            => SEEK_END

    fseek => 0, OK
          => != 0, ERRO
    
    B) long int ftell(FILE * fp);

    ftell => -1L, ERRO
          => != -1L, OK

    C) void rewind(FILE * fp); === fseek(fp, 0L, SEEK_SET);

    3) Arquivos Texto

    FILE * fopen(char * nome, char * modo);
    void fclose(FILE * fp);
    int fscanf(FILE * fp, char * form, <END_VAR>);
    int fprintf(FILE * fp, char * form, <VAR>);

    ORDENAÇÃO DE ARQUIVOS TEXTO
        * suposição: Arquivos que não cabem em Memória Principal.

    Sub divisão em 2 problemas:
        1) Geração de Partições ordenadas (ou classificadas); e
        2) Intercalação dessas partições p/ geração do arquivo final ordenado.

    GERAÇÃO DE PARTIÇÕES CLASSIFICADAS

    Maneira 1 - Classificação Interna


    Maneira 2 - Seleção com Substituição

        * ALGORITMO:
        1) Ler M dados para a Memória Principal;
        2) Selecionar a menor chave R desses M dados;
        3) Gravar R na partição;
        4) Substituir R pelo próximo dado do arquivo original, P.
            Se P < R, congela posição. Senão, vá P/ 2).
        5) Se existem posições descongeladas, vá P/ 2). Senão,
            -> Fechar partição;
            -> Descongelar posições;
            -> Abrir nova partição;
            -> Voltar P/ 2.
    

    Maneira 3 - Seleção Natural

        * ALGORITMO:
        1) Ler M dados para a Memória Principal;
        2) Selecionar o menor valor R desses M dados;
        3) Gravar R na partição;
        4) Substituir, na MP, R pelo próximo P.
            Se P > R, vai para 2). Senão, gravar
            no reservatório (RES) e voltar p/ 4),
            enquanto RES não estiver cheio, ou P < R.
        5) Quando RES estiver cheio:
            -> Fechar Partição;
            -> Copiar RES para MP;
            -> Esvaziar RES;
            -> Abrir Nova Partição;
            -> Voltar para 2).
    
*/