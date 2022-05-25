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
    listint_t *prev;
    listint_t *temp = *head;
    if (new == NULL)
        return (NULL);
    new->n = number;
    while (temp != NULL)
    {/*insert ichi wo kimeru*/
        if (temp->n > number)/*insert ichi ga mitsukaru*/
            break;
        prev = temp;/*temp wo mae no node toshite oboeru*/
        temp = temp->next;/*tsugi no node e susumu*/
    }
    if (*head == NULL)/*moshimo sento ga NULL no baai*/
    {
        new->next = NULL;
        *head = new;/*list no sento wo new ni suru*/
    }
    else
    {
        new->next = temp;/*tuika ichi ga owari no baai wa temp*/
        if (temp == *head)/*tsuika ichiga sento no baai*/
            *head = new;/*sento ni new wo tuika*/
        else
            prev->next = new;
    }
    return (new);
}
