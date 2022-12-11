
#include <stdio.h>
#include <unistd.h>

int main () {
int real = getuid();
int euid = geteuid();
printf("The REAL UID =: %d\n", real);
printf("The EFFECTIVE UID =: %d\n", euid);
}