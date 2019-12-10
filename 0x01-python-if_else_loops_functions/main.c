#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;

	head = NULL;
	add_nodeint_end(&head, 30);
	add_nodeint_end(&head, 36);
	add_nodeint_end(&head, 55);
	add_nodeint_end(&head, 98);
	print_listint(head);

	printf("-----------------\n");

	insert_node(&head, 1);
	insert_node(&head, 99);

	print_listint(head);

	free_listint(head);

	return (0);
}
