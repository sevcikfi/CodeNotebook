#include <stdio.h>

int main(int argc, char const *argv[])
{
    while (1)
    {
        int c;
        if ((c = getchar()) == EOF)
        {
            return(0);
        }
        printf("%c",c);
    }
    
    return 0;
}
