#include <stdio.h>

void findFactorial(int n, long *f)
{
    int i;
    *f = 1;

    for (i = 1; i <= n; i++)
    {
        *f = (*f) * i;
    }
}

int main()
{
    int num;
    long result;

    scanf("%d", &num);

    findFactorial(num, &result);

    printf("Factorial:%ld\n", result);

    return 0;
}
