#include <stdio.h>

int copy(char* src, char* dst);

int main(int argc, char const *argv[])
{
    char a[] = {"test"};
    char b[sizeof(a)/sizeof(a[0])];
    copy(a, b);
    printf(b);
}

int copy(char* src, char* dst){
    printf(src);
    while (!src)
    {
        *dst = *src;
        src++; dst++;
    }
    
}