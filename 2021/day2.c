#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BUFFER 100
#define MAX_INPUT 1000
#define streq(a, b) strcmp(a, b) == 0

struct command_t {
    char *direction;
    int distance;
} command_t;

int part1(struct command_t *command, int size);
int part2(struct command_t *command, int size);

int main(void) {
    int size = 0;
    FILE *fp;
    char buffer[MAX_BUFFER];
    struct command_t commands[MAX_INPUT];

    fp = fopen("day2.input", "r");

    for (int i = 0; fgets(buffer, MAX_BUFFER, fp) != NULL; i++) {
        commands[i].direction = strdup(strtok(buffer, " "));
        commands[i].distance = atoi(strtok(NULL, " "));
        size++;
    }
    fclose(fp);

    printf("%d\n", part1(commands, size));
    printf("%d\n", part2(commands, size));
    return 0;
}

int part1(struct command_t *commands, int size) {
    int x = 0;
    int y = 0;

    for (int i = 0; i < size; i++) {
        if (streq(commands[i].direction, "forward")) {
            x += commands[i].distance;
        } else if (streq(commands[i].direction, "up")) {
            y -= commands[i].distance;
        } else if (streq(commands[i].direction, "down")) {
            y += commands[i].distance;
        }
    }

    return x * y;
}

int part2(struct command_t *commands, int size) {
    int x = 0;
    int y = 0;
    int aim = 0;

    for (int i = 0; i < size; i++) {
        if (streq(commands[i].direction, "forward")) {
            x += commands[i].distance;
            y += commands[i].distance * aim;
        } else if (streq(commands[i].direction, "up")) {
            aim -= commands[i].distance;
        } else if (streq(commands[i].direction, "down")) {
            aim += commands[i].distance;
        }
    }

    return x * y;
}
