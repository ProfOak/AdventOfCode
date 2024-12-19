/*
 */

#include <stdio.h>
#include <stdlib.h>

#define MAX_LINE_SIZE 10

enum RPS {
    Rock,
    Paper,
    Scissors,
} RPS;

enum RPS translate_code(char code) {
    if (code == 'A' || code == 'X') {
        return Rock;
    } else if (code == 'B' || code == 'Y') {
        return Paper;
    }
    return Scissors;
}

/*
 * Points:
 *  You select rock: 1, paper: 2, scissors: 3
 *  You lose: 0, draw: 3, win: 6
 */
int rps_score(int player, int opponent) {
    int total = player + 1;
    if ((player + 1) % 3 == opponent) {
        total += 0;
    } else if (player == opponent) {
        total += 3;
    } else {
        total += 6;
    }

    return total;
}

int main(void) {

    FILE *fp;
    char line[MAX_LINE_SIZE];
    int player;
    int opponent;
    int total = 0;

    fp = fopen("day2.input", "r");
    while (fgets(line, MAX_LINE_SIZE, fp) != NULL) {
        // Column 1: A for Rock, B for Paper, and C for Scissors
        opponent = translate_code(line[0]);

        // Column 2: X for Rock, Y for Paper, and Z for Scissors
        player = translate_code(line[2]);
        total += rps_score(player, opponent);
    }

    printf("%d\n", total);
    fclose(fp);
    return 0;
}
