#include "lists.h"
/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: param
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (temp && list && temp->next)
	{
		list = list->next;
		temp = temp->next->next;
		if(list == temp)
		return (1);
	}
	return (0);
}
