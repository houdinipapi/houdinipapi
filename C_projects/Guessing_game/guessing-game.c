#include <stdio.h>

/**
 * main - guessing game
 * Return: 0
 */

int main(void)
{
	int luckyNumber;

	do {
		printf("Guess a lucky number: ");
		scanf("%d", &luckyNumber);
	} while (luckyNumber != 7);

	if (luckyNumber == 7)
	{
		printf("YEES!! That's our LUCKY NUMBER!!\n");
	}

	return (0);
}
