#include <stdio.h>

int main() {
    int matriz[4][4];
    int i, j, soma = 0;
    float media;

    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            printf("Digite o elemento [%d][%d]: ", i, j);
            scanf("%d", &matriz[i][j]);
            soma += matriz[i][j];
        }
    }

    media = (float) soma / 16;
    printf("Media dos elementos: %.2f\n", media);

    return 0;
}

