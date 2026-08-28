#include <stdio.h>
#include <conio.h>

int main()
{
    int v, s;
    printf("SUM OF DIGITS\n\n");

    printf("Enter digit: "); scanf("%d", &v);
    /*USING FOR
    for(s=0; v; s+= v%10, v/=10);
    */
    while(v!= 0)
    {
        s += v%10;
        v /= 10;
    }
    printf("Sum of digits: %d", s);
    printf("\n");
    printf("Press any key to continue...\n");
    getch();
    return 0;
}
