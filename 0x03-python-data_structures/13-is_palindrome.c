#include "lists.h"
/**
 * is_palindrome - Checks if a list is palindrome or not
 * @head: head node
 * Return: 1 if palindromel, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	int values[100];
	int i = 0;

	while (fast != NULL && fast->next != NULL)
	{
		values[i++] = slow->n;
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	while (slow != NULL)
	{

		if (values[--i] != slow->n)
		{
			return (0);
		}
		slow = slow->next;
	}

	return (1);
}

