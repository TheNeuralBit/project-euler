#include <stdio.h>
#define MAX 1000000

int main () {
    short collatz_lengths[MAX];
    int max = 1;
    int result;
    collatz_lengths[0] = 1;

    for (int i = 2; i < MAX; ++i) {
        long curr = i;
        int length = 0;
        while (curr >= i && curr != 1) {
            length++;
            if (curr % 2 == 0) curr /= 2;
            else curr = 3*curr + 1;
        }
        length += collatz_lengths[curr - 1];
        collatz_lengths[i - 1] = length;
        if (length > max) {
            max = length;
            result = i;
        }
    }
    printf("%d (len=%d)\n", result, max);
}
