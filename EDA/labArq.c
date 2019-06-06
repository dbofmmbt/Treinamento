#include "LibsUteis.h"

void bolhaBin(char * nomeArq){
  FILE * fp = fopen(nomeArq, "rb+");
  if (!fp) exit(1);
  int n1, n2, pos1, pos2, trocou, r;

  do {
    trocou = 0;
    pos1 = 0;
    fread(&n1, sizeof(int), 1, fp);
    pos2 = ftell(fp);
    r = fread(&n2, sizeof(int), 1, fp);
    while (r){
      if (n1 > n2){
        fseek(fp, pos1, SEEK_SET);
        fwrite(&n2, sizeof(int), 1, fp);
        fseek(fp, pos2, SEEK_SET);
        fwrite(&n1, sizeof(int), 1, fp);
        trocou = 1;
      } else {
        fseek(fp, sizeof(int), SEEK_CUR);
      }
      n1 = n2;
      pos1 = pos2;
      pos2 = ftell(fp);
      r = fread(&n2, sizeof(int), 1, fp);
    }
    fseek(fp, 0, SEEK_SET);
  } while (trocou);
}

int main(void){
  FILE * f = fopen("int.bin", "wb");
  int n = 5;
  fwrite(&n, sizeof(int), 1, f);

  n = 4;
  fwrite(&n, sizeof(int), 1, f);
  bolhaBin("int.bin");
  fseek(f, 0, SEEK_SET);
  fread(&n, sizeof(int), 1, f);
  printf("%d\n", n);
  fread(&n, sizeof(int), 1, f);
  printf("%d\n", n);
}