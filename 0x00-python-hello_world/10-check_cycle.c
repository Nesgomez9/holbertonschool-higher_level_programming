#include "lists.h"

/**
 * check_cycle - function in C that checks if a singly linked list has
 *  a cycle in it
 * @list: head of singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head;

	if (!list)
		return (0);

	while (list)
	{
		head = list;
		list = list->next;
		if (head <= list)
			return (1);
	}
	return (0);
}
