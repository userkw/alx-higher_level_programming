#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_listint - reverses a linked list
 * @head: pointer
 *
 * Return: pointer to the first node
 */
void reverse_listint(listint_t **head)
{
	listint_t *pv = NULL;
	listint_t *crt = *head;
	listint_t *n = NULL;

	while (crt)
	{
		n = crt->n;
		crt->n = pv;
		pv = crt;
		crt = n;
	}

	*head = pv;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer
 *
 * Return: 1 if it is, 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *t = *head, *d = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		f = f->next->next;
		if (!f)
		{
			d = s->next;
			break;
		}
		if (!f->next)
		{
			d = s->next->next;
			break;
		}
		s = s->next;
	}

	reverse_listint(&d);

	while (d && t)
	{
		if (t->n == d->n)
		{
			d = d->next;
			t = t->next;
		}
		else
			return (0);
	}

	if (!d)
		return (1);

	return (0);
}
