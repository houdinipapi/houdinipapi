#include <stdio.h>

int calculator(void);

/**
 * main - calls the calculator function
 */

void main(void)
{
	calculator();
}

/**
 * calculator - simple calculations
 * Return: Success
 */

int calculator(void)
{
	int a, b, c;
	int sum, prod, diff, division;

	printf("Enter two numbers and a calculation sign:\n");
	scanf("%d%d%d", &a, &b, &c);

	if (c == +)
	{
		return (a + b);
	}
	else if (c == -)
	{
		return (a - b);
	}
	else if (c == *)
	{
		return (a * b);
	}
	else if (c == /)
	{
		return (a / b);
	}
	else
		printf("Enter Valid Operator\n");
}
