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
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *temp = *head;

	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		*head = new;
		new->next = temp;
	}
	else
	{
		while (temp->next != NULL && number > temp->next->n)
			temp = temp->next;
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}
