#include <stdio.h>

int main() {
    int matriz[4][4];
    int i, j, soma = 0;

    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            printf("Digite o elemento [%d][%d]: ", i, j);
            scanf("%d", &matriz[i][j]);
            soma += matriz[i][j];
        }
    }

    printf("Soma = %d\n", soma);

    return 0;
}
