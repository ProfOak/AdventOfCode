#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_SIZE 10
#define is_empty(line) strlen(line) == 0

// Return the index of the lowest calorie if the new_cals is bigger than at
// least one of them. If there's nothing lower in the array then return -1.
int is_bigger(int most_cals[3], int new_cals) {
    bool replace = false;
    int smallest = most_cals[0];
    int smallest_index = 0;

    for (int i = 0; i < 3; i++) {
        if (most_cals[i] < smallest) {
            smallest = most_cals[i];
            smallest_index = i;
        }
        if (new_cals > most_cals[i]) {
            replace = true;
        }
    }
    if (replace) {
        return smallest_index;
    }
    return -1;
}

int main(void) {

    FILE *fp;
    char line[MAX_LINE_SIZE];
    int total = 0;
    int index = 0;
    int most_cals[3] = {0, 0, 0};

    fp = fopen("day1.input", "r");
    for (int i = 0; fgets(line, MAX_LINE_SIZE, fp) != NULL; i++) {
        // strip new line char
        line[strcspn(line, "\n")] = 0;

        if (is_empty(line)) {
            index = is_bigger(most_cals, total);
            if (index >= 0) {
                most_cals[index] = total;
            }
            total = 0;
        }
        total += atoi(line);
    }

    fclose(fp);

    total = 0;
    for (int i = 0; i < 3; i++) {
        total += most_cals[i];
        printf("%d\n", most_cals[i]);
    }
    puts("---");
    printf("Total: %d\n", total);

    return 0;
}
