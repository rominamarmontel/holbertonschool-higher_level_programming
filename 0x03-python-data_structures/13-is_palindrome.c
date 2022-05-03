#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome: checks if a singly linked list is a palindrome.
 * @head: param
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int idx = 0;
	int i = 0;
	int j = 0;
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
			return (1);
		}
		i++;
		j++;
	}
	return (0);
 }
