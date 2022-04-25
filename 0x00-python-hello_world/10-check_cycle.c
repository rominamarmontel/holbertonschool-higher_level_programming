#include "lists.h"
/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: param
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (!list)
		return (0);
	temp = list;
	while (list->next != NULL)
	{
		if (temp == list->next)
		{
			return (1);
		}
		list = list->next;
	}
	return (0);
}

