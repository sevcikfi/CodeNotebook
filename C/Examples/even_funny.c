#include <stdio.h>

int isEven(int num){
    double half = num / 2.0;
    double halfPlus = half + 0.1;
    if((int) halfPlus == half)
        return 1;
    else 
        return 0;
}

int main(int argc, char const *argv[])
{
    printf("%d: %d\n", 1, isEven(1));
    printf("%d: %d\n", 2, isEven(2));
    return 0;
}
