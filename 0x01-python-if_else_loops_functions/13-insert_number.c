#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - Insert a node in a singed linked list
 *
 * @head: Pointer to list to add the node
 * @number: number to add to the list
 * Return: Always 0.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *new, *node;


	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	node = *head;
	if (!node || number < node->n)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	tmp = node->next;
	while (tmp && number > tmp->n)
	{
		node = tmp;
		tmp = tmp->next;
	}
	new->next = tmp;
	node->next = new;
	return (new);
}
