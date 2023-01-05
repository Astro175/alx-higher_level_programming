#include "lists.h"

/**
 * insert_node - Inserts a number at a node
 * @head: head of list
 * @number: n
 * Return: new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(new));

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head)
	{
		*head = new;
		return (new);
	}

	current = *head;
	if (current->n > number)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current->next && current->next->n < number)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}
