#include <stdio.h>
#define N 4

int main() {
    int matriz[N][N];
    int i, j, soma = 0;

    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            printf("Digite o elemento [%d][%d]: ", i, j);
            scanf("%d", &matriz[i][j]);
        }
    }

    for (i = 0; i < N; i++) {
        soma += matriz[i][N - 1 - i];
    }

    printf("Soma da diagonal secundaria: %d\n", soma);

    return 0;
}
