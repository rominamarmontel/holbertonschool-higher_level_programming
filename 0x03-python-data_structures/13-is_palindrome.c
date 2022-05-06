#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - Return is a list s palindrome or not
 * @head:  double ponter to head
 *
 * Return: 1 on success
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int count;
	int i;
	int arr[2046];

	temp = *head;
	count = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		arr[count] = temp->n;
		temp = temp->next;
		count++;
	}
	for (i = 0; i < count; i++)
	{
		if (arr[i] == arr[count - 1])
			count--;
		else
			return (0);
	}
	return (1);
}
