#include <stdio.h>
#include <string.h>

/**
 * main - string reversal
 */

void main(void)
{
	char s1[30], new_name[15];

	printf("Enter your name: ");
	scanf("%s", s1);

	new_name = strev(s1);
	printf("%s\n", new_name);
}
