#include "lists.h"

/**
 * check_cycle - Check cycle of a linked list
 * @list: linked list
 * Return: 1 on success, 0 on failure
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
