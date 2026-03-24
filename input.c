#include <stdio.h>

int main() {
    char name[20];
    printf("Enter your name: ");
    scanf("%s", name);
    printf("Hello %s! Your C program is working.\n", name);
    return 0;
}
