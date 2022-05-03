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
	listint_t *temp = *head;
	int idx = 0;
	int i = 0;
	int j = 0;
	int check = 0;
	int array[2048];

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		array[idx] = temp->n;
		temp = temp->next;
		idx++;
	}
	idx = idx - 1;
	j = idx;
	while (i <= (idx / 2) && j >= (idx / 2))
	{
		if (array[i] != array[j])
		{
			check = 1;
			break;
		}
		i++;
		j++;
	}
	if (check == 1)
		return (0);
	return (1);
}
