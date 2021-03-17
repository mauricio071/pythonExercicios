#include <stdio.h>
#include <malloc.h>

void imprimir(int * x);
void popular(int * x);

void main(void) {
    int *x;

    x = (int * ) malloc(12 *sizeof(int));
    popular(x);
    imprimir(x);
    free(x);

    x = (int *) malloc(8 * sizeof(int));
    imprimir(x);
    free(x);
}

void imprimir(int*x) {
    printf("\nOs valores do vetor: ");
    int i;
    for(i = 0; i < 12; i++) {
        printf("\t%d",x[i]);
    }
}

void popular(int * x) {
    x[0] = 1; x[1] = 12; x[2] = 42; x[3] = 26; x[4] = 96; x[5] = 102;
    x[6] = 3; x[7] = 17; x[8] = 37; x[9] = 9; x[10] = 11; x[11] = 45;
}