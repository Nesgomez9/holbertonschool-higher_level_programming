#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *new, *node;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	node = *head;
	tmp = node->next;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return(new);
	}
	while(tmp && number > tmp->n)
	{
		node = tmp;
		tmp = tmp->next;
	}
	new->next = tmp;
	node->next = new;
	return (new);
}
