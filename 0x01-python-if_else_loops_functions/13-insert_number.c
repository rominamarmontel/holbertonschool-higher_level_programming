#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - function that inserts a number into a linked list
 * @head: a pointer to a pointer pointing at the beginning of a linked list
 * @number: the value of the node
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *prev;
	listint_t *temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	while (temp != NULL)
	{
		if (temp->n > new->n)
		{
			break;
		}
		prev = temp;
		temp = temp->next;
	}
	if (temp == *head)
	{
		new->next = *head;
		head = &new;
	}
	else
	{
		prev->next = new;
		new->next = temp;
	}
	return (0);
}
