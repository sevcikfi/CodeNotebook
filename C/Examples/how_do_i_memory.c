#include <stdio.h>

int main(int argc, char const *argv[])
{
    int x = 69420;
    int *px = &x;
    char string[] = {"pointerinos"};
    //int mem stuff
    printf("Val: x\t   %d, Mem: px\t %d\n", x, px);
    printf("Val: *px   %d, Mem: *x\t %d\n", *px, &x);
    printf("Val: *(&x) %d, Mem: &(*px)\t %d\n", x, px);
    printf("Val: ++x   %d, Mem: &x+1\t %d\n", ++x, &x+1);
    printf("Val: *&x+1 %d, Mem: &x+1\t %d\n", *(&x-1), &x-1);
    //char arr stuff
    //printf("arr stuf, -1 index, begin, middle, last, len+1\n");
    //printf("Val: x\t   %d, Mem: px\t %d\n", string[-1], &string[-1]);
    //printf("Val: x\t   %c, Mem: px\t %d\n", string[0], &string[0]);
    //printf("Val: x\t   %c, Mem: px\t %d\n", string[5], &string[5]);
    //printf("Val: x\t   %c, Mem: px\t %d\n", string[10], &string[10]);
    //printf("Val: x\t   %d, Mem: px\t %d\n", string[11], &string[11]);
    int len = (sizeof(string)/sizeof(string[0]))+8;
    for (int i = -3; i < len; ++i)
    {
        printf("Val:%d\t Mem: %d\n", string[i], &string[i]);
    }
    return 0;    
}
