#include <stdio.h>

void f(int x, int y){
    printf("%d\n", x - y);
}

int main(int argc, char const *argv[])
{
    f('二', '一');
    return 0;
}
