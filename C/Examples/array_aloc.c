/* 
 * This one was used to test and see how C handles dynamic array allocation.
 * In other words, seeing how compilers handles the memory allocation and
 * computation of sizeof() operand via https://godbolt.org/ (ARM and RISC-V)
 * compilers with and without -O1 flag and LLVM via RISC-V.
 */
#include <stdio.h>

int main(void)
{
	int fixed[1024];
	size_t fixedsize = sizeof (fixed) / sizeof (fixed[0]);
    int n;
    printf("Gib number: ");
    scanf("%d", &n);
	printf("Fixed size: %zu, fixed length: %zu\n", sizeof(fixed), fixedsize);
    int dyn[n];
    size_t dynSize = sizeof(dyn) / sizeof (dyn[0]);
	printf("Dynam size: %zu, dynam length: %zu\n", sizeof(dyn), dynSize);
}