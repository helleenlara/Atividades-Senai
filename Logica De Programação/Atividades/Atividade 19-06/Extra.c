#include <stdio.h>
#define ALUNOS 5
#define NOTAS 4

int main() {
    float notas[ALUNOS][NOTAS];
    float media[ALUNOS];
    float somaGeral = 0, maiorMedia, menorMedia;
    int i, j;

    for (i = 0; i < ALUNOS; i++) {
        printf("=== Aluno %d ===\n", i + 1);
        float soma = 0;
        for (j = 0; j < NOTAS; j++) {
            printf("Nota %d: ", j + 1);
            scanf("%f", &notas[i][j]);
            soma += notas[i][j];
        }
        media[i] = soma / NOTAS;
    }

    printf("\n=== Resultados ===\n");
    maiorMedia = media[0];
    menorMedia = media[0];

    for (i = 0; i < ALUNOS; i++) {
        printf("Aluno %d - Media: %.2f - %s\n",
               i + 1, media[i],
               (media[i] >= 7.0) ? "APROVADO" : "REPROVADO");
        somaGeral += media[i];
        if (media[i] > maiorMedia) maiorMedia = media[i];
        if (media[i] < menorMedia) menorMedia = media[i];
    }

    printf("\nMaior media da turma: %.2f\n", maiorMedia);
    printf("Menor media da turma: %.2f\n", menorMedia);
    printf("Media geral da turma: %.2f\n", somaGeral / ALUNOS);

    return 0;
}
