#include <stdio.h>

int main()
{
    char buf[4];
    for (int i=0; i<4; i++){
        buf[i] = getchar();
    }

    if ((int)buf[22] % 3 == 0) {
        printf (" It is a main() function ");
    }

    if ((int)buf[22] % 3 == 0) {
        printf (" It is a main() function ");
    }

    for (int i=0; i<4; i++){
        buf[i] = getchar();
    }
    return 0;
}