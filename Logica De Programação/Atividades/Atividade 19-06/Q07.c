#include <stdio.h>

int main() {
    int matriz[3][4];
    int i, j, cont = 0;

    for (i = 0; i < 3; i++) {
        for (j = 0; j < 4; j++) {
            printf("Digite o elemento [%d][%d]: ", i, j);
            scanf("%d", &matriz[i][j]);
        }
    }

    for (i = 0; i < 3; i++) {
        for (j = 0; j < 4; j++) {
            if (matriz[i][j] % 2 == 0) {
                cont++;
            }
        }
    }

    printf("Quantidade de numeros pares: %d\n", cont);

    return 0;
}