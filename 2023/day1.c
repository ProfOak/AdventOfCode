#define _GNU_SOURCE
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define is_digit(c) '0' <= c &&c <= '9'

int find_number(char *line, bool include_strings);
bool starts_with(char *prefix, char *line);

int main(void) {
    FILE *f;
    char *line;
    size_t len = 0;
    int part_one = 0;
    int part_two = 0;

    f = fopen("day1.input", "r");
    while (getline(&line, &len, f) != -1) {
        part_one += find_number(line, false);
        part_two += find_number(line, true);
    }

    printf("%d\n", part_one);
    printf("%d\n", part_two);
    fclose(f);
    return 0;
}

int find_number(char *line, bool include_strings) {
    int numbers[100] = {0};
    int numbers_index = -1;
    char *number_list[10] = {
        "zero", "one", "two",   "three", "four",
        "five", "six", "seven", "eight", "nine",
    };

    for (int i = 0; *line != '\0'; line++, i++) {
        if (is_digit(*line)) {
            numbers_index++;
            numbers[numbers_index] = *line - '0';
            continue;
        }

        if (include_strings) {
            for (int list_i = 0; list_i < 10; list_i++) {
                if (starts_with(number_list[list_i], line)) {
                    numbers_index++;
                    numbers[numbers_index] = list_i;
                    break;
                }
            }
        }
    }
    return (numbers[0] * 10) + numbers[numbers_index];
}

bool starts_with(char *prefix, char *string) {
    for (int i = 0; i < strlen(prefix); i++) {
        // Reached the end of the string or there's a mismatch.
        if (string[i] == 0 || prefix[i] != string[i]) {
            return false;
        }
    }
    return true;
}
