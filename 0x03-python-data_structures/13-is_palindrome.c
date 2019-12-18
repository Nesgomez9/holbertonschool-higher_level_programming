#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * list_len - check the code for Holberton School students.
 *
 * @h: h
 * Return: Always 0.
 */
int list_len(const listint_t *h)
{
	int size = 0;

	while (h)
	{
		h = h->next;
		size++;
	}
	return (size);
}
/**
 * is_palindrome - check the code for Holberton School students.
 *
 * @head: The header of the linked list
 * Return: 1 if the list is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp1, *tmp2;
	int i, size, size1, start, count;

	if (!head)
		return (0);
	if (!*head)
		return (1);
	tmp1 = *head;
	start = count = 0;
	size = size1 = list_len(tmp1);
	while (count < size1 / 2)
	{
		tmp1 = tmp2 = *head;
		i =  0;
		while (i < start)
		{
			tmp1 = tmp1->next;
			i++;
		}
		i = 0;
		while (i < size - 1)
		{
			tmp2 = tmp2->next;
			i++;
		}
		if (tmp1->n != tmp2->n)
			return (0);
		start++;
		size--;
		count++;
	}
	return (1);
}
