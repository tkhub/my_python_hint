#include <stdio.h>

int main (int argc, char * argv[])
{
    int cnt;
    printf("%d",argc);
    for(cnt = 0; cnt < argc; cnt++)
    {
        printf(",%s", argv[cnt]);
    }
}
