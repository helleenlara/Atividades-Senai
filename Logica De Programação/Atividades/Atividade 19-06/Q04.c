#include <stdio.h>

int main() {
    int matriz[5][5];
    int i, j, menor;

    for (i = 0; i < 5; i++) {
        for (j = 0; j < 5; j++) {
            printf("Digite o elemento [%d][%d]: ", i, j);
            scanf("%d", &matriz[i][j]);
        }
    }

    menor = matriz[0][0];
    for (i = 0; i < 5; i++) {
        for (j = 0; j < 5; j++) {
            if (matriz[i][j] < menor) {
                menor = matriz[i][j];
            }
        }
    }

    printf("Menor elemento: %d\n", menor);

    return 0;
}
