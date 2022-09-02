#include <stdio.h>

int main(int argc, char const *argv[])
{
    for (size_t i = 0; i < 3; i++)
    {
        /* works just fine */
        printf("%d ", i);
        
    }

    for (int i = -3; i < 3; i++)
    {
        /* works just fine */
        printf("%d ", i);
        
    }
    
    return 0;
}
